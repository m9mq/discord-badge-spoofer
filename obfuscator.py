#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════════════════
        M9MQ HYPER-SHIELD CODE PROTECTOR & OBFUSCATION ENGINE v4.0
═══════════════════════════════════════════════════════════════════════════════
  Author: m9mq
  All Rights Reserved (C) 2026 m9mq
  Protects Python source with 6-stage cryptographic transformation:
  1. Dynamic 256-byte S-Box Substitution
  2. Circular 5-bit permutation & dynamic SHA-512 round keys
  3. CBC Running Block Cipher Feedback
  4. Dual-pass Level 9 Zlib Deflate Compression
  5. Base85 Byte Armor
  6. Anti-Debugger + Anti-Hooking + Anti-Dump Memory Sanitization
═══════════════════════════════════════════════════════════════════════════════
"""

import base64
import hashlib
import hmac
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def build_protected_release(source_code: str, author: str = "m9mq") -> str:
    salt = "m9mq_hyper_shield_crypto_2026_x86_arm_v4"
    derived_key = hashlib.sha512((author + salt).encode("utf-8")).digest()
    key_len = len(derived_key)

    # 1. Build Dynamic S-Box (256-byte substitution table)
    sbox = bytearray(range(256))
    j = 0
    for i in range(256):
        j = (j + sbox[i] + derived_key[i % key_len]) & 0xFF
        sbox[i], sbox[j] = sbox[j], sbox[i]

    # 2. Layer 1: Compress source text with level 9
    c1 = zlib.compress(source_code.encode("utf-8"), level=9)

    # 3. Layer 2: S-Box Substitution
    sub = bytearray(sbox[b] for b in c1)

    # 4. Layer 3: Bit-rotation & Dynamic Keystream XOR
    rot = bytearray()
    for i, b in enumerate(sub):
        k = derived_key[i % key_len]
        r = ((b << 5) & 0xFF) | (b >> 3)
        rot.append(r ^ k ^ ((i * 17) & 0xFF))

    # 5. Layer 4: CBC Running Feedback Cipher
    cbc = bytearray()
    prev = 0x5A
    for b in rot:
        out_b = b ^ prev
        cbc.append(out_b)
        prev = out_b

    # 6. Layer 5: Secondary Zlib Compression
    c2 = zlib.compress(bytes(cbc), level=9)

    # 7. Layer 6: Base85 Encoding
    b85_payload = base64.b85encode(c2).decode("ascii")

    # Format chunks
    chunk_size = 92
    chunks = [b85_payload[i:i + chunk_size] for i in range(0, len(b85_payload), chunk_size)]
    formatted_payload = "\n    ".join(f'"{c}"' for c in chunks)

    # HMAC integrity signature
    integrity_sig = hmac.new(derived_key, author.encode("utf-8"), hashlib.sha256).hexdigest()

    loader = f'''# -*- coding: utf-8 -*-
# ==============================================================================
#  ███╗   ███╗   ██████╗   ███╗   ███╗   ██████╗ 
#  ████╗ ████║  ██╔═████╗  ████╗ ████║  ██╔═══██╗
#  ██╔████╔██║  ██║██╔██║  ██╔████╔██║  ██║   ██║
#  ██║╚██╔╝██║  ████╔╝██║  ██║╚██╔╝██║  ██║▄▄ ██║
#  ██║ ╚═╝ ██║  ╚██████╔╝  ██║ ╚═╝ ██║  ╚██████╔╝
#  ╚═╝     ╚═╝   ╚═════╝   ╚═╝     ╚═╝   ╚══▀▀═╝ 
# ==============================================================================
#  DISCORD BADGE ENGINE v4.0 · OFFICIAL PROTECTED RELEASE
#  ENCRYPTED & COMPILED BY m9mq SECURITY CORE (C) 2026 m9mq
#  ALL RIGHTS RESERVED · PROPRIETARY TELEMETRY SUITE
#  UNAUTHORIZED MODIFICATION, DEOBFUSCATION OR REBRANDING WILL CRASH EXECUTION
# ==============================================================================

import sys as _0x01
import base64 as _0x02
import zlib as _0x03
import hashlib as _0x04
import hmac as _0x05

_AUTHOR = "{author}"
_SIG = "{integrity_sig}"
_SALT = "{salt}"

def _0x_shield():
    # Anti-Debugger & Anti-Tracer
    if getattr(_0x01, "gettrace", lambda: None)() is not None:
        _0x01.exit(0)
    # Anti-Hook Verification on core execution primitives
    _b = getattr(__builtins__, "__dict__", __builtins__)
    for _fn in ("compile", "exec"):
        _f = _b.get(_fn) if isinstance(_b, dict) else getattr(_b, _fn, None)
        if _f is not None and getattr(_f, "__class__", None).__name__ != "builtin_function_or_method":
            _0x01.exit(0)

_0x_shield()

_0x_raw_key = _0x04.sha512((_AUTHOR + _SALT).encode("utf-8")).digest()
if _0x05.new(_0x_raw_key, _AUTHOR.encode("utf-8"), _0x04.sha256).hexdigest() != _SIG:
    print("\\n  \\x1b[38;2;239;68;68m[FATAL] Integrity verification failed. Unauthorized tampering detected.\\x1b[0m\\n")
    _0x01.exit(1)

_0x_payload = (
    {formatted_payload}
)

def _boot():
    _0x_shield()
    try:
        _k_len = len(_0x_raw_key)
        # S-Box Inversion
        _sb = bytearray(range(256))
        _j = 0
        for _i in range(256):
            _j = (_j + _sb[_i] + _0x_raw_key[_i % _k_len]) & 0xFF
            _sb[_i], _sb[_j] = _sb[_j], _sb[_i]
        _inv_sb = bytearray(256)
        for _i in range(256):
            _inv_sb[_sb[_i]] = _i

        # Layer 1: Base85 + Zlib Decompress
        _d1 = _0x02.b85decode(_0x_payload.encode("ascii"))
        _d_cbc = bytearray(_0x03.decompress(_d1))

        # Layer 2: Inverse CBC feedback
        _d_rot = bytearray()
        _prev = 0x5A
        for _b in _d_cbc:
            _orig_b = _b ^ _prev
            _d_rot.append(_orig_b)
            _prev = _b

        # Layer 3: Inverse Bit-rotation & Keystream
        _d_sub = bytearray()
        for _i, _b in enumerate(_d_rot):
            _k = _0x_raw_key[_i % _k_len]
            _r = _b ^ _k ^ ((_i * 17) & 0xFF)
            _orig = ((_r >> 5) | (_r << 3)) & 0xFF
            _d_sub.append(_orig)

        # Layer 4: Inverse S-Box
        _d_c1 = bytearray(_inv_sb[_b] for _b in _d_sub)

        # Layer 5: Final Decompression
        _raw_src = _0x03.decompress(bytes(_d_c1)).decode("utf-8")
        _code = compile(_raw_src, "<m9mq_core_engine>", "exec")

        # Memory Sanitization
        _d1 = None
        _d_cbc.clear()
        _d_rot.clear()
        _d_sub.clear()
        _d_c1.clear()
        del _raw_src
    except Exception as _e:
        print(f"\\n  \\x1b[38;2;239;68;68m[FATAL] Decryption error: {{_e}}\\x1b[0m\\n")
        _0x01.exit(1)

    try:
        exec(_code, globals(), globals())
    except KeyboardInterrupt:
        pass
    except Exception as _e:
        print(f"\\n  [ERROR] {{_e}}\\n")
    finally:
        if _0x01.platform == "win32":
            try:
                input("\\n  Press Enter to exit...")
            except Exception:
                pass

if __name__ == "__main__":
    _boot()
'''
    return loader


def run():
    source_file = ROOT / "spoofer_source.py"
    if not source_file.exists():
        source_file = ROOT / "spoofer.py"

    print(f"[*] Reading source code from {source_file.name}...")
    source_code = source_file.read_text(encoding="utf-8")

    print("[*] Encrypting with m9mq Hyper-Shield (S-Box + Permutation + CBC + Dual Zlib + Base85 + Anti-Tamper)...")
    protected_code = build_protected_release(source_code, author="m9mq")

    # Output to spoofer.py in ROOT
    out_1 = ROOT / "spoofer.py"
    out_1.write_text(protected_code, encoding="utf-8")
    print(f"[+] Output compiled & encrypted -> {out_1.name}")

    # Output to subfolder if exists
    sub = ROOT / "discord-badge-spoofer-main"
    if sub.exists() and sub.is_dir():
        out_2 = sub / "spoofer.py"
        out_2.write_text(protected_code, encoding="utf-8")
        (sub / "spoofer_source.py").write_text(source_code, encoding="utf-8")
        print(f"[+] Synchronized to {sub.name}/spoofer.py")

    print("[✔] Protected release built successfully with exclusive rights for m9mq!")


if __name__ == "__main__":
    run()
