import os
import shutil

source_directory = input("Enter a file location: ")
files = os.listdir(source_directory)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(source_directory + '/' + extension):
        shutil.copyfile(source_directory + '/' + file, source_directory + '/' + extension + '/' + filename)
    else:
        os.makedirs(source_directory + '/' + extension)
        shutil.copyfile(source_directory + '/' + file, source_directory + '/' + extension + '/' + filename)