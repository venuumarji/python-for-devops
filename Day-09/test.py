import os
os.chdir('../')
folders = input("Enter folder:").split()
for folder in folders:
    files = os.listdir(folder)  
    print(f"Files in folder {folder} are:---")
    for file in files:
        print(file)