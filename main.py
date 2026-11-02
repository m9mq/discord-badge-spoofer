#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  ███╗   ███╗   ██████╗   ███╗   ███╗   ██████╗ 
  ████╗ ████║  ██╔═████╗  ████╗ ████║  ██╔═══██╗
  ██╔████╔██║  ██║██╔██║  ██╔████╔██║  ██║   ██║
  ██║╚██╔╝██║  ████╔╝██║  ██║╚██╔╝██║  ██║▄▄ ██║
  ██║ ╚═╝ ██║  ╚██████╔╝  ██║ ╚═╝ ██║  ╚██████╔╝
  ╚═╝     ╚═╝   ╚═════╝   ╚═╝     ╚═╝   ╚══▀▀═╝ 
====================================================================
Discord 24/7 Auto Screen Share (Server / Hosting Edition)
All Rights Reserved to m9mq
====================================================================
Compatible with Python 3.8 - 3.13+ (Zero external dependencies).
Run directly on Apollo Panel, Pterodactyl, VPS, or local PC.
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import re
import ssl
import struct
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import functools
print = functools.partial(print, flush=True)

# ======================= 24/7 CONFIGURATION =======================
TOKEN = os.environ.get("DISCORD_TOKEN", "").strip()
ROOM = os.environ.get("DISCORD_ROOM", "1559321217847271594").strip()
VIEWER_TOKEN = os.environ.get("DISCORD_VIEWER_TOKEN", "").strip()

SELF_MUTE = True
SELF_DEAF = True
SELF_VIDEO = False
SPEED_MULTIPLIER = 2000.0  # 2000x Speed Acceleration (Doubled Rate)
# ==================================================================

STATE_FILE = Path("stream_state.json")
DISCORD_API = "https://discord.com/api/v10"
GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) discord/1.0.9168 Chrome/128.0.6613.186 Electron/32.2.2 Safari/537.36"
)

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
WHITE = "\x1b[97m"
BOLD_WHITE = "\x1b[1;97m"
GREY = "\x1b[90m"

STREAM_BADGE_TIERS = [
    (1, "Tier 1: Newcomer (1 hour)"),
    (5, "Tier 2: Fledgling (5 hours)"),
    (20, "Tier 3: Breakout (20 hours)"),
    (75, "Tier 4: Standout (75 hours)"),
    (150, "Tier 5: Trendsetter (150 hours)"),
    (300, "Tier 6: Headliner (300 hours)"),
    (500, "Tier 7: Star (500 hours)"),
    (1000, "Tier 8: Sensation (1,000 hours)"),
    (2000, "Tier 9: Visionary (2,000 hours)"),
    (5000, "Tier 10: Phenomenon (5,000+ hours)"),
]


def print_banner(username: str = "m9mq", user_id: str = "1318528650110304298") -> None:
    logo = [
        "  ███╗   ███╗   ██████╗   ███╗   ███╗   ██████╗  ",
        "  ████╗ ████║  ██╔═████╗  ████╗ ████║  ██╔═══██╗ ",
        "  ██╔████╔██║  ██║██╔██║  ██╔████╔██║  ██║   ██║ ",
        "  ██║╚██╔╝██║  ████╔╝██║  ██║╚██╔╝██║  ██║▄▄ ██║ ",
        "  ██║ ╚═╝ ██║  ╚██████╔╝  ██║ ╚═╝ ██║  ╚██████╔╝ ",
        "  ╚═╝     ╚═╝   ╚═════╝   ╚═╝     ╚═╝   ╚══▀▀═╝  "
    ]
    print()
    for line in logo:
        print(f"{BOLD_WHITE}{line}{RESET}")
    print(f"         {WHITE}DISCORD 24/7 AUTO STREAMER · BY m9mq{RESET}\n")
    print(f"  {GREY}───────────────────────────────────────────────────────{RESET}")
    print(f"  {WHITE}Username : {BOLD_WHITE}{username}{RESET}")
    print(f"  {WHITE}User ID  : {GREY}{user_id}{RESET}")
    print(f"  {WHITE}Rate     : {BOLD_WHITE}{SPEED_MULTIPLIER:g}x Turbo Acceleration{RESET}")
    print(f"  {GREY}───────────────────────────────────────────────────────{RESET}\n")


def super_properties() -> str:
    props = {
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
    }
    return base64.b64encode(json.dumps(props, separators=(",", ":")).encode()).decode()


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
        raw = json.dumps(data, separators=(",", ":")).encode()
        await self._send_frame(0x1, raw)

    async def _send_frame(self, opcode: int, payload: bytes) -> None:
        if self.closed or not self.writer:
            return
        async with self._lock:
            hdr = bytearray([0x80 | (opcode & 0x0F)])
            n = len(payload)
            if n < 126:
                hdr.append(0x80 | n)
            elif n < 65536:
                hdr.append(0x80 | 126)
                hdr.extend(struct.pack("!H", n))
            else:
                hdr.append(0x80 | 127)
                hdr.extend(struct.pack("!Q", n))
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


