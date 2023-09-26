import os

def is_chrome_installed():
    # List of possible executable names for Chrome
    chrome_file_path = "C:\Program Files\Google\Chrome"
    
    if os.path.exists(chrome_file_path):
        return True
    else:
        return False
    
if is_chrome_installed():
    print("Chrome is installed on this system")
else:
    print("Chrome is not installed on this system")



# print what version of chrome you have running
# print if that version is up to date
# if your version is out of date print what vulnerabilities you may be susceptible to.