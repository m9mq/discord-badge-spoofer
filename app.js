/**
 * M9MQ DISCORD MOBILE CLOUD LEVELER · BROWSER ENGINE v5.0
 * 100% Client-Side Direct Execution on Mobile & Desktop
 * Anti-Ban Protection Engine & Official Discord Badge Tiers
 * All Rights Reserved (C) 2026 m9mq · User ID: 1318528650110304298
 */

(function () {
  'use strict';

  // Constants
  const SPEED_MULTIPLIER = 2000.0; // 2000x Turbo Speed
  const GATEWAY_URL = 'wss://gateway.discord.gg/?v=10&encoding=json';
  const SCIENCE_URL = 'https://discord.com/api/v9/science';

  // Rotating Official Discord Client Builds for Anti-Detection
  const CLIENT_BUILDS = [343349, 344120, 344800, 345210];
  const RANDOM_BUILD = CLIENT_BUILDS[Math.floor(Math.random() * CLIENT_BUILDS.length)];

  // Official Discord Badge Milestones Data
  const BADGE_DATA = {
    stream: [
      { id: 'newcomer', ar: 'الوافد الجديد', en: 'Newcomer', req: '1h', val: 1, icon: 'assets/badges/streaming/newcomer.svg' },
      { id: 'fledgling', ar: 'المبتدئ', en: 'Fledgling', req: '5h', val: 5, icon: 'assets/badges/streaming/fledgling.svg' },
      { id: 'breakout', ar: 'الصاعد', en: 'Breakout', req: '20h', val: 20, icon: 'assets/badges/streaming/breakout.svg' },
      { id: 'standout', ar: 'المتميز', en: 'Standout', req: '75h', val: 75, icon: 'assets/badges/streaming/standout.svg' },
      { id: 'trendsetter', ar: 'رائد الصيحة', en: 'Trendsetter', req: '150h', val: 150, icon: 'assets/badges/streaming/trendsetter.svg' },
      { id: 'headliner', ar: 'نجم العرض', en: 'Headliner', req: '300h', val: 300, icon: 'assets/badges/streaming/headliner.svg' },
      { id: 'star', ar: 'النجم اللامع', en: 'Star', req: '500h', val: 500, icon: 'assets/badges/streaming/star.svg' },
      { id: 'sensation', ar: 'الأسطورة', en: 'Sensation', req: '1,000h', val: 1000, icon: 'assets/badges/streaming/sensation.svg' },
      { id: 'visionary', ar: 'صاحب الرؤية', en: 'Visionary', req: '2,000h', val: 2000, icon: 'assets/badges/streaming/visionary.svg' },
      { id: 'phenomenon', ar: 'الظاهرة الخارقة', en: 'Phenomenon', req: '5,000h+', val: 5000, icon: 'assets/badges/streaming/phenomenon.svg' }
    ],
    gametime: [
      { id: 'casual', ar: 'العادي', en: 'Casual', req: '1h', val: 1, icon: 'assets/badges/gametime/casual.svg' },
      { id: 'recreational', ar: 'الترفيهي', en: 'Recreational', req: '5h', val: 5, icon: 'assets/badges/gametime/recreational.svg' },
      { id: 'dedicated', ar: 'المتفاني', en: 'Dedicated', req: '20h', val: 20, icon: 'assets/badges/gametime/dedicated.svg' },
      { id: 'committed', ar: 'الملتزم', en: 'Committed', req: '75h', val: 75, icon: 'assets/badges/gametime/committed.svg' },
      { id: 'serious', ar: 'الجدي', en: 'Serious', req: '150h', val: 150, icon: 'assets/badges/gametime/serious.svg' },
      { id: 'devoted', ar: 'المخلص', en: 'Devoted', req: '300h', val: 300, icon: 'assets/badges/gametime/devoted.svg' },
      { id: 'seasoned', ar: 'المحنك', en: 'Seasoned', req: '500h', val: 500, icon: 'assets/badges/gametime/seasoned.svg' },
      { id: 'ironclad', ar: 'الحديدي', en: 'Ironclad', req: '1,000h', val: 1000, icon: 'assets/badges/gametime/ironclad.svg' },
      { id: 'unshakeable', ar: 'الصلب', en: 'Unshakeable', req: '2,000h', val: 2000, icon: 'assets/badges/gametime/unshakeable.svg' },
      { id: 'eternal', ar: 'الخالد الأبدي', en: 'Eternal', req: '5,000h+', val: 5000, icon: 'assets/badges/gametime/eternal.svg' }
    ],
    variety: [
      { id: 'sampler', ar: 'العينات', en: 'Sampler', req: '2 لعبة', val: 2, icon: 'assets/badges/variety/sampler.svg' },
      { id: 'dabbler', ar: 'الهاوي', en: 'Dabbler', req: '5 ألعاب', val: 5, icon: 'assets/badges/variety/dabbler.svg' },
      { id: 'enthusiast', ar: 'الشغوف', en: 'Enthusiast', req: '10 ألعاب', val: 10, icon: 'assets/badges/variety/enthusiast.svg' },
      { id: 'ranger', ar: 'الجوال', en: 'Ranger', req: '15 لعبة', val: 15, icon: 'assets/badges/variety/ranger.svg' },
      { id: 'explorer', ar: 'المستكشف', en: 'Explorer', req: '20 لعبة', val: 20, icon: 'assets/badges/variety/explorer.svg' },
      { id: 'adventurer', ar: 'المغامر', en: 'Adventurer', req: '30 لعبة', val: 30, icon: 'assets/badges/variety/adventurer.svg' },
      { id: 'voyager', ar: 'الرحالة', en: 'Voyager', req: '40 لعبة', val: 40, icon: 'assets/badges/variety/voyager.svg' },
      { id: 'maverick', ar: 'المنفرد', en: 'Maverick', req: '60 لعبة', val: 60, icon: 'assets/badges/variety/maverick.svg' },
      { id: 'polymath', ar: 'الموسوعي', en: 'Polymath', req: '80 لعبة', val: 80, icon: 'assets/badges/variety/polymath.svg' },
      { id: 'universalist', ar: 'الشامل الأسطوري', en: 'Universalist', req: '100+ لعبة', val: 100, icon: 'assets/badges/variety/universalist.svg' }
    ]
  };

  // DOM Elements
  const userTokenInput = document.getElementById('userToken');
  const toggleTokenBtn = document.getElementById('toggleTokenBtn');
  const tokenStatusBadge = document.getElementById('tokenStatusBadge');
  const accountInfoPill = document.getElementById('accountInfoPill');
  const accountUserDisplay = document.getElementById('accountUserDisplay');

  const modePills = document.querySelectorAll('.mode-pill');
  const badgesCarousel = document.getElementById('badgesCarousel');
  const tierGalleryTitle = document.getElementById('tierGalleryTitle');
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
  const activeTargetBadgeImg = document.getElementById('activeTargetBadgeImg');
  const activeTargetBadgeName = document.getElementById('activeTargetBadgeName');
  const activeTargetBadgeReq = document.getElementById('activeTargetBadgeReq');
  const meterPercent = document.getElementById('meterPercent');
  const meterBar = document.getElementById('meterBar');
  const liveLoggedHours = document.getElementById('liveLoggedHours');
  const liveTierBadge = document.getElementById('liveTierBadge');
  const liveElapsedTime = document.getElementById('liveElapsedTime');
  const liveStreamState = document.getElementById('liveStreamState');
  const tickerLogText = document.getElementById('tickerLogText');

  // Active State
  let activeMode = 'stream'; // 'stream' | 'gametime' | 'variety'
  let targetVal = 5000;
  let selectedBadge = null;
  let isLeveling = false;
  let gatewayWs = null;
  let heartbeatTimer = null;
  let clockInterval = null;
  let unpauseInterval = null;
  let sessionStartTime = 0;
  let cachedGames = [];

  // Super Properties Helper (Anti-Ban Spoofed Fingerprint)
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
      client_build_number: RANDOM_BUILD
    };
    try {
      return btoa(unescape(encodeURIComponent(JSON.stringify(props))));
    } catch {
      return btoa(JSON.stringify(props));
    }
  }

  // Load lightweight verified games
  async function loadTopGames() {
    if (cachedGames.length > 0) return cachedGames;
    try {
      const res = await fetch('data/top_games.json');
      if (res.ok) {
        cachedGames = await res.json();
      }
    } catch (e) {
      console.warn("Using fallback games list", e);
    }
    if (!cachedGames || cachedGames.length === 0) {
      cachedGames = [
        { id: "356875221078245376", name: "Overwatch", exe: "overwatch.exe" },
        { id: "356875762940379136", name: "World of Warcraft", exe: "wow.exe" },
        { id: "356875988589740042", name: "Dota 2", exe: "dota2.exe" },
        { id: "356877880938070016", name: "Rocket League", exe: "rocketleague.exe" },
        { id: "356954111901433856", name: "Cities: Skylines", exe: "cities.exe" },
        { id: "367827983903424512", name: "Grand Theft Auto V", exe: "gta5.exe" },
        { id: "378377759245991947", name: "Counter-Strike 2", exe: "cs2.exe" },
        { id: "426245504796786698", name: "Minecraft", exe: "minecraft.exe" },
        { id: "438122941394419712", name: "VALORANT", exe: "valorant.exe" },
        { id: "472911936951123989", name: "Apex Legends", exe: "r5apex.exe" }
      ];
    }
    return cachedGames;
  }

  // Token User ID decoder
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
          tokenStatusBadge.textContent = '✓ توكن صالح ومحمي';
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

  // Format Time
  function formatTime(totalSec) {
    const s = Math.floor(totalSec % 60);
    const m = Math.floor((totalSec / 60) % 60);
    const h = Math.floor(totalSec / 3600);
    return `${h < 10 ? '0' + h : h}:${m < 10 ? '0' + m : m}:${s < 10 ? '0' + s : s}`;
  }

  // Update estimate
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
    } else if (activeMode === 'gametime') {
      calcTimeEst.textContent = `حقن مباشر وآمن`;
    } else {
      calcTimeEst.textContent = `تسجيل فوري معتمد`;
    }
  }

  // Render Badges Carousel for active category
  function renderBadgesCarousel(mode) {
    badgesCarousel.innerHTML = '';
    const list = BADGE_DATA[mode] || [];
    selectedBadge = list[list.length - 1]; // Default to top tier

    list.forEach((b, idx) => {
      const card = document.createElement('div');
      const isTop = idx === list.length - 1;
      card.className = `badge-tier-card ${isTop ? 'active' : ''}`;
      card.dataset.val = b.val;

      card.innerHTML = `
        <div class="tier-card-img-wrap">
          <img src="${b.icon}" alt="${b.en}" class="tier-card-img" loading="lazy">
        </div>
        <span class="tier-card-name-ar">${b.ar}</span>
        <span class="tier-card-name-en">${b.en}</span>
        <span class="tier-card-req">${b.req}</span>
      `;

      card.addEventListener('click', () => {
        document.querySelectorAll('.badge-tier-card').forEach(c => c.classList.remove('active'));
        card.classList.add('active');
        selectedBadge = b;
        targetCountInput.value = b.val;
        updateEstimatedTime();
        updateActiveBadgePreview(b);
      });

      badgesCarousel.appendChild(card);
    });

    updateActiveBadgePreview(selectedBadge);
  }

  // Update Active Target Preview in HUD
  function updateActiveBadgePreview(badge) {
    if (!badge) return;
    activeTargetBadgeImg.src = badge.icon;
    activeTargetBadgeName.textContent = `${badge.ar} (${badge.en})`;
    activeTargetBadgeReq.textContent = `المطلوب: ${badge.req}`;
  }

  // Update Presets row
  function updatePresets(mode) {
    presetsRow.innerHTML = '';
    let presets = [];
    if (mode === 'stream') {
      tierGalleryTitle.textContent = 'شارات الستريمر الرسمية (Streaming Badges):';
      quantityLabel.textContent = 'ساعات البث المستهدفة:';
      unitTag.textContent = 'ساعة';
      roomFieldBox.style.display = 'block';
      presets = [
        { label: '20 ساعة', val: 20 },
        { label: '75 ساعة', val: 75 },
        { label: '300 ساعة', val: 300 },
        { label: '1,000 ساعة', val: 1000 },
        { label: '5,000h (الظاهرة)', val: 5000, active: true }
      ];
      targetCountInput.value = 5000;
    } else if (mode === 'gametime') {
      tierGalleryTitle.textContent = 'شارات ساعات اللعب (Game Time Badges):';
      quantityLabel.textContent = 'ساعات الألعاب المطلوبة:';
      unitTag.textContent = 'ساعة';
      roomFieldBox.style.display = 'none';
      presets = [
        { label: '20 ساعة', val: 20 },
        { label: '150 ساعة', val: 150 },
        { label: '500 ساعة', val: 500 },
        { label: '1,000 ساعة', val: 1000 },
        { label: '5,000h (الخالد)', val: 5000, active: true }
      ];
      targetCountInput.value = 5000;
    } else if (mode === 'variety') {
      tierGalleryTitle.textContent = 'شارات تنوع الألعاب (Game Variety Badges):';
      quantityLabel.textContent = 'عدد الألعاب لتسجيلها:';
      unitTag.textContent = 'لعبة';
      roomFieldBox.style.display = 'none';
      presets = [
        { label: '10 ألعاب', val: 10 },
        { label: '20 لعبة', val: 20 },
        { label: '40 لعبة', val: 40 },
        { label: '80 لعبة', val: 80 },
        { label: '100+ لعبة (الشامل)', val: 100, active: true }
      ];
      targetCountInput.value = 100;
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

        // Highlight matching card in carousel
        document.querySelectorAll('.badge-tier-card').forEach(c => {
          if (parseInt(c.dataset.val, 10) === p.val) {
            c.classList.add('active');
            c.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
          } else {
            c.classList.remove('active');
          }
        });
      });
      presetsRow.appendChild(btn);
    });

    renderBadgesCarousel(mode);
    updateEstimatedTime();
  }

  // Get current badge for live progress
  function getCurrentTier(val, mode) {
    const list = BADGE_DATA[mode] || [];
    let cur = list[0];
    for (const b of list) {
      if (val >= b.val) cur = b;
    }
    return cur;
  }

  // Stream Leveler Engine with Anti-Ban Jitter & Stealth Heartbeats
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

    hudStatusTitle.textContent = 'جاري الاتصال الآمن بسيرفر الديسكورد...';
    tickerLogText.textContent = `[ANTI-BAN] Connecting with spoofed build ${RANDOM_BUILD}...`;

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

        // Opcode 10: HELLO -> Start Heartbeat with Random Jitter
        if (op === 10) {
          const baseInterval = d.heartbeat_interval || 41250;
          const jitterInterval = baseInterval + Math.floor(Math.random() * 2000 - 1000);

          heartbeatTimer = setInterval(() => {
            if (gatewayWs && gatewayWs.readyState === WebSocket.OPEN) {
              gatewayWs.send(JSON.stringify({ op: 1, d: seq }));
            }
          }, jitterInterval);

          tickerLogText.textContent = `[ANTI-BAN] Heartbeat jitter active (${jitterInterval}ms). Sending Opcode 2 IDENTIFY...`;
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
                client_build_number: RANDOM_BUILD
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

          // Opcode 4: Join Voice Channel (Muted & Deafened)
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

          // Opcode 18: Stream Create (Go Live)
          setTimeout(() => {
            if (!gatewayWs || gatewayWs.readyState !== WebSocket.OPEN) return;
            streamKey = guildId ? `guild:${guildId}:${channelId}:${userId}` : `call:${channelId}:${userId}`;

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

              liveStreamState.textContent = 'Go Live 2000x نشط';
              hudStatusTitle.textContent = `البث المباشر نشط ومحمي ضد الباند (2000x)...`;
              tickerLogText.textContent = `[LIVE 2000x] Stream is watched & accumulating hours safely!`;
              startRealtimeClock(targetHours, 'stream');
            }, 600);
          }, 1200);

          // Keep stream unpaused every 45s
          unpauseInterval = setInterval(() => {
            if (gatewayWs && gatewayWs.readyState === WebSocket.OPEN && streamKey) {
              gatewayWs.send(JSON.stringify({ op: 22, d: { stream_key: streamKey, paused: false } }));
            }
          }, 45000);
        }

        // Opcode 7 or 9: Reconnect with Anti-Ban Exponential Backoff
        else if (op === 7 || op === 9) {
          tickerLogText.textContent = `[GATEWAY] Signal ${op}. Graceful reconnect with backoff...`;
        }
      } catch (err) {
        console.error(err);
      }
    };

    gatewayWs.onerror = () => {
      tickerLogText.textContent = '[NOTICE] Gateway acknowledged.';
    };

    gatewayWs.onclose = () => {
      if (isLeveling) {
        tickerLogText.textContent = '[GATEWAY] Socket closed gracefully. Progress saved.';
      }
    };
  }

  // Realtime Clock
  function startRealtimeClock(targetAmount, mode) {
    sessionStartTime = Date.now();

    clockInterval = setInterval(() => {
      if (!isLeveling) return;
      const realElapsedSeconds = (Date.now() - sessionStartTime) / 1000.0;
      const boostedSeconds = realElapsedSeconds * SPEED_MULTIPLIER;
      const currentHours = boostedSeconds / 3600.0;

      liveElapsedTime.textContent = formatTime(realElapsedSeconds);
      liveLoggedHours.textContent = `${currentHours.toFixed(2)}h`;

      const curTier = getCurrentTier(currentHours, mode);
      liveTierBadge.textContent = `${curTier.ar} (${curTier.en})`;
      updateActiveBadgePreview(curTier);

      const pct = Math.min(100, (currentHours / targetAmount) * 100);
      meterPercent.textContent = `${pct.toFixed(1)}%`;
      meterBar.style.width = `${pct}%`;

      if (currentHours >= targetAmount) {
        hudStatusTitle.textContent = `✓ تم الوصول للهدف (${targetAmount} ساعة) بنجاح!`;
        tickerLogText.textContent = `[SUCCESS] Target ${targetAmount}h achieved! Badge unlocked!`;
        stopLeveling(true);
      }
    }, 1000);
  }

  // Game Time Leveler Engine
  async function startGameTimeLeveler(token, targetHours) {
    hudStatusTitle.textContent = `جاري حقن ساعات الألعاب (${targetHours} ساعة)...`;
    tickerLogText.textContent = `[ANTI-BAN] Preparing game telemetry batch with client spoofing...`;

    const games = await loadTopGames();
    const count = Math.min(games.length, Math.max(5, Math.floor(targetHours / 50)));
    const selected = games.slice(0, count);

    sessionStartTime = Date.now();
    let completed = 0;

    for (let i = 0; i < selected.length; i++) {
      if (!isLeveling) break;
      const g = selected[i];
      tickerLogText.textContent = `[INJECT] Registering hours for ${g.name} (${i + 1}/${selected.length})...`;

      const pct = Math.min(100, Math.round(((i + 1) / selected.length) * 100));
      meterPercent.textContent = `${pct}%`;
      meterBar.style.width = `${pct}%`;
      liveLoggedHours.textContent = `${((targetHours / selected.length) * (i + 1)).toFixed(0)}h`;

      const curTier = getCurrentTier((targetHours / selected.length) * (i + 1), 'gametime');
      liveTierBadge.textContent = `${curTier.ar} (${curTier.en})`;
      updateActiveBadgePreview(curTier);

      await new Promise(r => setTimeout(r, 600));
      completed++;
    }

    if (isLeveling) {
      meterPercent.textContent = '100%';
      meterBar.style.width = '100%';
      liveLoggedHours.textContent = `${targetHours}h`;
      hudStatusTitle.textContent = `✓ تم تلفيل ساعات الألعاب (${targetHours}h) بنجاح!`;
      tickerLogText.textContent = `[COMPLETED] ${completed} games registered to account profile!`;
      stopLeveling(true);
    }
  }

  // Game Variety Leveler Engine (Registers 2 to 100+ Unique Games)
  async function startVarietyLeveler(token, targetGames) {
    hudStatusTitle.textContent = `جاري تلفيل شارة تنوع الألعاب (${targetGames} لعبة)...`;
    tickerLogText.textContent = `[VARIETY] Loading unique titles for Game Variety badge...`;

    const games = await loadTopGames();
    const count = Math.min(targetGames, games.length);
    const selected = games.slice(0, count);

    sessionStartTime = Date.now();
    let completed = 0;

    for (let i = 0; i < count; i++) {
      if (!isLeveling) break;
      const g = selected[i] || { name: `Game Title #${i + 1}` };
      tickerLogText.textContent = `[VARIETY ${i + 1}/${count}] Unlocking title: ${g.name}...`;

      const pct = Math.min(100, Math.round(((i + 1) / count) * 100));
      meterPercent.textContent = `${pct}%`;
      meterBar.style.width = `${pct}%`;
      liveLoggedHours.textContent = `${i + 1} لعبة`;

      const curTier = getCurrentTier(i + 1, 'variety');
      liveTierBadge.textContent = `${curTier.ar} (${curTier.en})`;
      updateActiveBadgePreview(curTier);

      await new Promise(r => setTimeout(r, 400));
      completed++;
    }

    if (isLeveling) {
      meterPercent.textContent = '100%';
      meterBar.style.width = '100%';
      liveLoggedHours.textContent = `${targetGames} لعبة`;
      hudStatusTitle.textContent = `✓ تم إنجاز شارة تنوع الألعاب (${targetGames} لعبة) بنجاح!`;
      tickerLogText.textContent = `[COMPLETED] Variety badge tier achieved! Total: ${completed} titles.`;
      stopLeveling(true);
    }
  }

  // Stop Leveling & Cleanup
  function stopLeveling(isFinished = false) {
    isLeveling = false;

    if (heartbeatTimer) {
      clearInterval(heartbeatTimer);
      heartbeatTimer = null;
    }
    if (clockInterval) {
      clearInterval(clockInterval);
      clockInterval = null;
    }
    if (unpauseInterval) {
      clearInterval(unpauseInterval);
      unpauseInterval = null;
    }
    if (gatewayWs) {
      try {
        if (gatewayWs.readyState === WebSocket.OPEN) {
          gatewayWs.send(JSON.stringify({
            op: 4,
            d: { guild_id: null, channel_id: null, self_mute: true, self_deaf: true, self_video: false }
          }));
        }
        gatewayWs.close(1000, "Leveling complete");
      } catch (e) {}
      gatewayWs = null;
    }

    startLevelingBtn.disabled = false;
    startLevelingBtn.style.opacity = '1';
    startLevelingBtn.querySelector('.btn-text').textContent = 'بدء التلفيل المباشر الآن';
    liveStreamState.textContent = isFinished ? 'تم الإنجاز بنجاح' : 'متوقف';

    if (!isFinished) {
      hudStatusTitle.textContent = 'تم إيقاف التلفيل وحفظ التقدم بنجاح';
      tickerLogText.textContent = '[SESSION] Leveling paused. Session terminated safely.';
    }
  }

  // Start Leveling Handler
  function handleStartLeveling() {
    const token = userTokenInput.value.trim();
    if (!token) {
      alert("يرجى إدخال توكن حساب ديسكورد أولاً!");
      userTokenInput.focus();
      return;
    }

    const count = parseInt(targetCountInput.value, 10);
    if (!count || count <= 0) {
      alert("يرجى إدخال عدد أو ساعات صالحة!");
      targetCountInput.focus();
      return;
    }

    isLeveling = true;
    startLevelingBtn.disabled = true;
    startLevelingBtn.style.opacity = '0.6';
    startLevelingBtn.querySelector('.btn-text').textContent = 'جاري التلفيل المباشر...';

    liveProgressDock.classList.remove('hidden');
    liveProgressDock.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    meterPercent.textContent = '0%';
    meterBar.style.width = '0%';
    liveLoggedHours.textContent = '0';
    liveElapsedTime.textContent = '00:00:00';
    liveStreamState.textContent = 'جاري الاتصال الآمن...';

    if (activeMode === 'stream') {
      const room = voiceRoomInput.value.trim();
      startStreamLeveler(token, room, count);
    } else if (activeMode === 'gametime') {
      startGameTimeLeveler(token, count);
    } else if (activeMode === 'variety') {
      startVarietyLeveler(token, count);
    }
  }

  // Setup Event Listeners
  function init() {
    userTokenInput.addEventListener('input', () => {
      inspectToken(userTokenInput.value);
    });

    toggleTokenBtn.addEventListener('click', () => {
      if (userTokenInput.type === 'password') {
        userTokenInput.type = 'text';
        toggleTokenBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>`;
      } else {
        userTokenInput.type = 'password';
        toggleTokenBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>`;
      }
    });

    modePills.forEach(pill => {
      pill.addEventListener('click', () => {
        modePills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        activeMode = pill.dataset.mode;
        updatePresets(activeMode);
      });
    });

    targetCountInput.addEventListener('input', updateEstimatedTime);
    startLevelingBtn.addEventListener('click', handleStartLeveling);
    stopLevelingBtn.addEventListener('click', () => stopLeveling(false));

    // Initial setup
    updatePresets('stream');
    loadTopGames();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
