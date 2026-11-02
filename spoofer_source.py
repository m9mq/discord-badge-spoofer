#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DISCORD BADGE SPOOFER v3.5 · BY m9mq
All Rights Reserved (C) 2026 m9mq
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import random
import re
import ssl
import struct
import subprocess
import sys
import tempfile
import threading
import time
import uuid
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterator, Sequence, Optional, Dict, Any

ROOT = Path(__file__).resolve().parent

def resolve_path(filename: str) -> Path:
    candidates = [
        ROOT / filename,
        ROOT / "data" / filename,
        ROOT.parent / filename,
        ROOT.parent / "data" / filename,
        ROOT / "discord-badge-spoofer-main" / filename,
        ROOT.parent / "discord-badge-spoofer-main" / filename,
    ]
    for c in candidates:
        if c.exists():
            return c
    return ROOT / filename

GAMES_FILE = resolve_path("games.json")
STATE_FILE = resolve_path("science_state.json")

ME_URL = "https://discord.com/api/v9/users/@me"
SCIENCE_URL = "https://discord.com/api/v9/science"
PROPERTIES_URL = "https://cordapi.dolfi.es/api/v2/properties/windows"
GAMES_CDN_URL = "https://cdn.discordapp.com/detectables/games.json"

BATCH_SIZE = 50
BATCH_DELAY = 1.0

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


def _user_id_from_token(token: str) -> str:
    try:
        first = token.strip().split(".", 1)[0]
        pad = "=" * (-len(first) % 4)
        return base64.b64decode(first + pad).decode("utf-8")
    except Exception:
        return ""


def generate_snowflake() -> str:
    discord_epoch = 1420070400000
    now_ms = int(time.time() * 1000)
    worker_id = random.randint(1, 31)
    process_id = random.randint(1, 31)
    seq = random.randint(1, 4095)
    sf = ((now_ms - discord_epoch) << 22) | (worker_id << 17) | (process_id << 12) | seq
    return str(sf)


class Console:
    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"
    WHITE = "\x1b[97m"
    BOLD_WHITE = "\x1b[1;97m"
    GREY = "\x1b[90m"
    LIGHT_GREY = "\x1b[37m"
    BORDER = "\x1b[90m"

    # Backward compatibility aliases mapped to monochrome
    VIOLET = "\x1b[97m"
    CYAN = "\x1b[97m"
    GREEN = "\x1b[97m"
    AMBER = "\x1b[90m"
    RED = "\x1b[90m"
    MUTED = "\x1b[90m"
    YELLOW = "\x1b[90m"
    ORANGE = "\x1b[90m"

    def __init__(self) -> None:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        if sys.platform == "win32":
            self._enable_ansi()

    @staticmethod
    def _enable_ansi() -> None:
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            pass

    def _stamp(self) -> str:
        return f"{self.GREY}[{time.strftime('%H:%M:%S')}]{self.RESET}"

    def ok(self, target: str, detail: str) -> None:
        print(f"  {self._stamp()} {self.BOLD_WHITE}[OK]{self.RESET} {self.WHITE}{target}{self.RESET} {self.GREY}─▶{self.RESET} {self.WHITE}{detail}{self.RESET}")

    def sent(self, target: str, detail: str) -> None:
        print(f"  {self._stamp()} {self.BOLD_WHITE}[+] {self.WHITE}{target}{self.RESET} {self.GREY}─▶{self.RESET} {self.WHITE}{detail}{self.RESET}")

    def warn(self, target: str, detail: str) -> None:
        print(f"  {self._stamp()} {self.GREY}[!] {self.WHITE}{target}{self.RESET} {self.GREY}─▶{self.RESET} {self.GREY}{detail}{self.RESET}")

    def err(self, target: str, detail: str) -> None:
        print(f"  {self._stamp()} {self.BOLD_WHITE}[X] {self.WHITE}{target}{self.RESET} {self.GREY}─▶{self.RESET} {self.GREY}{detail}{self.RESET}")

    def info(self, detail: str) -> None:
        print(f"  {self._stamp()} {self.BOLD_WHITE}[*]{self.RESET} {self.WHITE}{detail}{self.RESET}")

    def rule(self) -> None:
        print(f"  {self.GREY}{'─' * 55}{self.RESET}")

    def clear(self) -> None:
        print("\x1b[2J\x1b[3J\x1b[H", end="")

    def banner(self, user_info: Optional[Dict[str, Any]] = None, state: Optional[State] = None) -> None:
        self.clear()
        logo_lines = [
            "  ███╗   ███╗   ██████╗   ███╗   ███╗   ██████╗  ",
            "  ████╗ ████║  ██╔═████╗  ████╗ ████║  ██╔═══██╗ ",
            "  ██╔████╔██║  ██║██╔██║  ██╔████╔██║  ██║   ██║ ",
            "  ██║╚██╔╝██║  ████╔╝██║  ██║╚██╔╝██║  ██║▄▄ ██║ ",
            "  ██║ ╚═╝ ██║  ╚██████╔╝  ██║ ╚═╝ ██║  ╚██████╔╝ ",
            "  ╚═╝     ╚═╝   ╚═════╝   ╚═╝     ╚═╝   ╚══▀▀═╝  "
        ]
        print()
        for line in logo_lines:
            print(f"{self.BOLD_WHITE}{line}{self.RESET}")
        print(f"         {self.WHITE}DISCORD BADGE ENGINE · BY m9mq{self.RESET}\n")

        if user_info:
            uname = user_info.get("username", "m9mq")
            uid = user_info.get("id", "Unknown")
            print(f"  {self.GREY}───────────────────────────────────────────────────────{self.RESET}")
            print(f"  {self.WHITE}Username : {self.BOLD_WHITE}{uname}{self.RESET}")
            print(f"  {self.WHITE}User ID  : {self.GREY}{uid}{self.RESET}")
            print(f"  {self.GREY}───────────────────────────────────────────────────────{self.RESET}\n")



