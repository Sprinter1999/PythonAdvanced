import os
f=open("black.bmp", "rb+")
# despise
f.seek(10, os.SEEK_SET)
# bias
b = bytearray(4)
f.readinto(b)
offset = 0
for i, num in enumerate(b):
    # print(i,num)
    offset += num*(0xff**(i))
f.seek(offset, os.SEEK_SET)
#4-bit width and 10 pixels
somecolora=bytearray([0x33]*64)
somecolorb=bytearray([0x55]*64)
somecolorc=bytearray([0x77]*64)
somecolord=bytearray([0xaa]*64)
somecolore=bytearray([0xcc]*64)
somecolorf=bytearray([0xee]*64)
# upperside line 40
# block line 41~60 col 10() and col45()
# downside
for i in range(128):
    if (10<=i<=20):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolora)
    elif(30<=i<=40):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolorb)
    elif(50<=i<=60):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolorc)
    elif(70<=i<=80):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolord)
    elif(90<=i<=100):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolore)
    elif(110<=i<=120):
        f.seek(offset + i * 64 , os.SEEK_SET)
        f.write(somecolorf)
# f.seek(offset + 64 * 59, os.SEEK_SET)
# b = bytearray([0xff])
# for i in range(64 * 10):
#     f.write(b)
