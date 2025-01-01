import my_functions

OUTPUT_DIRECTORY = 'targets'

if __name__ == "__main__":
    url = "https://www.vasonite.com"
    target_name = "vasonite"
    
    # Generate the target report
    my_functions.target_report(url, target_name)