@dataclass
class State:
    token: str = ""
    cookie: str = ""
    fingerprint: str = ""
    analytics_token: str = ""
    fetched_at: int = 0
    used_games: list[str] = None
    total_games_claimed: int = 0
    total_hours_claimed: float = 0.0
    total_stream_hours_claimed: float = 0.0
    last_guild_id: str = "1491147576886689822"
    last_channel_id: str = "1559321217847271594"
    viewer_token: str = ""

    def __post_init__(self) -> None:
        if self.used_games is None:
            self.used_games = []

    @classmethod
    def load(cls) -> "State":
        for p in [STATE_FILE, ROOT / "science_state.json", ROOT.parent / "science_state.json", ROOT / "discord-badge-spoofer-main" / "science_state.json"]:
            if p.exists():
                try:
                    data = json.loads(p.read_text(encoding="utf-8"))
                    state = cls(**{k: data.get(k, v) for k, v in cls().__dict__.items() if k != "used_games"})
                    state.used_games = data.get("used_games", [])
                    return state
                except Exception:
                    pass
        return cls()

    def save(self) -> None:
        try:
            data = asdict(self)
            STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
            STATE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
            # Sync to subfolder if exists
            sub = ROOT / "discord-badge-spoofer-main" / "science_state.json"
            if sub.parent.exists() and sub != STATE_FILE:
                sub.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception:
            pass

    @property
    def has_token(self) -> bool:
        return bool(self.token.strip())


def build_super_props(launch_signature: str, heartbeat_session: str) -> str:
    props = {
        "os": "Windows",
        "browser": "Discord Client",
        "release_channel": "stable",
        "client_version": "1.0.9253",
        "os_version": "10.0.26200",
        "os_arch": "x64",
        "app_arch": "x64",
        "system_locale": "en-US",
        "has_client_mods": False,
        "browser_user_agent": USER_AGENT,
        "browser_version": "42.7.1",
        "os_sdk_version": "26200",
        "client_build_number": 594031,
        "native_build_number": 88414,
        "client_event_source": None,
        "client_app_state": "focused",
        "client_launch_id": str(uuid.uuid4()),
        "launch_signature": launch_signature,
        "client_heartbeat_session_id": heartbeat_session,
    }
    raw = json.dumps(props, separators=(",", ":")).encode("utf-8")
    return base64.b64encode(raw).decode("ascii")


def auto_fetch_discord_cookies() -> str:
    try:
        cmd = [
            "curl.exe", "-s", "-i",
            "https://discord.com",
            "-H", f"user-agent: {USER_AGENT}"
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=8)
        cookies = []
        for line in proc.stdout.splitlines():
            if line.lower().startswith("set-cookie:"):
                c = line.split(":", 1)[1].strip().split(";")[0]
                cookies.append(c)
        if cookies:
            return "; ".join(cookies)
    except Exception:
        pass
    return ""


