import my_functions



my_url = "https://www.vasonite.com/"

# filter the top level domain 
top_level_domain = my_functions.top_level_domain(my_url)


# get the IP Address 
ip_address = my_functions.get_ip(top_level_domain)


# get the nmap scan 
nmap_scan = my_functions.get_nmap('-F', ip_address)


print(f"output: {top_level_domain}\nIP: {str(ip_address)}")
print(nmap_scan)