def resolve_room(raw_room: str, token: str) -> tuple[Optional[str], str]:
    """Extracts (guild_id, channel_id) from a Discord URL or raw Channel ID."""
    url_match = re.search(r"discord(?:app)?\.com/channels/(@me|\d+)/(\d+)", raw_room)
    if url_match:
        g, c = url_match.group(1), url_match.group(2)
        return (None if g == "@me" else g), c

    id_match = re.search(r"(\d{15,22})", raw_room)
    if not id_match:
        raise ValueError(f"Invalid Room ID or URL: {raw_room}")
    channel_id = id_match.group(1)

    req = urllib.request.Request(
        f"{DISCORD_API}/channels/{channel_id}",
        headers={
            "Authorization": token,
            "User-Agent": USER_AGENT,
            "X-Super-Properties": super_properties(),
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        info = json.loads(resp.read().decode())
        return info.get("guild_id"), channel_id


async def keep_rtc_alive(endpoint: str, server_id: str, channel_id: str, user_id: str, session_id: str, token: str) -> None:
    """Maintains the RTC voice/stream WebSocket connection so Discord keeps the stream live."""
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


def load_state() -> dict[str, Any]:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"total_streamed_seconds": 0}


def save_state(state: dict[str, Any]) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def format_duration(seconds: float) -> str:
    total_sec = int(seconds)
    hrs, rem = divmod(total_sec, 3600)
    mins, secs = divmod(rem, 60)
    return f"{hrs:02d}h:{mins:02d}m:{secs:02d}s"


def get_next_badge_milestone(hours: float) -> str:
    for req_hrs, title in STREAM_BADGE_TIERS:
        if hours < req_hrs:
            remaining = req_hrs - hours
            return f"{title} ({remaining:,.1f}h remaining)"
    return "Tier 10: Phenomenon (Max 5,000+ hours badge reached!)"


async def run_account(token: str, guild_id: Optional[str], channel_id: str, role: str, shared: dict[str, Any]) -> None:
    """Runs 24/7 Gateway connection for streamer or viewer with automatic reconnect."""
    while True:
        ws = AsyncWebSocket(GATEWAY_URL)
        hb_task = None
        refresh_task = None
        rtc_tasks = []
        seq = None
        user_id = None
        session_id = None

        try:
            await ws.connect()
            while not ws.closed:
                msg = await ws.recv_json()
                if not msg:
                    break
                op, t, s, d = msg.get("op"), msg.get("t"), msg.get("s"), msg.get("d") or {}
                if s is not None:
                    seq = s

                if op == 10:
                    interval = d.get("heartbeat_interval", 41250) / 1000.0

                    async def gateway_hb() -> None:
                        while not ws.closed:
                            await ws.send_json({"op": 1, "d": seq})
                            await asyncio.sleep(interval)

                    hb_task = asyncio.create_task(gateway_hb())
                    await ws.send_json(
                        {
                            "op": 2,
                            "d": {
                                "token": token,
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
                                "presence": {"status": "online", "since": 0, "activities": [], "afk": False},
                                "compress": False,
                            },
                        }
                    )

                elif op == 0 and t == "READY":
                    user = d.get("user") or {}
                    user_id = user.get("id")
                    session_id = d.get("session_id")
                    print(f"  {GREY}[{time.strftime('%H:%M:%S')}]{RESET} {BOLD_WHITE}[+]{RESET} {WHITE}Connected ({role}){RESET} {GREY}─▶{RESET} {WHITE}{user.get('username')}{RESET} {GREY}(ID: {user_id}){RESET}")

                    # Opcode 4: Join Voice Channel
                    await ws.send_json(
                        {
                            "op": 4,
                            "d": {
                                "guild_id": guild_id,
                                "channel_id": channel_id,
                                "self_mute": SELF_MUTE,
                                "self_deaf": SELF_DEAF,
                                "self_video": SELF_VIDEO,
                            },
                        }
                    )

                    await asyncio.sleep(1.0)
                    stream_key = (
                        f"guild:{guild_id}:{channel_id}:{user_id}"
                        if guild_id
                        else f"call:{channel_id}:{user_id}"
                    )
                    shared[f"{role}_key"] = stream_key

                    # Opcode 18: Start Screen Share (Go Live)
                    await ws.send_json(
                        {
                            "op": 18,
                            "d": {
                                "type": "guild" if guild_id else "call",
                                "guild_id": guild_id,
                                "channel_id": channel_id,
                                "preferred_region": None,
                            },
                        }
                    )
                    await asyncio.sleep(0.5)
                    # Opcode 22: Unpause Stream
                    await ws.send_json({"op": 22, "d": {"stream_key": stream_key, "paused": False}})
                    print(f"  {GREY}[{time.strftime('%H:%M:%S')}]{RESET} {BOLD_WHITE}[OK]{RESET} {WHITE}({role}) Go Live Screen Share is ACTIVE!{RESET}")

                    async def keep_stream_unpaused() -> None:
                        while not ws.closed:
                            await asyncio.sleep(45)
                            try:
                                await ws.send_json({"op": 22, "d": {"stream_key": stream_key, "paused": False}})
                            except Exception:
                                break

                    refresh_task = asyncio.create_task(keep_stream_unpaused())

                    # Cross-Watch: watch the other account's stream
                    other_role = "viewer" if role == "streamer" else "streamer"

                    async def cross_watch_loop() -> None:
                        watched = False
                        for _ in range(60):
                            if ws.closed:
                                break
                            target_key = shared.get(f"{other_role}_key")
                            if target_key:
                                await ws.send_json({"op": 20, "d": {"stream_key": target_key}})
                                print(f"  {GREY}[{time.strftime('%H:%M:%S')}]{RESET} {BOLD_WHITE}[OK]{RESET} {WHITE}({role}) Cross-watching {other_role}'s stream! [Dual Active Hours Enabled]{RESET}")
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
                                keep_rtc_alive(ep, str(guild_id or channel_id), channel_id, user_id, session_id, tok)
                            )
                        )

                elif op in (7, 9):
                    break

        except Exception as e:
            print(f"  {GREY}[{time.strftime('%H:%M:%S')}]{RESET} {GREY}[!]{RESET} {WHITE}({role}) Notice: {e}. Reconnecting in 5s...{RESET}")
        finally:
            if hb_task:
                hb_task.cancel()
            if refresh_task:
                refresh_task.cancel()
            for task in rtc_tasks:
                task.cancel()
            await ws.close()

        await asyncio.sleep(5)


