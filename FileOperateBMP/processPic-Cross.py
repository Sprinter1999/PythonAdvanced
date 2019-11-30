import os
#Process bmp header
f=open("black.bmp", "rb+")
# despise
f.seek(10, os.SEEK_SET)
# bias
b = bytearray(4)
f.readinto(b)
print(f.tell())
offset = 0
for i, num in enumerate(b):
    print(i,num)
    offset += num*(0xff**(i))
    print(offset)
f.seek(offset, os.SEEK_SET)
print(f.tell())
# just draw
#4-bit width and 10 pixels
whiteblock = bytearray([0x0f, 0xff, 0xff, 0xff, 0xff,0xf0])
somecolor=bytearray([0xAA]*64)
for i in range(128):
    f.seek(offset + i * 64 + 29, os.SEEK_SET)
    f.write(whiteblock)
f.seek(offset + 64 * 59, os.SEEK_SET)
print(f.tell())
block = bytearray([0xff])
for i in range(64 * 10):
    f.write(block)