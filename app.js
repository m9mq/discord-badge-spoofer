/**
 * M9MQ DISCORD BADGE SPOOFER & 2000x STREAM BOOSTER · OFFICIAL APP LOGIC
 * All Rights Reserved (C) 2026 m9mq
 * Zero Tracking · 100% Client-Side Secure Execution
 */

(function () {
  'use strict';

  // Badge Tiers Data
  const STREAM_TIERS = [
    { tier: 1, hours: 1, name: "Tier 1: Newcomer (1 hour)" },
    { tier: 2, hours: 5, name: "Tier 2: Fledgling (5 hours)" },
    { tier: 3, hours: 20, name: "Tier 3: Breakout (20 hours)" },
    { tier: 4, hours: 75, name: "Tier 4: Standout (75 hours)" },
    { tier: 5, hours: 150, name: "Tier 5: Trendsetter (150 hours)" },
    { tier: 6, hours: 300, name: "Tier 6: Headliner (300 hours)" },
    { tier: 7, hours: 500, name: "Tier 7: Star (500 hours)" },
    { tier: 8, hours: 1000, name: "Tier 8: Sensation (1,000 hours)" },
    { tier: 9, hours: 2000, name: "Tier 9: Visionary (2,000 hours)" },
    { tier: 10, hours: 5000, name: "Tier 10: Phenomenon (5,000+ hours)" }
  ];

  const SPEED_MULTIPLIER = 2000.0; // 2000x Turbo Speed

  // DOM Elements - Calculator
  const currentHoursInput = document.getElementById('currentHoursInput');
  const currentHoursSlider = document.getElementById('currentHoursSlider');
  const nextTierName = document.getElementById('nextTierName');
  const nextTierTimeRemaining = document.getElementById('nextTierTimeRemaining');
  const maxTierTimeRemaining = document.getElementById('maxTierTimeRemaining');
  const progressFill = document.getElementById('progressFill');
  const progressPct = document.getElementById('progressPct');
  const tierCards = document.querySelectorAll('.tier-card');

  // DOM Elements - Terminal Simulator
  const terminalOutput = document.getElementById('terminalOutput');
  const simHours = document.getElementById('simHours');
  const termStartBtn = document.getElementById('termStartBtn');
  const termPauseBtn = document.getElementById('termPauseBtn');
  const termClearBtn = document.getElementById('termClearBtn');

  // DOM Elements - Config Generator
  const cfgToken = document.getElementById('cfgToken');
  const cfgRoom = document.getElementById('cfgRoom');
  const cfgViewer = document.getElementById('cfgViewer');
  const configCodePreview = document.getElementById('configCodePreview');
  const btnGenerateConfig = document.getElementById('btnGenerateConfig');
  const btnDownloadConfig = document.getElementById('btnDownloadConfig');
  const btnCopyCommand = document.getElementById('btnCopyCommand');
  const modeRadios = document.querySelectorAll('input[name="cfgMode"]');

  // DOM Elements - Language
  const langToggle = document.getElementById('langToggle');
  const langText = document.getElementById('langText');
  let currentLang = 'ar';

  // Format real-time duration
  function formatRealDuration(seconds) {
    if (seconds <= 0) return 'مكتمل بالفعل!';
    if (seconds < 60) return `${seconds.toFixed(1)} ثانية واقعية`;
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    if (mins < 60) {
      return `${mins} دقيقة ${secs > 0 ? `و ${secs} ثانية` : ''}`;
    }
    const hrs = Math.floor(mins / 60);
    const remMins = mins % 60;
    return `${hrs} ساعة ${remMins > 0 ? `و ${remMins} دقيقة` : ''}`;
  }

  // Update Badge Calculator
  function updateCalculator() {
    const hours = parseFloat(currentHoursInput.value) || 0;
    currentHoursSlider.value = Math.min(hours, 5000);

    // Find next tier
    let nextTier = null;
    for (const t of STREAM_TIERS) {
      if (hours < t.hours) {
        nextTier = t;
        break;
      }
    }

    if (nextTier) {
      const remainingHours = nextTier.hours - hours;
      const realSeconds = (remainingHours * 3600) / SPEED_MULTIPLIER;
      nextTierName.textContent = nextTier.name;
      nextTierTimeRemaining.textContent = `الوقت المطلوب مع التيربو 2000x: ${formatRealDuration(realSeconds)}`;
    } else {
      nextTierName.textContent = 'Tier 10: Phenomenon (تم الوصول لأعلى مستوى!)';
      nextTierTimeRemaining.textContent = 'تهانينا! حققت الحد الأقصى لشارات البث على ديسكورد.';
    }

    // Time to max tier (5000h)
    const maxRemHours = Math.max(0, 5000 - hours);
    const maxRealSeconds = (maxRemHours * 3600) / SPEED_MULTIPLIER;
    maxTierTimeRemaining.textContent = maxRemHours > 0 ? formatRealDuration(maxRealSeconds) : 'مكتمل (5,000+ ساعة)';

    // Progress bar
    const pct = Math.min(100, (hours / 5000) * 100);
    progressFill.style.width = `${pct}%`;
    progressPct.textContent = `${pct.toFixed(2)}%`;

    // Highlight tier cards
    tierCards.forEach(card => {
      const cardHours = parseFloat(card.getAttribute('data-hours'));
      if (hours >= cardHours) {
        card.classList.add('active-tier');
        const st = card.querySelector('.tier-status');
        if (st && !st.classList.contains('epic-status')) {
          st.textContent = '✓ مكتمل';
          st.style.color = '#ffffff';
          st.style.borderColor = '#ffffff';
        }
      } else {
        card.classList.remove('active-tier');
        const st = card.querySelector('.tier-status');
        if (st && !st.classList.contains('epic-status')) {
          st.textContent = 'جاهز';
          st.style.color = '';
          st.style.borderColor = '';
        }
      }
    });
  }

  // Event Listeners for Calculator
  if (currentHoursInput && currentHoursSlider) {
    currentHoursInput.addEventListener('input', () => {
      updateCalculator();
    });

    currentHoursSlider.addEventListener('input', () => {
      currentHoursInput.value = currentHoursSlider.value;
      updateCalculator();
    });
  }

  // Terminal Simulation Engine
  let termInterval = null;
  let termTime = 75.0; // Current simulated hours
  let termRunning = false;

  function pad(n) {
    return n < 10 ? '0' + n : n;
  }

  function appendTerminalLine(text, className = 't-info') {
    const line = document.createElement('span');
    line.className = className;
    line.textContent = text;
    terminalOutput.appendChild(line);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  }

  function runTerminalTick() {
    termTime += (1.0 * SPEED_MULTIPLIER) / 3600.0;
    simHours.textContent = termTime.toFixed(2);

    const now = new Date();
    const timeStr = `${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;

    // Periodic gateway event logs
    const tickCount = Math.floor(termTime * 10) % 15;
    if (tickCount === 0) {
      appendTerminalLine(`[${timeStr}] [GATEWAY] Heartbeat acknowledged (seq_ack: ok, ping: 14ms)`, 't-comment');
    } else if (tickCount === 5) {
      appendTerminalLine(`[${timeStr}] [Op 22] Stream unpause refresh sent for Dual Broadcasters`, 't-info');
    } else if (tickCount === 10) {
      appendTerminalLine(`[${timeStr}] [SCIENCE] 2000x Telemetry payload synced (active_viewers: 2, sfu_sustain: 100%)`, 't-success');
    }

    // Update live HUD line in terminal
    let liveLine = terminalOutput.querySelector('.t-highlight');
    if (!liveLine) {
      liveLine = document.createElement('span');
      liveLine.className = 't-highlight';
      terminalOutput.appendChild(liveLine);
    }
    const realSec = Math.floor((termTime - 75.0) * 3600 / SPEED_MULTIPLIER);
    const m = Math.floor(realSec / 60);
    const s = realSec % 60;
    liveLine.textContent = `[LIVE 2000x] Dual Cross-Stream: ${pad(m)}:${pad(s)} (${termTime.toFixed(2)} hrs) | Rate: 2000x Turbo | Both Accounts Active`;
  }

  function startTerminal() {
    if (termRunning) return;
    termRunning = true;
    termStartBtn.textContent = 'قيد التشغيل...';
    termStartBtn.style.opacity = '0.7';
    appendTerminalLine(`[${new Date().toLocaleTimeString()}] [SYSTEM] Dual Cross-Streaming resumed at 2000x Turbo speed...`, 't-info');
    termInterval = setInterval(runTerminalTick, 1000);
  }

  function pauseTerminal() {
    termRunning = false;
    termStartBtn.textContent = 'استئناف المحاكاة';
    termStartBtn.style.opacity = '1';
    clearInterval(termInterval);
    appendTerminalLine(`[${new Date().toLocaleTimeString()}] [PAUSE] Simulator paused safely. Hours preserved.`, 't-comment');
  }

  function clearTerminal() {
    terminalOutput.innerHTML = '';
    appendTerminalLine('# Terminal cleared. Ready for session.', 't-comment');
  }

  if (termStartBtn) termStartBtn.addEventListener('click', startTerminal);
  if (termPauseBtn) termPauseBtn.addEventListener('click', pauseTerminal);
  if (termClearBtn) termClearBtn.addEventListener('click', clearTerminal);

  // Config Generator Logic
  function getSelectedMode() {
    for (const r of modeRadios) {
      if (r.checked) return r.value;
    }
    return 'dual';
  }

  function updateConfigPreview() {
    const token = (cfgToken.value.trim()) || "YOUR_DISCORD_TOKEN_HERE";
    const room = (cfgRoom.value.trim()) || "1559321217847271594";
    const viewer = (cfgViewer.value.trim()) || "";
    const mode = getSelectedMode();

    const configObj = {
      token: token,
      last_guild_id: "1491147576886689822",
      last_channel_id: room,
      viewer_token: viewer,
      speed_multiplier: SPEED_MULTIPLIER,
      mode: mode,
      self_mute: true,
      self_deaf: true,
      total_streamed_seconds: 0,
      generated_by: "m9mq_protocol_v3.5"
    };

    configCodePreview.textContent = JSON.stringify(configObj, null, 2);
  }

  if (cfgToken) cfgToken.addEventListener('input', updateConfigPreview);
  if (cfgRoom) cfgRoom.addEventListener('input', updateConfigPreview);
  if (cfgViewer) cfgViewer.addEventListener('input', updateConfigPreview);

  modeRadios.forEach(radio => {
    radio.addEventListener('change', () => {
      document.querySelectorAll('.radio-card').forEach(c => c.classList.remove('active'));
      radio.closest('.radio-card').classList.add('active');
      updateConfigPreview();
    });
  });

  if (btnGenerateConfig) {
    btnGenerateConfig.addEventListener('click', () => {
      updateConfigPreview();
      btnGenerateConfig.classList.add('flash');
      setTimeout(() => btnGenerateConfig.classList.remove('flash'), 400);
      alert('تم توليد ملف التكوين محلياً بنجاح!');
    });
  }

  if (btnDownloadConfig) {
    btnDownloadConfig.addEventListener('click', () => {
      updateConfigPreview();
      const content = configCodePreview.textContent;
      const blob = new Blob([content], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'stream_state.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

  if (btnCopyCommand) {
    btnCopyCommand.addEventListener('click', () => {
      const mode = getSelectedMode();
      let cmd = 'python spoofer.py';
      if (mode === 'hosting') {
        cmd = 'python main.py';
      }
      navigator.clipboard.writeText(cmd).then(() => {
        const origText = btnCopyCommand.innerHTML;
        btnCopyCommand.innerHTML = '<span>✓ تم النسخ بنجاح!</span>';
        setTimeout(() => {
          btnCopyCommand.innerHTML = origText;
        }, 2000);
      });
    });
  }

  // Language Dictionary
  const translations = {
    ar: {
      lang: 'EN',
      dir: 'rtl'
    },
    en: {
      lang: 'AR',
      dir: 'ltr'
    }
  };

  if (langToggle) {
    langToggle.addEventListener('click', () => {
      currentLang = currentLang === 'ar' ? 'en' : 'ar';
      document.documentElement.setAttribute('dir', translations[currentLang].dir);
      document.documentElement.setAttribute('lang', currentLang);
      langText.textContent = translations[currentLang].lang;
      updateCalculator();
    });
  }

  // Initial Calculation Run
  updateCalculator();
  updateConfigPreview();
})();