def fetch_user_profile(auth_token: str, super_props: str = "") -> Dict[str, Any]:
    # Try curl first
    try:
        cmd = [
            "curl.exe", "-s",
            f"{ME_URL}?with_analytics_token=true",
            "-H", f"authorization: {auth_token}",
            "-H", f"user-agent: {USER_AGENT}",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if proc.stdout.strip().startswith("{"):
            data = json.loads(proc.stdout)
            if "analytics_token" in data or "username" in data:
                return data
    except Exception:
        pass

    req = urllib.request.Request(
        f"{ME_URL}?with_analytics_token=true",
        headers={
            "authorization": auth_token,
            "user-agent": USER_AGENT,
        }
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


@dataclass(frozen=True)
class Session:
    heartbeat_session: str
    launch_signature: str
    super_props: str

    @classmethod
    def new(cls) -> "Session":
        hb = str(uuid.uuid4())
        sig = str(uuid.uuid4())
        return cls(hb, sig, build_super_props(sig, hb))


@dataclass(frozen=True)
class Game:
    id: str
    name: str
    exe: str


def _win_exe(game: dict) -> str:
    for entry in game.get("executables", []):
        if entry.get("os") == "win32" and entry.get("name"):
            return entry["name"]
    return "game.exe"


def _parse_games(raw: str) -> list[Game]:
    data = json.loads(raw)
    games: list[Game] = []
    seen: set[str] = set()
    for entry in data:
        gid = str(entry.get("id", ""))
        if not gid.isdigit() or gid in seen:
            continue
        if not any(e.get("os") == "win32" and e.get("name") for e in entry.get("executables", [])):
            continue
        seen.add(gid)
        games.append(Game(gid, entry.get("name", "Unknown"), _win_exe(entry)))
    return games


def load_games() -> list[Game]:
    for p in [GAMES_FILE, ROOT / "data" / "games.json", ROOT / "games.json", ROOT.parent / "data" / "games.json"]:
        if p.exists():
            try:
                raw = p.read_text(encoding="utf-8").strip()
                if raw:
                    return _parse_games(raw)
            except Exception:
                pass
    try:
        req = urllib.request.Request(GAMES_CDN_URL, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=25) as r:
            raw = r.read().decode("utf-8")
        GAMES_FILE.write_text(raw, encoding="utf-8")
        return _parse_games(raw)
    except Exception:
        return []


class ScienceClient:
    def __init__(self, state: State, session: Session) -> None:
        self.state = state
        self.session = session
        self._seq = 0

    def _next_seq(self) -> int:
        self._seq += 1
        return self._seq

    def build_launch(self, game: Game, stream_voice: bool = False, channel_id: Optional[str] = None, guild_id: Optional[str] = None) -> dict:
        now = int(time.time() * 1000)
        props: Dict[str, Any] = {
            "client_track_timestamp": now,
            "client_heartbeat_session_id": self.session.heartbeat_session,
            "event_sequence_number": self._next_seq(),
            "game": game.name,
            "game_id": game.id,
            "verified": True,
            "elevated": False,
            "is_launcher": False,
            "game_platform": "desktop",
            "detection_method": "verified_game",
            "is_overlay_enabled": False,
            "is_overlay_game_enabled": True,
            "is_overlay_game_source": "OOP_DEFAULT_DATABASE",
            "fullscreen_type": "UNKNOWN",
            "hardware_display_count": 1,
            "overlay_method": "Disabled",
            "activity_status_enabled": True,
            "activity_status_shared_guilds": [],
            "current_user_status": "online",
            "game_detection_enabled": True,
            "executable_path": game.exe,
            "voice_channel_id": channel_id,
            "voice_channel_type": 2 if channel_id else None,
            "voice_channel_bitrate": 64000 if channel_id else None,
            "voice_channel_guild_id": guild_id,
            "hidden_by_distributor": False,
            "game_metadata": None,
            "client_performance_cpu": None,
            "client_performance_memory": None,
            "cpu_core_count": None,
            "accessibility_features": 0,
            "rendered_locale": "en-US",
            "launch_signature": self.session.launch_signature,
            "client_rtc_state": "connected" if stream_voice else None,
            "client_app_state": "focused",
            "client_send_timestamp": now,
        }
        if self.state.fingerprint:
            props["executable_fingerprint"] = self.state.fingerprint
        return {"type": "launch_game", "properties": props}

    def build_heartbeat(self, game: Game, duration_ms: int, session_id: str,
                        initial: bool, final: bool, ts: int | None = None,
                        rtc_id: Optional[str] = None, media_id: Optional[str] = None,
                        channel_id: Optional[str] = None, guild_id: Optional[str] = None) -> dict:
        ts = int(time.time() * 1000) if ts is None else ts
        return {
            "type": "running_game_heartbeat",
            "properties": {
                "client_track_timestamp": ts,
                "client_heartbeat_session_id": self.session.heartbeat_session,
                "event_sequence_number": self._next_seq(),
                "game_id": game.id,
                "game_name": game.name,
                "game_metadata": None,
                "game_executable": game.exe,
                "game_detection_enabled": True,
                "initial_heartbeat": initial,
                "final_heartbeat": final,
                "game_session_id": session_id,
                "duration_tracked_ms": duration_ms,
                "rtc_connection_id": rtc_id,
                "media_session_id": media_id,
                "voice_channel_id": channel_id,
                "voice_channel_type": 2 if channel_id else None,
                "voice_channel_guild_id": guild_id,
                "launch_signature": self.session.launch_signature,
                "client_app_state": "focused",
                "client_send_timestamp": ts,
            },
        }

    def build_stream_events(self, game: Game, duration_ms: int, channel_id: Optional[str] = None, guild_id: Optional[str] = None) -> list[dict]:
        sid = str(uuid.uuid4())
        rtc_id = str(uuid.uuid4())
        media_id = uuid.uuid4().hex
        ch_id = channel_id.strip() if channel_id and channel_id.strip().isdigit() else generate_snowflake()
        g_id = guild_id.strip() if guild_id and guild_id.strip().isdigit() else generate_snowflake()
        viewer_id = generate_snowflake()
        viewer_id_2 = generate_snowflake()
        now = int(time.time() * 1000)
        start = now - duration_ms if now > duration_ms else now
        dur_sec = max(1, int(duration_ms / 1000))

        return [
            self.build_launch(game, stream_voice=True, channel_id=ch_id, guild_id=g_id),
            {
                "type": "video_stream_started",
                "properties": {
                    "client_track_timestamp": start,
                    "client_heartbeat_session_id": self.session.heartbeat_session,
                    "event_sequence_number": self._next_seq(),
                    "stream_source_type": "window",
                    "guild_id": g_id,
                    "channel_id": ch_id,
                    "channel_type": 2,
                    "rtc_connection_id": rtc_id,
                    "media_session_id": media_id,
                    "share_game": True,
                    "game_id": game.id,
                    "game_name": game.name,
                    "is_soundshare": True,
                    "max_viewers": 2,
                    "num_viewers": 2,
                    "viewer_count": 2,
                    "has_viewers": True,
                    "stream_has_viewers": True,
                    "active_viewers": [viewer_id, viewer_id_2],
                    "launch_signature": self.session.launch_signature,
                    "client_app_state": "focused",
                    "client_send_timestamp": start,
                }
            },
            self.build_heartbeat(game, 0, sid, True, False, start, rtc_id, media_id, ch_id, g_id),
            self.build_heartbeat(game, duration_ms, sid, False, True, now, rtc_id, media_id, ch_id, g_id),
            {
                "type": "screenshare_finished",
                "properties": {
                    "client_track_timestamp": now,
                    "client_heartbeat_session_id": self.session.heartbeat_session,
                    "event_sequence_number": self._next_seq(),
                    "duration": dur_sec,
                    "duration_ms": duration_ms,
                    "duration_with_viewers": dur_sec,
                    "duration_with_viewers_ms": duration_ms,
                    "media_session_id": media_id,
                    "rtc_connection_id": rtc_id,
                    "stream_source_type": "window",
                    "game_id": game.id,
                    "max_viewers": 2,
                    "num_viewers": 2,
                    "viewer_count": 2,
                    "has_viewers": True,
                    "client_app_state": "focused",
                    "client_send_timestamp": now,
                }
            },
            {
                "type": "video_stream_ended",
                "properties": {
                    "client_track_timestamp": now,
                    "client_heartbeat_session_id": self.session.heartbeat_session,
                    "event_sequence_number": self._next_seq(),
                    "stream_source_type": "window",
                    "guild_id": g_id,
                    "channel_id": ch_id,
                    "channel_type": 2,
                    "duration": dur_sec,
                    "duration_ms": duration_ms,
                    "duration_with_viewers": dur_sec,
                    "duration_with_viewers_ms": duration_ms,
                    "rtc_connection_id": rtc_id,
                    "media_session_id": media_id,
                    "game_id": game.id,
                    "game_name": game.name,
                    "max_viewers": 2,
                    "max_concurrent_viewers": 2,
                    "num_viewers": 2,
                    "viewer_count": 2,
                    "total_viewers": 2,
                    "has_viewers": True,
                    "stream_has_viewers": True,
                    "launch_signature": self.session.launch_signature,
                    "client_app_state": "focused",
                    "client_send_timestamp": now,
                }
            }
        ]

    def build_playtime(self, game: Game, duration_ms: int) -> list[dict]:
        sid = str(uuid.uuid4())
        now = int(time.time() * 1000)
        start = now - duration_ms if now > duration_ms else now
        return [
            self.build_heartbeat(game, 0, sid, initial=True, final=False, ts=start),
            self.build_launch(game),
            self.build_heartbeat(game, duration_ms, sid, initial=False, final=True, ts=now),
        ]

    def post(self, events: Sequence[dict]) -> int:
        payload = {"token": self.state.analytics_token, "events": list(events)}
        body_bytes = json.dumps(payload).encode("utf-8")

        # Use curl.exe directly on Windows (Bypasses Cloudflare block)
        if sys.platform == "win32":
            try:
                tf = tempfile.NamedTemporaryFile("wb", delete=False)
                tf.write(body_bytes)
                tf_name = tf.name
                tf.close()

                cmd = [
                    "curl.exe", "-s", "-o", "NUL", "-w", "%{http_code}",
                    SCIENCE_URL,
                    "-X", "POST",
                    "-H", "content-type: application/json",
                ]
                if self.state.cookie:
                    cmd.extend(["-H", f"cookie: {self.state.cookie}"])
                cmd.append(f"-d@{tf_name}")
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                try:
                    os.unlink(tf_name)
                except OSError:
                    pass

                code_str = proc.stdout.strip()
                if code_str.isdigit():
                    return int(code_str)
            except Exception:
                pass

        # Standard urllib fallback
        req = urllib.request.Request(SCIENCE_URL, data=body_bytes, method="POST", headers={"content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=12) as res:
                return res.status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            return 0


def _chunked(items: Sequence[Any], size: int) -> Iterator[Sequence[Any]]:
    for start in range(0, len(items), size):
        yield items[start:start + size]


class AsyncWebSocket:
    """Minimal RFC 6455 WebSocket client using pure Python standard library."""

    def __init__(self, url: str) -> None:
        self.url = url
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self.closed = False
        self._lock = asyncio.Lock()

    async def connect(self) -> None:
        m = re.match(r"^(wss?|https?)://([^/:]+)(?::(\d+))?(/.*)?$", self.url)
        if not m:
            raise ValueError(f"Invalid WS URL: {self.url}")
        scheme, host, port_s, path = m.groups()
        use_ssl = scheme in ("wss", "https")
        port = int(port_s) if port_s else (443 if use_ssl else 80)
        ssl_ctx = ssl.create_default_context() if use_ssl else None

        self.reader, self.writer = await asyncio.open_connection(
            host, port, ssl=ssl_ctx, server_hostname=host if use_ssl else None
        )
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        req = (
            f"GET {path or '/'} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Upgrade: websocket\r\n"
            f"Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            f"Sec-WebSocket-Version: 13\r\n"
            f"User-Agent: {USER_AGENT}\r\n\r\n"
        )
        self.writer.write(req.encode())
        await self.writer.drain()

        status = await self.reader.readline()
        if not status.startswith(b"HTTP/1.1 101"):
            raise ConnectionError(f"Handshake failed: {status.decode(errors='ignore').strip()}")
        while (await self.reader.readline()) not in (b"\r\n", b"\n", b""):
            pass

    async def send_json(self, data: dict[str, Any]) -> None:
        await self._send_frame(0x1, json.dumps(data, separators=(",", ":")).encode("utf-8"))

    async def _send_frame(self, opcode: int, payload: bytes) -> None:
        if self.closed or not self.writer:
            return
        async with self._lock:
            length = len(payload)
            hdr = bytearray([0x80 | (opcode & 0x0F)])
            if length < 126:
                hdr.append(0x80 | length)
            elif length <= 0xFFFF:
                hdr.append(0x80 | 126)
                hdr.extend(struct.pack("!H", length))
            else:
                hdr.append(0x80 | 127)
                hdr.extend(struct.pack("!Q", length))
            mask = os.urandom(4)
            hdr.extend(mask)
            masked = bytes(b ^ mask[i & 3] for i, b in enumerate(payload))
            self.writer.write(hdr + masked)
            await self.writer.drain()

    async def recv_json(self) -> Optional[dict[str, Any]]:
        if not self.reader or self.closed:
            return None
        buf = bytearray()
        msg_op = None
        while True:
            b1, b2 = await self.reader.readexactly(2)
            fin, op, masked, length = bool(b1 & 0x80), b1 & 0x0F, bool(b2 & 0x80), b2 & 0x7F
            if length == 126:
                length = struct.unpack("!H", await self.reader.readexactly(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", await self.reader.readexactly(8))[0]
            mask = await self.reader.readexactly(4) if masked else b""
            data = await self.reader.readexactly(length) if length else b""
            if masked:
                data = bytes(b ^ mask[i & 3] for i, b in enumerate(data))

            if op == 0x8:
                self.closed = True
                raise ConnectionResetError("WebSocket closed by server")
            elif op == 0x9:
                await self._send_frame(0xA, data)
                continue
            elif op == 0xA:
                continue
            elif op in (0x1, 0x2):
                msg_op = op
                buf.extend(data)
            elif op == 0x0:
                buf.extend(data)

            if fin:
                if msg_op == 0x1:
                    return json.loads(buf.decode("utf-8", errors="replace"))
                buf.clear()
                msg_op = None

    async def close(self) -> None:
        if self.closed:
            return
        if self.writer:
            try:
                await self._send_frame(0x8, struct.pack("!H", 1000))
                self.writer.close()
            except Exception:
                pass
        self.closed = True


async def keep_rtc_alive(endpoint: str, server_id: str, channel_id: str, user_id: str, session_id: str, token: str) -> None:
    url = endpoint if endpoint.startswith("wss://") else f"wss://{endpoint}"
    if "?v=" not in url:
        url = f"{url.rstrip('/')}/?v=8"
    ws = AsyncWebSocket(url)
    hb_task = None
    try:
        await ws.connect()
        await ws.send_json(
            {
                "op": 0,
                "d": {
                    "server_id": str(server_id),
                    "channel_id": str(channel_id),
                    "user_id": str(user_id),
                    "session_id": session_id,
                    "token": token,
                    "video": True,
                    "streams": [{"type": "screen", "rid": "100", "quality": 100}],
                },
            }
        )
        while not ws.closed:
            msg = await ws.recv_json()
            if not msg:
                break
            op, d = msg.get("op"), msg.get("d") or {}
            if op == 8:
                interval = d.get("heartbeat_interval", 15000) / 1000.0

                async def hb() -> None:
                    while not ws.closed:
                        await ws.send_json({"op": 3, "d": {"t": int(time.time() * 1000), "seq_ack": -1}})
                        await asyncio.sleep(interval)

                hb_task = asyncio.create_task(hb())
            elif op == 2:
                ssrc = d.get("ssrc", 1)
                await ws.send_json(
                    {
                        "op": 12,
                        "d": {
                            "audio_ssrc": ssrc,
                            "video_ssrc": ssrc + 1,
                            "rtx_ssrc": ssrc + 2,
                            "streams": [
                                {
                                    "type": "video",
                                    "rid": "100",
                                    "ssrc": ssrc + 1,
                                    "active": True,
                                    "quality": 100,
                                    "rtx_ssrc": ssrc + 2,
                                    "max_bitrate": 2500000,
                                    "max_framerate": 30,
                                    "max_resolution": {"type": "fixed", "width": 1280, "height": 720},
                                }
                            ],
                        },
                    }
                )
    except Exception:
        pass
    finally:
        if hb_task:
            hb_task.cancel()
        await ws.close()


class VoiceStreamEngine:
    def __init__(
        self,
        token: str,
        guild_id: str,
        channel_id: str,
        console: Console,
        client: Optional[ScienceClient] = None,
        game_name: str = "Discord Streamer",
        speed_multiplier: float = 2000.0,
        viewer_token: Optional[str] = None,
    ) -> None:
        self.token = token
        self.viewer_token = viewer_token.strip() if viewer_token else ""
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.console = console
        self.client = client
        self.game_name = game_name
        self.speed_multiplier = speed_multiplier
        self.stop_event = asyncio.Event()
        self.start_time = 0.0
        self.shared: dict[str, Any] = {}

    async def run(self) -> float:
        C = self.console
        mode_text = "Dual Cross-Stream" if self.viewer_token else "Solo Spoof"
        C.info(f"Starting {mode_text} Engine in voice channel {self.channel_id} (Rate: {self.speed_multiplier:g}x Turbo)...")

        async def run_worker(acc_token: str, role: str) -> None:
            gateway_url = "wss://gateway.discord.gg/?v=10&encoding=json"
            while not self.stop_event.is_set():
                ws = AsyncWebSocket(gateway_url)
                hb_task = None
                refresh_task = None
                rtc_tasks = []
                seq = None
                user_id = None
                session_id = None

                try:
                    await ws.connect()
                    while not self.stop_event.is_set() and not ws.closed:
                        msg = await ws.recv_json()
                        if not msg:
                            break
                        op, t, s, d = msg.get("op"), msg.get("t"), msg.get("s"), msg.get("d") or {}
                        if s is not None:
                            seq = s

                        if op == 10:
                            interval = d.get("heartbeat_interval", 41250) / 1000.0

                            async def gateway_hb() -> None:
                                while not self.stop_event.is_set() and not ws.closed:
                                    await ws.send_json({"op": 1, "d": seq})
                                    await asyncio.sleep(interval)

                            hb_task = asyncio.create_task(gateway_hb())
                            await ws.send_json(
                                {
                                    "op": 2,
                                    "d": {
                                        "token": acc_token,
                                        "capabilities": 16381,
                                        "properties": {
                                            "os": "Windows",
                                            "browser": "Discord Client",
                                            "release_channel": "stable",
                                            "client_version": "1.0.9168",
                                            "os_version": "10.0.22631",
                                            "os_arch": "x64",
                                            "app_arch": "x64",
                                            "system_locale": "en-US",
                                            "browser_user_agent": USER_AGENT,
                                            "browser_version": "32.2.2",
                                            "client_build_number": 343349,
                                        },
                                        "presence": {
                                            "status": "online",
                                            "since": 0,
                                            "activities": [{"name": self.game_name, "type": 1, "url": "https://twitch.tv/m9mq"}],
                                            "afk": False,
                                        },
                                        "compress": False,
                                    },
                                }
                            )

                        elif op == 0 and t == "READY":
                            u = d.get("user") or {}
                            user_id = u.get("id")
                            username = u.get("username", "user")
                            session_id = d.get("session_id")
                            self.shared[f"{role}_id"] = user_id
                            C.ok("Gateway", f"Connected ({role}) ─▶ {username} (ID: {user_id})")

                            # Opcode 4: Join Voice Channel
                            await ws.send_json(
                                {
                                    "op": 4,
                                    "d": {
                                        "guild_id": self.guild_id,
                                        "channel_id": self.channel_id,
                                        "self_mute": True,
                                        "self_deaf": True,
                                        "self_video": False,
                                    },
                                }
                            )

                            await asyncio.sleep(1.0)
                            stream_key = (
                                f"guild:{self.guild_id}:{self.channel_id}:{user_id}"
                                if self.guild_id
                                else f"call:{self.channel_id}:{user_id}"
                            )
                            self.shared[f"{role}_key"] = stream_key

                            # Opcode 18: Start Screen Share (Go Live)
                            await ws.send_json(
                                {
                                    "op": 18,
                                    "d": {
                                        "type": "guild" if self.guild_id else "call",
                                        "guild_id": self.guild_id,
                                        "channel_id": self.channel_id,
                                        "preferred_region": None,
                                    },
                                }
                            )
                            await asyncio.sleep(0.5)
                            # Opcode 22: Unpause Stream
                            await ws.send_json({"op": 22, "d": {"stream_key": stream_key, "paused": False}})
                            if self.start_time == 0.0:
                                self.start_time = time.time()
                            C.ok("Go Live", f"({username}) Screen Share is BROADCASTING LIVE!")

                            async def keep_stream_unpaused() -> None:
                                while not self.stop_event.is_set() and not ws.closed:
                                    await asyncio.sleep(45)
                                    try:
                                        await ws.send_json({"op": 22, "d": {"stream_key": stream_key, "paused": False}})
                                    except Exception:
                                        break

                            refresh_task = asyncio.create_task(keep_stream_unpaused())

                            # Cross-Watch task: watch the other account's stream
                            other_role = "acc2" if role == "acc1" else "acc1"

                            async def cross_watch_loop() -> None:
                                watched = False
                                for _ in range(60):
                                    if self.stop_event.is_set() or ws.closed:
                                        break
                                    target_key = self.shared.get(f"{other_role}_key")
                                    if target_key:
                                        await ws.send_json({"op": 20, "d": {"stream_key": target_key}})
                                        C.ok("Cross-Watch", f"({username}) is watching {other_role} stream! [Dual Active Hours Enabled]")
                                        watched = True
                                        break
                                    await asyncio.sleep(1.0)
                                if not watched and not ws.closed:
                                    # Solo mode: watch own stream
                                    await ws.send_json({"op": 20, "d": {"stream_key": stream_key}})

                            asyncio.create_task(cross_watch_loop())

                        elif op == 0 and t in ("VOICE_SERVER_UPDATE", "STREAM_SERVER_UPDATE"):
                            ep, tok = d.get("endpoint"), d.get("token")
                            if ep and tok and user_id and session_id:
                                rtc_tasks.append(
                                    asyncio.create_task(
                                        keep_rtc_alive(ep, str(self.guild_id or self.channel_id), self.channel_id, user_id, session_id, tok)
                                    )
                                )

                        elif op in (7, 9):
                            break

                except Exception:
                    pass
                finally:
                    if hb_task:
                        hb_task.cancel()
                    if refresh_task:
                        refresh_task.cancel()
                    for task in rtc_tasks:
                        task.cancel()
                    await ws.close()

                if self.stop_event.is_set():
                    break
                await asyncio.sleep(3)

        tasks = [asyncio.create_task(run_worker(self.token, "acc1"))]
        if self.viewer_token:
            tasks.append(asyncio.create_task(run_worker(self.viewer_token, "acc2")))

        last_sync = time.time()
        try:
            while not self.stop_event.is_set():
                await asyncio.sleep(1.0)
                if self.start_time > 0:
                    real_elapsed = time.time() - self.start_time
                    boosted_elapsed = real_elapsed * self.speed_multiplier
                    hrs = boosted_elapsed / 3600.0
                    h = int(boosted_elapsed // 3600)
                    m = int((boosted_elapsed % 3600) // 60)
                    s = int(boosted_elapsed % 60)
                    label = "Dual Cross-Stream" if self.viewer_token else "Solo Spoof"
                    sys.stdout.write(
                        f"\r  {C._stamp()} {C.BOLD_WHITE}[LIVE 2000x]{C.RESET} {label}: {h:02d}:{m:02d}:{s:02d} ({hrs:,.2f} hrs) | "
                        f"Rate: {self.speed_multiplier:g}x Turbo | Press Enter to Stop   "
                    )
                    sys.stdout.flush()

                    if time.time() - last_sync >= 10.0 and self.client:
                        last_sync = time.time()
                        try:
                            dummy_game = Game("356875221078245376", self.game_name, "game.exe")
                            events = self.client.build_stream_events(dummy_game, int(boosted_elapsed * 1000), self.channel_id, self.guild_id)
                            self.client.post(events)
                        except Exception:
                            pass
        finally:
            for t in tasks:
                t.cancel()

        total_elapsed = ((time.time() - self.start_time) * self.speed_multiplier) if self.start_time > 0 else 0.0
        return total_elapsed / 3600.0


class BadgeApp:
    def __init__(self) -> None:
        self.console = Console()
        self.state = State.load()
        self.session = Session.new()
        self.client = ScienceClient(self.state, self.session)
        self.games = load_games()
        self.user_info: Optional[Dict[str, Any]] = None

    def start(self) -> None:
        C = self.console

        # 1. Token setup
        if not self.state.has_token:
            self.console.banner()
            while not self.state.has_token:
                token = input(f"  {C.WHITE}Enter Discord Token: {C.RESET}").strip().strip('"').strip("'")
                if token:
                    self.state.token = token
                    self.state.save()

        # 2. Analytics token setup
        try:
            self.user_info = fetch_user_profile(self.state.token, self.session.super_props)
            if self.user_info and "analytics_token" in self.user_info:
                self.state.analytics_token = self.user_info["analytics_token"]
                self.state.save()
        except Exception:
            pass

        if not self.user_info:
            uid = _user_id_from_token(self.state.token)
            self.user_info = {"username": "m9mq", "id": uid or "1318528650110304298"}

        if not self.state.analytics_token:
            uid = self.user_info.get("id", "")
            C.warn("Auth", f"Could not auto-fetch analytics token for account {uid}.")
            man = input(f"  {C.WHITE}Paste analytics_token manually: {C.RESET}").strip().strip('"').strip("'")
            if man:
                self.state.analytics_token = man
                self.state.save()

        # 3. Automatic cookie sync
        if not self.state.cookie or "cf_clearance=valid123" in self.state.cookie:
            fresh_cookie = auto_fetch_discord_cookies()
            if fresh_cookie:
                self.state.cookie = fresh_cookie
                self.state.save()

        self.menu()

    def run_batches(self, items: Sequence[Any], build_fn) -> int:
        C = self.console
        total = len(items)
        sent = 0
        chunks = list(_chunked(items, BATCH_SIZE))
        total_chunks = len(chunks)

        for idx, chunk in enumerate(chunks, 1):
            events = []
            for item in chunk:
                events.extend(build_fn(item))

            status = self.client.post(events)
            if status == 429:
                C.warn("Rate-Limit", "Cloudflare cooldown, waiting 5s...")
                time.sleep(5)
                status = self.client.post(events)

            if status == 204:
                sent += len(chunk)
                pct = int((idx / total_chunks) * 100)
                bar_len = 20
                filled = int(bar_len * (idx / total_chunks))
                bar = "█" * filled + "░" * (bar_len - filled)
                print(f"  {C._stamp()} [{bar}] {pct:>3}% │ Batch {idx:02d}/{total_chunks:02d} ({sent:,}/{total:,}) ─▶ [204 OK]")
            elif status in (401, 403):
                C.err(f"Batch {idx}", f"[{status}] Auth rejected. Please check your token via [4].")
                return sent
            else:
                C.warn(f"Batch {idx}", f"Status {status}")
            time.sleep(BATCH_DELAY)
        return sent

    def claim_playtime(self) -> None:
        C = self.console
        C.banner(self.user_info, self.state)
        print(f"  {C.GREY}───────────────── [ MODULE: PLAYTIME BOOSTER ] ─────────────────{C.RESET}")
        print(f"  {C.WHITE}Boost Discord game presence & hours across verified games.{C.RESET}")
        print(f"  {C.GREY}─────────────────────────────────────────────────────────────────{C.RESET}\n")

        raw_count = input(f"  {C.WHITE}Target games count [default: 100]: {C.RESET}").strip()
        count = int(raw_count) if raw_count.isdigit() else 100
        count = max(1, min(count, len(self.games)))

        raw_hours = input(f"  {C.WHITE}Hours per game [default: 50]: {C.RESET}").strip()
        try:
            hours = float(raw_hours) if raw_hours else 50.0
        except ValueError:
            hours = 50.0

        selected = self._select_games(count)
        dur_ms = int(hours * 3600 * 1000)
        print()
        C.info(f"Injecting telemetry for {len(selected)} games x {hours:g}h ({len(selected)*hours:,.0f}h total)...")
        print()

        ok = self.run_batches(selected, lambda g: self.client.build_playtime(g, dur_ms))
        print()
        C.ok("Completed", f"{ok}/{len(selected)} game playtime payloads registered.")
        self.state.total_games_claimed += ok
        self.state.total_hours_claimed += ok * hours
        self.state.save()
        input(f"\n  {C.GREY}Press Enter to return to main menu...{C.RESET}")

    def claim_games(self) -> None:
        C = self.console
        C.banner(self.user_info, self.state)
        print(f"  {C.GREY}────────────────── [ MODULE: VARIETY BOOSTER ] ──────────────────{C.RESET}")
        print(f"  {C.WHITE}Unlock unique game presence badges by registering library titles.{C.RESET}")
        print(f"  {C.GREY}─────────────────────────────────────────────────────────────────{C.RESET}\n")

        raw_count = input(f"  {C.WHITE}Number of games to mark played [default: 120]: {C.RESET}").strip()
        count = int(raw_count) if raw_count.isdigit() else 120
        count = max(1, min(count, len(self.games)))

        selected = self._select_games(count)
        print()
        C.info(f"Registering {len(selected)} unique games in Discord telemetry...")
        print()

        ok = self.run_batches(selected, lambda g: self.client.build_playtime(g, 60 * 1000))
        print()
        C.ok("Completed", f"{ok}/{len(selected)} unique games registered successfully.")
        self.state.total_games_claimed += ok
        self.state.save()
        input(f"\n  {C.GREY}Press Enter to return to main menu...{C.RESET}")

    def claim_stream(self) -> None:
        C = self.console
        C.banner(self.user_info, self.state)
        print(f"  {C.GREY}──────────────── [ MODULE: STREAMING BADGE PRO ] ────────────────{C.RESET}")
        print(f"  {C.WHITE}[1] Live Voice Room Streamer (Account joins room & streams live 24/7){C.RESET}")
        print(f"  {C.WHITE}[2] Turbo Telemetry Injector (Inject 1h - 5,000h badge milestones){C.RESET}")
        print(f"  {C.WHITE}[0] Return to main menu{C.RESET}")
        print(f"  {C.GREY}─────────────────────────────────────────────────────────────────{C.RESET}\n")

        sub_choice = input(f"  {C.WHITE}Select mode [default: 1]: {C.RESET}").strip()
        if sub_choice == "0":
            return

        def_guild = self.state.last_guild_id or "1491147576886689822"
        def_channel = self.state.last_channel_id or "1559321217847271594"

        room_in = input(f"  {C.WHITE}Voice Channel ID or URL [default: {def_channel}]: {C.RESET}").strip()
        raw_guild = def_guild
        raw_channel = def_channel

        if room_in:
            url_match = re.search(r"discord(?:app)?\.com/channels/(@me|\d+)/(\d+)", room_in)
            if url_match:
                g, c = url_match.group(1), url_match.group(2)
                raw_guild = def_guild if g == "@me" else g
                raw_channel = c
            else:
                id_match = re.search(r"(\d{15,22})", room_in)
                if id_match:
                    raw_channel = id_match.group(1)
                else:
                    raw_channel = room_in

        self.state.last_guild_id = raw_guild
        self.state.last_channel_id = raw_channel
        self.state.save()

        def_viewer = self.state.viewer_token or ""
        viewer_hint = f" [saved: {def_viewer[:10]}...]" if def_viewer else " [press Enter to spoof solo 2000x]"
        viewer_in = input(f"  {C.WHITE}Secondary Account Token (Dual Cross-Stream){viewer_hint}: {C.RESET}").strip()
        if viewer_in:
            self.state.viewer_token = viewer_in
            self.state.save()
        elif not viewer_in and def_viewer:
            viewer_in = def_viewer

        if sub_choice in ("1", ""):
            print()
            C.info(f"Starting real-time Voice Streamer in channel: {raw_channel}...")
            engine = VoiceStreamEngine(
                self.state.token,
                raw_guild,
                raw_channel,
                self.console,
                self.client,
                speed_multiplier=2000.0,
                viewer_token=viewer_in,
            )

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            def wait_for_enter():
                time.sleep(1.0)
                try:
                    sys.stdin.readline()
                except Exception:
                    pass
                loop.call_soon_threadsafe(engine.stop_event.set)

            t = threading.Thread(target=wait_for_enter, daemon=True)
            t.start()

            try:
                hours_streamed = loop.run_until_complete(engine.run())
            except KeyboardInterrupt:
                engine.stop_event.set()
                hours_streamed = ((time.time() - engine.start_time) * engine.speed_multiplier) / 3600.0 if engine.start_time > 0 else 0.0
            finally:
                loop.close()

            print()
            C.ok("Completed", f"Disconnected from voice room. Logged {hours_streamed:,.2f} streaming hours (2000x Turbo).")
            self.state.total_stream_hours_claimed += hours_streamed
            self.state.save()
            input(f"\n  {C.GREY}Press Enter to return to main menu...{C.RESET}")

        elif sub_choice == "2":
            raw_hours = input(f"  {C.WHITE}Stream hours to inject [default: 5000]: {C.RESET}").strip()
            try:
                hours = float(raw_hours) if raw_hours else 5000.0
            except ValueError:
                hours = 5000.0

            session_dur = 8.0
            sessions = max(1, int(hours / session_dur))
            dur_each_ms = int((hours / sessions) * 3600 * 1000)
            chosen_games = random.choices(self.games, k=sessions)
            jobs = [(g, dur_each_ms) for g in chosen_games]

            print()
            C.info(f"Dispatching {len(jobs)} stream sessions ({hours:,.0f} hours total telemetry)...")
            print()

            ok = self.run_batches(jobs, lambda j: self.client.build_stream_events(j[0], j[1], raw_channel, raw_guild))
            print()
            C.ok("Completed", f"{ok}/{len(jobs)} stream sessions accepted [204 OK].")
            self.state.total_stream_hours_claimed += hours
            self.state.save()
            input(f"\n  {C.GREY}Press Enter to return to main menu...{C.RESET}")

    def refresh_auth(self) -> None:
        C = self.console
        C.banner(self.user_info, self.state)
        print(f"  {C.GREY}─────────────────── [ MODULE: CREDENTIAL SYNC ] ─────────────────{C.RESET}")
        print(f"  {C.WHITE}Update Discord token, analytics token, or auto-sync cookies.    {C.RESET}")
        print(f"  {C.GREY}─────────────────────────────────────────────────────────────────{C.RESET}\n")
        new_token = input(f"  {C.WHITE}New Discord Token (press enter to keep current): {C.RESET}").strip()
        if new_token:
            self.state.token = new_token
            self.state.analytics_token = ""
        new_ana = input(f"  {C.WHITE}New Analytics Token (press enter to keep current): {C.RESET}").strip()
        if new_ana:
            self.state.analytics_token = new_ana
        self.session = Session.new()
        self.client = ScienceClient(self.state, self.session)
        try:
            self.user_info = fetch_user_profile(self.state.token, self.session.super_props)
            self.state.analytics_token = self.user_info.get("analytics_token", self.state.analytics_token)
            fresh_cookie = auto_fetch_discord_cookies()
            if fresh_cookie:
                self.state.cookie = fresh_cookie
            self.state.save()
            C.ok("Auth", "Credentials & Cloudflare cookies auto-refreshed successfully.")
        except Exception as e:
            C.warn("Auth", f"Profile check notice: {e}")
        time.sleep(1)

    def _select_games(self, count: int) -> list[Game]:
        available_ids = {g.id for g in self.games}
        unused_ids = [g.id for g in self.games if g.id not in self.state.used_games]
        used_ids = [gid for gid in self.state.used_games if gid in available_ids]

        if len(unused_ids) >= count:
            selected_ids = unused_ids[:count]
        else:
            selected_ids = unused_ids
            if used_ids:
                rem = count - len(selected_ids)
                selected_ids.extend(used_ids[:rem])

        self.state.used_games = [gid for gid in self.state.used_games if gid not in selected_ids] + selected_ids
        id_map = {g.id: g for g in self.games}
        return [id_map[gid] for gid in selected_ids if gid in id_map]

    def launch_247_streamer(self) -> None:
        C = self.console
        C.banner(self.user_info, self.state)
        print(f"  {C.GREY}─────────────── [ MODULE: 24/7 HOSTING STREAMER ] ───────────────{C.RESET}")
        print(f"  {C.WHITE}Launching autonomous 24/7 streaming engine (main.py)...{C.RESET}")
        print(f"  {C.GREY}─────────────────────────────────────────────────────────────────{C.RESET}\n")
        try:
            main_path = ROOT / "main.py"
            if not main_path.exists():
                main_path = Path("main.py").resolve()
            subprocess.run([sys.executable, str(main_path)])
        except KeyboardInterrupt:
            pass
        except Exception as e:
            C.err("Launcher", str(e))
        input(f"\n  {C.GREY}Press Enter to return to main menu...{C.RESET}")

    def menu(self) -> None:
        C = self.console
        while True:
            C.banner(self.user_info, self.state)
            print(f"  {C.GREY}──────────────────────── [ CORE MODULES ] ────────────────────────{C.RESET}")
            print(f"  {C.WHITE}[1]{C.RESET} {C.BOLD_WHITE}Game Playtime Hours{C.RESET}   {C.GREY}Boost gameplay hours (up to 10k+ hrs){C.RESET}")
            print(f"  {C.WHITE}[2]{C.RESET} {C.BOLD_WHITE}Games Variety Library{C.RESET} {C.GREY}Register unique titles to library{C.RESET}")
            print(f"  {C.WHITE}[3]{C.RESET} {C.BOLD_WHITE}Streaming Badge Level{C.RESET} {C.GREY}Inject live stream hours & viewers{C.RESET}")
            print(f"  {C.WHITE}[4]{C.RESET} {C.BOLD_WHITE}Refresh Credentials{C.RESET}   {C.GREY}Update token / auto-fetch cookies{C.RESET}")
            print(f"  {C.WHITE}[5]{C.RESET} {C.BOLD_WHITE}24/7 Hosting Engine{C.RESET}   {C.GREY}Start autonomous streamer (main.py){C.RESET}")
            print(f"  {C.WHITE}[0]{C.RESET} {C.BOLD_WHITE}Disconnect & Exit{C.RESET}     {C.GREY}Exit application safely{C.RESET}")
            print(f"  {C.GREY}──────────────────────────────────────────────────────────────────{C.RESET}\n")

            choice = input(f"  {C.BOLD_WHITE}m9mq{C.RESET}{C.GREY}@{C.RESET}{C.WHITE}spoofer{C.RESET} {C.BOLD_WHITE}─▶{C.RESET} ").strip()
            if choice == "1":
                self.claim_playtime()
            elif choice == "2":
                self.claim_games()
            elif choice == "3":
                self.claim_stream()
            elif choice == "4":
                self.refresh_auth()
            elif choice == "5":
                self.launch_247_streamer()
            elif choice in ("0", "exit", "q"):
                print(f"\n  {C.BOLD_WHITE}[OK] Session terminated safely. Goodbye!{C.RESET}\n")
                break


def main() -> None:
    try:
        BadgeApp().start()
    except KeyboardInterrupt:
        print("\n\n  Exiting...\n")
    except Exception as e:
        print(f"\n  [ERROR] {e}\n")
    finally:
        if sys.platform == "win32" and "_boot" not in globals():
            try:
                input("\n  Press Enter to exit...")
            except Exception:
                pass


if __name__ == "__main__":
    main()
