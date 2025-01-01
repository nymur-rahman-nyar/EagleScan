import os 
from tld import get_tld
import urllib.request 
import io

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



## getting ip address from tld we input 
def get_ip(tld):
    '''
        The function just outputs the ip address
    '''
    command = f"dig +short {tld}" 
    process = os.popen(command)
    ip = str(process.read().strip())
    process.close()
    
    return ip


## Added nmap 
def get_nmap(option, ip):
    '''
    -F : fast scan 
    -A : Detailed 
    -O : operating system (need root privilege)
    Here, we are doing an nmap scan of the ip address
    - open / close / filtered ports
    - service idenificiation 
    - also will help us find common vulnerabilities 
    - network mapping 
    - os system detection 
    '''
    
    command = f"nmap {option} {str(ip)}"
    process = os.popen(command)
    output = str(process.read().strip())
    process.close()
    return output



# Getting robot.txt file from website
def get_robot_txt(url):
    '''
    This would help us know which sites are sensitive to the site
    '''
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    if url[-1] != '/':
        url += '/'

    try:
        req = urllib.request.urlopen(url + "robots.txt")
        data = io.TextIOWrapper(req, encoding='utf-8')  # Fixed 'encoding' typo
        final_robot = data.read()
        return final_robot
    except Exception as e:
        return f"Error fetching robots.txt: {e}"


# whois function to retrieve whois info from public directory 

def whois_data(url):
    '''
    the url should be top level domain only 
    for example. google.com and not www.google.com or any other 
    prefix or suffix
    '''
    command = "whois "+ url
    proccess = os.popen(command)
    data = proccess.read().strip()
    proccess.close()
    return data




if __name__ == "__main__":
    print(whois_data('google.com'))