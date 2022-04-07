import os
import sys

f = open(sys.argv[1], "rb")
o = open(sys.argv[2], "wb")

data = f.read()
for d in data:
    o.write("" + chr (ord(d) ^ 0x2a))

f.close()
o.close()