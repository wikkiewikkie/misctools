import os
import zipfile

with open("files.txt", "w", encoding="utf8") as out_file:

    files = os.listdir(".")
    
    for file_name in files:

        if file_name[-3:] == "zip":
            zip_file = zipfile.ZipFile(file_name, "r")

            for zf_name in zip_file.namelist():
                out_file.write("{}{}".format(zf_name, "\n"))
            

