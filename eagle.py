import my_functions
import os 
from tld import get_tld


my_url = 'https://www.google.com/'

top_level_domain = my_functions.top_level_domain(my_url)
print("\n Output: ")
print(top_level_domain)