import hashlib
import os
path=input("Escribe el nombre del archivo: ")
file_obj=open(path,"rb")
file=file_obj.read()

Hash=hashlib.sha512(file)
hashed=Hash.hexdigest()
print(hashed)
f=open("Hash.txt","a")
f.write("File:"+path+" Hash:")
f.write(str(hashed))
f.write("\n")
f.close()
