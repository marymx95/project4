import sys

uniquename = b"marym"
grade = "A+"
n =  len(uniquename)


sys.stdout.buffer.write(b"marymx" +b"\x00"*4+ b"A+" )