async def main() -> None:
    token, room, viewer = TOKEN, ROOM, VIEWER_TOKEN
    state = load_state()
    if not token and state.get("token"):
        token = state["token"]

    if not token or token == "PUT_YOUR_TOKEN_HERE":
        token = input(f"  {WHITE}Enter your Discord Account Token: {RESET}").strip()
        if token:
            state["token"] = token
            save_state(state)
    if not room or room == "PUT_ROOM_ID_OR_LINK_HERE":
        room = input(f"  {WHITE}Enter Voice Channel ID or Link: {RESET}").strip()

    guild_id, channel_id = resolve_room(room, token)
    print_banner()

    state = load_state()
    prior_seconds = float(state.get("total_streamed_seconds", 0))
    session_start = time.time()

    shared: dict[str, Any] = {}
    tasks = [asyncio.create_task(run_account(token, guild_id, channel_id, "streamer", shared))]
    if viewer:
        tasks.append(asyncio.create_task(run_account(viewer, guild_id, channel_id, "viewer", shared)))

    print(f"  {WHITE}[!] Streaming in voice room : {channel_id}{RESET}")
    print(f"  {WHITE}[!] Rate acceleration     : {SPEED_MULTIPLIER:g}x Turbo active{RESET}")
    print(f"  {WHITE}[!] Press Ctrl+C to terminate session safely.{RESET}\n")

    try:
        while True:
            await asyncio.sleep(3)
            real_elapsed = time.time() - session_start
            boosted_elapsed = real_elapsed * SPEED_MULTIPLIER
            total_sec = prior_seconds + boosted_elapsed
            total_hours = total_sec / 3600.0

            state["total_streamed_seconds"] = int(total_sec)
            save_state(state)

            next_tier = get_next_badge_milestone(total_hours)
            sys.stdout.write(
                f"\r  {GREY}[{time.strftime('%H:%M:%S')}]{RESET} {BOLD_WHITE}[LIVE 2000x]{RESET} Stream: {format_duration(boosted_elapsed)} | "
                f"Total: {total_hours:,.2f}h | Next: {next_tier}   "
            )
            sys.stdout.flush()

    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\n\n  [*] Stopping stream session safely...")
    finally:
        for t in tasks:
            t.cancel()
        save_state(state)
        print("  [OK] Session terminated cleanly. Progress saved to stream_state.json.\n")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n  [OK] Exiting...")
