import os
import subprocess 

def is_chrome_installed():
    chrome_file_path = "C:\Program Files\Google\Chrome\Application"
    
    if os.path.exists(chrome_file_path):
        output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
        print("Google Chrome is running the following version:")
        version = output.decode('utf-8').strip()
        revised_version = version.replace("Version=", "")
        print(revised_version)
        if(revised_version == '117.0.5938.92'):
            print("You are running the latest version of Google Chrome")
        else:
            print("You are running an outdated version of Google Chrome and you may be vulnerable")
            print("To see how to update your version of Google Chrome, follow the steps at this site: https://support.google.com/chrome/answer/95414?hl=en&co=GENIE.Platform%3DDesktop")
    else:
        print("Google Chrome is not installed \n")
        return False

def possible_vulnerabilities():
    output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
    version = output.decode('utf-8').strip()
    revised_version = version.replace("Version=", "")
    if revised_version == '117.0.5938.92':
        return True
    elif revised_version == '114.0.5735.90':
        print("Your version of Google Chrome is 4 months out of date and contains these vulnerabilities:")
        f = open('114.csv', 'r')
        print(f.read())
        f.close()
    elif revised_version == '113.0.5672.126':
        print("Your version of Google Chrome is 4 and a half months out of date and contains these vulnerabilities:")
        f = open('113.csv', 'r')
        print(f.read())
        f.close()
    elif revised_version == '112.0.5615.49':
        print("Your version of Google Chrome is 6 months out of date and contains these vulnerabilities:")
        f = open('112.csv', 'r')
        print(f.read())
        f.close()
    

is_chrome_installed()
possible_vulnerabilities()

