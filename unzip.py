import zipfile
import os

for file in os.listdir('.'):
	print file
    if file.endswith(".zip"):
        name = os.path.splitext(os.path.basename(file))[0] #Split the pathname path into a pair (root, ext) 
        if not os.path.isdir(name):
            try:
                zip = zipfile.ZipFile(file)
                os.mkdir(name) # make a dir which has the same name with the ziped folder
                zip.extractall(path=name)
                zip.close()
                os.remove(file) # remove the zipped file
            except zipfile.BadZipfile, e:
                print file+ "is bad zip file."
              
