import os 
from tld import get_tld

## creating directory function 
def create_directory(directory):
    if not os.path.exist(directory):
        os.makedirs(directory)




## function to write data in files 
def write_file (path, data):
    with open(path, "w") as file:
        file.write(data)




## getting the top level domain 
def top_level_domain(url):
    my_tld = get_tld(url, as_object=True)
    return my_tld.fld