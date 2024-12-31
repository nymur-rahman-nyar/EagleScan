import os 

## creating directory function 
def create_directory(directory):
    if not os.path.exist(directory):
        os.makedirs(directory)

## function to write data in files 
def write_file (path, data):
    with open(path, "w") as file:
        file.write(data)
    