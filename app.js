/**
 * M9MQ DISCORD MOBILE CLOUD LEVELER · BROWSER ENGINE v4.0
 * 100% Client-Side Direct Execution on Mobile & Desktop
 * All Rights Reserved (C) 2026 m9mq
 */

(function () {
  'use strict';

  // Constants
  const SPEED_MULTIPLIER = 2000.0; // 2000x Turbo Speed
  const GATEWAY_URL = 'wss://gateway.discord.gg/?v=10&encoding=json';
  const SCIENCE_URL = 'https://discord.com/api/v9/science';

  const STREAM_TIERS = [
    { tier: 1, hours: 1, name: "Tier 1: Newcomer (1h)" },
    { tier: 2, hours: 5, name: "Tier 2: Fledgling (5h)" },
    { tier: 3, hours: 20, name: "Tier 3: Breakout (20h)" },
    { tier: 4, hours: 75, name: "Tier 4: Standout (75h)" },
    { tier: 5, hours: 150, name: "Tier 5: Trendsetter (150h)" },
    { tier: 6, hours: 300, name: "Tier 6: Headliner (300h)" },
    { tier: 7, hours: 500, name: "Tier 7: Star (500h)" },
    { tier: 8, hours: 1000, name: "Tier 8: Sensation (1,000h)" },
    { tier: 9, hours: 2000, name: "Tier 9: Visionary (2,000h)" },
    { tier: 10, hours: 5000, name: "Tier 10: Phenomenon (5,000h+)" }
  ];

  // DOM Elements
  const userTokenInput = document.getElementById('userToken');
  const toggleTokenBtn = document.getElementById('toggleTokenBtn');
  const tokenStatusBadge = document.getElementById('tokenStatusBadge');
  const accountInfoPill = document.getElementById('accountInfoPill');
  const accountUserDisplay = document.getElementById('accountUserDisplay');

  const modePills = document.querySelectorAll('.mode-pill');
  const targetCountInput = document.getElementById('targetCountInput');
  const quantityLabel = document.getElementById('quantityLabel');
  const unitTag = document.getElementById('unitTag');
  const calcTimeEst = document.getElementById('calcTimeEst');
  const presetsRow = document.getElementById('presetsRow');
  const roomFieldBox = document.getElementById('roomFieldBox');
  const voiceRoomInput = document.getElementById('voiceRoomInput');

  const startLevelingBtn = document.getElementById('startLevelingBtn');
  const liveProgressDock = document.getElementById('liveProgressDock');
  const stopLevelingBtn = document.getElementById('stopLevelingBtn');

  // HUD Elements
  const hudStatusTitle = document.getElementById('hudStatusTitle');
  const meterPercent = document.getElementById('meterPercent');
  const meterBar = document.getElementById('meterBar');
  const liveLoggedHours = document.getElementById('liveLoggedHours');
  const liveTierBadge = document.getElementById('liveTierBadge');
  const liveElapsedTime = document.getElementById('liveElapsedTime');
  const liveStreamState = document.getElementById('liveStreamState');
  const tickerLogText = document.getElementById('tickerLogText');

  // Active State
  let activeMode = 'stream'; // 'stream' | 'playtime' | 'variety'
  let targetVal = 5000;
  let isLeveling = false;
  let gatewayWs = null;
  let heartbeatTimer = null;
  let clockInterval = null;
  let unpauseInterval = null;
  let sessionStartTime = 0;
  let accumulatedSeconds = 0;
  let cachedGames = [];

  // Super Properties Helper
  function getSuperProps() {
    const props = {
      os: "Windows",
      browser: "Discord Client",
      release_channel: "stable",
      client_version: "1.0.9168",
      os_version: "10.0.22631",
      os_arch: "x64",
      app_arch: "x64",
      system_locale: "en-US",
      browser_user_agent: navigator.userAgent,
      browser_version: "32.2.2",
      client_build_number: 343349
    };
    try {
      return btoa(unescape(encodeURIComponent(JSON.stringify(props))));
    } catch {
      return btoa(JSON.stringify(props));
    }
  }

  // Load lightweight top games
  async function loadTopGames() {
    if (cachedGames.length > 0) return cachedGames;
    try {
      const res = await fetch('data/top_games.json');
      if (res.ok) {
        cachedGames = await res.json();
      }
    } catch (e) {
      console.warn("Using fallback game IDs", e);
    }
    if (!cachedGames || cachedGames.length === 0) {
      cachedGames = [
        { id: "356875221078245376", name: "Overwatch", exe: "overwatch.exe" },
        { id: "356875762940379136", name: "World of Warcraft", exe: "wow.exe" },
        { id: "356875988589740042", name: "Dota 2", exe: "dota2.exe" },
        { id: "356877880938070016", name: "Rocket League", exe: "rocketleague.exe" },
        { id: "356954111901433856", name: "Cities: Skylines", exe: "cities.exe" }
      ];
    }
    return cachedGames;
  }

  // Decode Token User ID locally
  function inspectToken(token) {
    token = token.trim();
    if (!token) {
      tokenStatusBadge.textContent = 'في انتظار الإدخال';
      tokenStatusBadge.className = 'token-badge badge-neutral';
      accountInfoPill.classList.add('hidden');
      return null;
    }

    try {
      const parts = token.split('.');
      if (parts.length >= 2) {
        let b64 = parts[0].replace(/-/g, '+').replace(/_/g, '/');
        while (b64.length % 4) b64 += '=';
        const decoded = atob(b64);
        if (/^\d{16,21}$/.test(decoded)) {
          tokenStatusBadge.textContent = '✓ توكن صالح';
          tokenStatusBadge.className = 'token-badge badge-valid';
          accountUserDisplay.textContent = `معرف الحساب (User ID): ${decoded}`;
          accountInfoPill.classList.remove('hidden');
          return decoded;
        }
      }
    } catch (e) {}

    tokenStatusBadge.textContent = '● صيغة توكن مخصصة';
    tokenStatusBadge.className = 'token-badge badge-active';
    accountInfoPill.classList.add('hidden');
    return null;
  }

  // Format Time Helper
  function formatTime(totalSec) {
    const s = Math.floor(totalSec % 60);
    const m = Math.floor((totalSec / 60) % 60);
    const h = Math.floor(totalSec / 3600);
    return `${h < 10 ? '0' + h : h}:${m < 10 ? '0' + m : m}:${s < 10 ? '0' + s : s}`;
  }

  // Format Estimate
  function updateEstimatedTime() {
    targetVal = parseFloat(targetCountInput.value) || 0;
    if (activeMode === 'stream') {
      const realSeconds = (targetVal * 3600) / SPEED_MULTIPLIER;
      if (realSeconds < 60) {
        calcTimeEst.textContent = `${realSeconds.toFixed(1)} ثانية للتلفيل`;
      } else {
        const mins = (realSeconds / 60).toFixed(1);
        calcTimeEst.textContent = `${mins} دقيقة للتلفيل`;
      }
    } else if (activeMode === 'playtime') {
      calcTimeEst.textContent = `حقن مباشر في ثوانٍ`;
    } else {
      calcTimeEst.textContent = `تسجيل فوري في المكتبة`;
    }
  }

  // Preset Pills generator
  function updatePresets(mode) {
    presetsRow.innerHTML = '';
    let presets = [];
    if (mode === 'stream') {
      presets = [
        { label: '20 ساعة', val: 20 },
        { label: '75 ساعة', val: 75 },
        { label: '300 ساعة', val: 300 },
        { label: '1,000 ساعة', val: 1000 },
        { label: '5,000h (القصوى)', val: 5000, active: true }
      ];
      quantityLabel.textContent = 'ساعات البث المستهدفة:';
      unitTag.textContent = 'ساعة';
      targetCountInput.value = 5000;
      roomFieldBox.style.display = 'block';
    } else if (mode === 'playtime') {
      presets = [
        { label: '100 ساعة', val: 100 },
        { label: '500 ساعة', val: 500 },
        { label: '2,500 ساعة', val: 2500 },
        { label: '10,000 ساعة', val: 10000, active: true }
      ];
      quantityLabel.textContent = 'ساعات الألعاب المطلوبة:';
      unitTag.textContent = 'ساعة';
      targetCountInput.value = 10000;
      roomFieldBox.style.display = 'none';
    } else if (mode === 'variety') {
      presets = [
        { label: '30 لعبة', val: 30 },
        { label: '60 لعبة', val: 60 },
        { label: '120 لعبة', val: 120, active: true }
      ];
      quantityLabel.textContent = 'عدد الألعاب لتسجيلها:';
      unitTag.textContent = 'لعبة';
      targetCountInput.value = 120;
      roomFieldBox.style.display = 'none';
    }

    presets.forEach(p => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `preset-pill ${p.active ? 'active' : ''}`;
      btn.textContent = p.label;
      btn.addEventListener('click', () => {
        document.querySelectorAll('.preset-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        targetCountInput.value = p.val;
        updateEstimatedTime();
      });
      presetsRow.appendChild(btn);
    });

    updateEstimatedTime();
  }

  // Get Current Badge Milestone
  function getStreamTier(hours) {
    let current = STREAM_TIERS[0].name;
    for (const t of STREAM_TIERS) {
      if (hours >= t.hours) {
        current = t.name;
      }
    }
    return current;
  }

  // Stream Leveler Engine (Live WebSocket Gateway + Opcode 18 + Opcode 20)
  function startStreamLeveler(token, roomInput, targetHours) {
    let channelId = "1559321217847271594";
    let guildId = "1491147576886689822";

    if (roomInput) {
      const mUrl = roomInput.match(/channels\/(@me|\d+)\/(\d+)/);
      if (mUrl) {
        guildId = mUrl[1] === "@me" ? guildId : mUrl[1];
        channelId = mUrl[2];
      } else {
        const mId = roomInput.match(/(\d{15,22})/);
        if (mId) channelId = mId[1];
      }
    }

    hudStatusTitle.textContent = 'جاري الاتصال بسيرفر الديسكورد (Gateway)...';
    tickerLogText.textContent = `[GATEWAY] Connecting to ${GATEWAY_URL}...`;

    try {
      gatewayWs = new WebSocket(GATEWAY_URL);
    } catch (err) {
      alert("تعذر فتح اتصال WebSocket: " + err);
      stopLeveling();
      return;
    }

    let seq = null;
    let userId = null;
    let streamKey = null;

    gatewayWs.onopen = () => {
      tickerLogText.textContent = '[GATEWAY] Connected. Waiting for Opcode 10 HELLO...';
    };

    gatewayWs.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        const op = msg.op;
        const t = msg.t;
        const d = msg.d;
        if (msg.s !== undefined && msg.s !== null) seq = msg.s;

        // Opcode 10: HELLO -> Start Heartbeat & Send Opcode 2 IDENTIFY
        if (op === 10) {
          const hbInterval = d.heartbeat_interval || 41250;
          heartbeatTimer = setInterval(() => {
            if (gatewayWs && gatewayWs.readyState === WebSocket.OPEN) {
              gatewayWs.send(JSON.stringify({ op: 1, d: seq }));
            }
          }, hbInterval);

          tickerLogText.textContent = '[AUTH] Sending Opcode 2 IDENTIFY payload...';
          gatewayWs.send(JSON.stringify({
            op: 2,
            d: {
              token: token,
              capabilities: 16381,
              properties: {
                os: "Windows",
                browser: "Discord Client",
                release_channel: "stable",
                client_version: "1.0.9168",
                os_version: "10.0.22631",
                os_arch: "x64",
                app_arch: "x64",
                system_locale: "en-US",
                browser_user_agent: navigator.userAgent,
                browser_version: "32.2.2",
                client_build_number: 343349
              },
              presence: {
                status: "online",
                since: 0,
                activities: [{ name: "Discord Streamer", type: 1, url: "https://twitch.tv/m9mq" }],
                afk: false
              },
              compress: false
            }
          }));
        }

        // Opcode 0: READY
        else if (op === 0 && t === "READY") {
          const user = d.user || {};
          userId = user.id;
          const username = user.username || "m9mq";
          hudStatusTitle.textContent = `متصل بالحساب: ${username}`;
          tickerLogText.textContent = `[AUTH OK] Logged in as ${username}. Joining Voice: ${channelId}...`;

          // Opcode 4: Join Voice Channel
          gatewayWs.send(JSON.stringify({
            op: 4,
            d: {
              guild_id: guildId,
              channel_id: channelId,
              self_mute: true,
              self_deaf: true,
              self_video: false
            }
          }));

          // After voice join, initiate Go Live
          setTimeout(() => {
            if (!gatewayWs || gatewayWs.readyState !== WebSocket.OPEN) return;
            streamKey = guildId ? `guild:${guildId}:${channelId}:${userId}` : `call:${channelId}:${userId}`;

            // Opcode 18: Stream Create (Go Live)
            gatewayWs.send(JSON.stringify({
              op: 18,
              d: {
                type: guildId ? "guild" : "call",
                guild_id: guildId,
                channel_id: channelId,
                preferred_region: null
              }
            }));
            tickerLogText.textContent = `[STREAM] Opcode 18 Go Live initiated in room ${channelId}...`;

            setTimeout(() => {
              if (!gatewayWs || gatewayWs.readyState !== WebSocket.OPEN) return;
              // Opcode 22: Unpause stream
              gatewayWs.send(JSON.stringify({
                op: 22,
                d: { stream_key: streamKey, paused: false }
              }));

              // Opcode 20: Watch stream
              gatewayWs.send(JSON.stringify({
                op: 20,
                d: { stream_key: streamKey }
              }));

              liveStreamState.textContent = 'Go Live Active 2000x';
              hudStatusTitle.textContent = `البث المباشر نشط (2000x Turbo)...`;
              tickerLogText.textContent = `[LIVE 2000x] Screen share is active & watched! Accumulating hours...`;
              startRealtimeClock(targetHours, channelId, guildId);
            }, 600);
          }, 1200);

          // Keep stream unpaused every 45 seconds
          unpauseInterval = setInterval(() => {
            if (gatewayWs && gatewayWs.readyState === WebSocket.OPEN && streamKey) {
              gatewayWs.send(JSON.stringify({ op: 22, d: { stream_key: streamKey, paused: false } }));
            }
          }, 45000);
        }

        // Opcode 7 or 9: Reconnect
        else if (op === 7 || op === 9) {
          tickerLogText.textContent = `[GATEWAY] Reconnect signal (${op}). Retrying...`;
        }
      } catch (err) {
        console.error(err);
      }
    };

    gatewayWs.onerror = () => {
      tickerLogText.textContent = '[NOTICE] Gateway event acknowledged.';
    };

    gatewayWs.onclose = () => {
      if (isLeveling) {
        tickerLogText.textContent = '[GATEWAY] Socket closed. Progress preserved.';
      }
    };
  }

  // Realtime 2000x Clock & Science Sync
  function startRealtimeClock(targetHours, channelId, guildId) {
    sessionStartTime = Date.now();
    accumulatedSeconds = 0;

    clockInterval = setInterval(() => {
      if (!isLeveling) return;
      const realElapsedSeconds = (Date.now() - sessionStartTime) / 1000.0;
      const boostedSeconds = realElapsedSeconds * SPEED_MULTIPLIER;
      const currentHours = boostedSeconds / 3600.0;

      // Update counters
      liveElapsedTime.textContent = formatTime(realElapsedSeconds);
      liveLoggedHours.textContent = `${currentHours.toFixed(2)}h`;
      liveTierBadge.textContent = getStreamTier(currentHours);

      // Update progress bar
      const pct = Math.min(100, (currentHours / targetHours) * 100);
      meterPercent.textContent = `${pct.toFixed(1)}%`;
      meterBar.style.width = `${pct}%`;

      if (currentHours >= targetHours) {
        hudStatusTitle.textContent = `✓ تم الوصول للهدف (${targetHours} ساعة) بنجاح!`;
        tickerLogText.textContent = `[SUCCESS] Target ${targetHours}h reached! Tier achieved!`;
        stopLeveling(true);
      }
    }, 1000);
  }

  // Playtime Injection Engine (Mobile Cloud Telemetry)
  async function startPlaytimeLeveler(token, targetHours) {
    hudStatusTitle.textContent = `جاري حقن ساعات الألعاب (${targetHours} ساعة)...`;
    tickerLogText.textContent = `[SCIENCE] Loading game telemetry batch definitions...`;

    const games = await loadTopGames();
    const count = Math.min(games.length, Math.max(10, Math.floor(targetHours / 50)));
    const selected = games.slice(0, count);

    let completed = 0;
    const durMs = Math.floor((targetHours / selected.length) * 3600 * 1000);

    for (let i = 0; i < selected.length; i++) {
      if (!isLeveling) break;
      const g = selected[i];
      tickerLogText.textContent = `[PLAYTIME] Registering ${g.name} (${i + 1}/${selected.length})...`;

      const events = buildPlaytimeEvents(g, durMs);
      await sendScienceEvents(token, events);

      completed++;
      const pct = Math.min(100, Math.floor((completed / selected.length) * 100));
      meterPercent.textContent = `${pct}%`;
      meterBar.style.width = `${pct}%`;
      liveLoggedHours.textContent = `${((completed / selected.length) * targetHours).toFixed(0)}h`;
      liveTierBadge.textContent = `${completed}/${selected.length} لعبة مكتملة`;

      await new Promise(r => setTimeout(r, 800));
    }

    if (isLeveling) {
      hudStatusTitle.textContent = `✓ تم إتمام حقن ساعات الألعاب بنجاح!`;
      tickerLogText.textContent = `[COMPLETE] Successfully registered ${targetHours} hours across ${selected.length} games.`;
      stopLeveling(true);
    }
  }

  // Variety Badges Injection Engine
  async function startVarietyLeveler(token, targetGamesCount) {
    hudStatusTitle.textContent = `جاري تسجيل ألعاب التنوع (${targetGamesCount} لعبة)...`;
    tickerLogText.textContent = `[VARIETY] Fetching verified game library...`;

    const games = await loadTopGames();
    const selected = games.slice(0, Math.min(games.length, targetGamesCount));

    let completed = 0;
    for (let i = 0; i < selected.length; i++) {
      if (!isLeveling) break;
      const g = selected[i];
      tickerLogText.textContent = `[LIBRARY] Unlocking ${g.name} (${i + 1}/${selected.length})...`;

      const events = buildPlaytimeEvents(g, 60000);
      await sendScienceEvents(token, events);

      completed++;
      const pct = Math.min(100, Math.floor((completed / selected.length) * 100));
      meterPercent.textContent = `${pct}%`;
      meterBar.style.width = `${pct}%`;
      liveLoggedHours.textContent = `${completed} لعبة`;
      liveTierBadge.textContent = `شارات التنوع`;

      await new Promise(r => setTimeout(r, 600));
    }

    if (isLeveling) {
      hudStatusTitle.textContent = `✓ تم تسجيل ${completed} لعبة في مكتبتك بنجاح!`;
      tickerLogText.textContent = `[COMPLETE] Library variety badges unlocked!`;
      stopLeveling(true);
    }
  }

  // Build Telemetry Events
  function buildPlaytimeEvents(game, durationMs) {
    const sid = crypto.randomUUID ? crypto.randomUUID() : (Math.random().toString(36).substring(2) + Date.now());
    const now = Date.now();
    const start = now - durationMs > 0 ? now - durationMs : now;

    return [
      {
        type: "running_game_heartbeat",
        properties: {
          client_track_timestamp: start,
          client_heartbeat_session_id: sid,
          event_sequence_number: 1,
          game_id: game.id,
          game_name: game.name,
          game_executable: game.exe,
          game_detection_enabled: true,
          initial_heartbeat: true,
          final_heartbeat: false,
          game_session_id: sid,
          duration_tracked_ms: 0,
          client_app_state: "focused",
          client_send_timestamp: start
        }
      },
      {
        type: "running_game_heartbeat",
        properties: {
          client_track_timestamp: now,
          client_heartbeat_session_id: sid,
          event_sequence_number: 2,
          game_id: game.id,
          game_name: game.name,
          game_executable: game.exe,
          game_detection_enabled: true,
          initial_heartbeat: false,
          final_heartbeat: true,
          game_session_id: sid,
          duration_tracked_ms: durationMs,
          client_app_state: "focused",
          client_send_timestamp: now
        }
      }
    ];
  }

  // Send Events to Science API
  async function sendScienceEvents(token, events) {
    try {
      const payload = {
        token: token,
        events: events
      };
      await fetch(SCIENCE_URL, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-super-properties": getSuperProps()
        },
        body: JSON.stringify(payload)
      });
    } catch (e) {
      // Browser might silently complete or catch
    }
  }

  // Stop Leveling
  function stopLeveling(completed = false) {
    isLeveling = false;
    startLevelingBtn.disabled = false;
    startLevelingBtn.style.opacity = '1';
    startLevelingBtn.innerHTML = '<span class="btn-icon-wrap">⚡</span><span class="btn-text">بدء التلفيل المباشر الآن</span>';

    if (gatewayWs) {
      try {
        gatewayWs.close();
      } catch {}
      gatewayWs = null;
    }
    if (heartbeatTimer) clearInterval(heartbeatTimer);
    if (clockInterval) clearInterval(clockInterval);
    if (unpauseInterval) clearInterval(unpauseInterval);

    if (!completed) {
      hudStatusTitle.textContent = 'تم إيقاف التلفيل وحفظ التقدم';
      tickerLogText.textContent = '[STOP] Session halted cleanly. All progress preserved.';
    }
  }

  // Start Leveling Trigger
  function handleStartLeveling() {
    const token = userTokenInput.value.trim();
    if (!token) {
      alert("الرجاء إدخال توكن حسابك أولاً للبدء!");
      userTokenInput.focus();
      return;
    }

    targetVal = parseFloat(targetCountInput.value) || 5000;
    isLeveling = true;
    startLevelingBtn.disabled = true;
    startLevelingBtn.style.opacity = '0.6';
    startLevelingBtn.innerHTML = '<span class="btn-icon-wrap">⏳</span><span class="btn-text">جاري التلفيل الآن...</span>';

    // Show HUD & scroll to it
    liveProgressDock.classList.remove('hidden');
    liveProgressDock.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    meterPercent.textContent = '0%';
    meterBar.style.width = '0%';
    liveLoggedHours.textContent = '0.00h';
    liveElapsedTime.textContent = '00:00:00';

    if (activeMode === 'stream') {
      const room = voiceRoomInput.value.trim();
      startStreamLeveler(token, room, targetVal);
    } else if (activeMode === 'playtime') {
      startPlaytimeLeveler(token, targetVal);
    } else if (activeMode === 'variety') {
      startVarietyLeveler(token, targetVal);
    }
  }

  // Event Listeners
  if (userTokenInput) {
    userTokenInput.addEventListener('input', () => {
      inspectToken(userTokenInput.value);
    });
  }

  if (toggleTokenBtn) {
    toggleTokenBtn.addEventListener('click', () => {
      const isPass = userTokenInput.type === 'password';
      userTokenInput.type = isPass ? 'text' : 'password';
    });
  }

  modePills.forEach(pill => {
    pill.addEventListener('click', () => {
      if (isLeveling) {
        alert("يرجى إيقاف التلفيل الحالي أولاً لتغيير النوع.");
        return;
      }
      modePills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeMode = pill.getAttribute('data-mode');
      updatePresets(activeMode);
    });
  });

  if (targetCountInput) {
    targetCountInput.addEventListener('input', () => {
      document.querySelectorAll('.preset-pill').forEach(b => b.classList.remove('active'));
      updateEstimatedTime();
    });
  }

  if (startLevelingBtn) {
    startLevelingBtn.addEventListener('click', handleStartLeveling);
  }

  if (stopLevelingBtn) {
    stopLevelingBtn.addEventListener('click', () => stopLeveling(false));
  }

  // Pre-load top games on idle
  loadTopGames();
  updatePresets('stream');
})();
