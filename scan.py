import os

def is_chrome_installed():
    # List of possible executable names for Chrome
    chrome_file_path = "C:\Program Files\Google\Chrome"
    
    if os.path.exists(chrome_file_path):
        print("Google Chrome is installed on your system.")
    else:
        print("Google Chrome is not installed on your system.")



# print what version of chrome you have running
# print if that version is up to date
# if your version is out of date print what vulnerabilities you may be susceptible to.