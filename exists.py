import os

folder = "practice"
if os.path.exists(folder):
    print("folder is already exist")
else :
    os.mkdir(folder)