import os
import zipfile

size = 0

files = os.listdir(".")

for file_name in files:

    if file_name[-3:] == "zip":
        zip_file = zipfile.ZipFile(file_name, "r")

        for zf in zip_file.infolist():
            size += zf.file_size

print(size/1024/1024/1024)
