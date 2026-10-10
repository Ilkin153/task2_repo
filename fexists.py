import os

file_name = input("Fayl adi daxil edin...")

if os.path.isfile(file_name):
    print("file is already exist")
else :
    print("file is not exist")