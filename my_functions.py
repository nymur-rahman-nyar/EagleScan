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
def top_level_domain(unfiltered_domain):
    top_level_dom = get_tld(unfiltered_domain)
    return top_level_dom