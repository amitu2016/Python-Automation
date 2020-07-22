import os


f = open("sample","a")
f.write("This is written using Python")
f.close()
#print(f.read())
os.remove("sample")