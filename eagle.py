import my_functions



my_url = "https://www.vasonite.com/"

top_level_domain = my_functions.top_level_domain(my_url)

ip_address = my_functions.get_ip(top_level_domain)


print(f"output: {top_level_domain}\nIP: {str(ip_address)}")