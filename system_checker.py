import os
import subprocess, sys

def is_chrome_installed():
    chrome_file_path = "C:\Program Files\Google\Chrome\Application"
    #Check if chrome is installed and grab version
    if os.path.exists(chrome_file_path):
        output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
        print("Google Chrome is running the following version:")
        version = output.decode('utf-8').strip()
        revised_version = version.replace("Version=", "")
        print(revised_version)
        if(revised_version[:3] == '117' or revised_version[:3] == '118'):
            print("You are running the latest version of Google Chrome")
        else:
            print("You are running an outdated version of Google Chrome and you may be vulnerable")
            print("To see how to update your version of Google Chrome, follow the steps at this site: https://support.google.com/chrome/answer/95414?hl=en&co=GENIE.Platform%3DDesktop")
    else:
        print("Google Chrome is not installed \n")
        return False

def possible_vulnerabilities():
    #Check if chrome is installed and grab version
    output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
    version = output.decode('utf-8').strip()
    revised_version = version.replace("Version=", "")
    if(revised_version[:3] == '117' or revised_version[:3] == '118'):
        return True
    
    #Classifications of versions and their vulnerabilities
    elif revised_version[:3] == '116' or revised_version[:3] == '115':
        print("Your version of Google Chrome is out of data and may contain vulnerabilites")
    elif revised_version[:3] == '114':
        print("Your version of Google Chrome is 4 months out of date and contains these vulnerabilities:")
        f = open('114.csv', 'r')
        print(f.read())
        f.close()
    elif revised_version[:3] == '113':
        print("Your version of Google Chrome is 4 and a half months out of date and contains these vulnerabilities:")
        f = open('113.csv', 'r')
        print(f.read())
        f.close()
    elif revised_version[:3] == '112':
        print("Your version of Google Chrome is 6 months out of date and contains these vulnerabilities:")
        f = open('112.csv', 'r')
        print(f.read())
        f.close()

def windows_defender_status():
    # Define the PowerShell command you want to execute
    powershell_command = "Get-MpComputerStatus"

    try:
        # Run the PowerShell command
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True, check=True)

        # Check the output
        if result.returncode == 0:
            # The command was successful
            print("PowerShell Command Output:")
            print(result.stdout)
        else:
            # There was an error
            print("Error executing PowerShell command:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def windows_update():
    p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\windows-update.ps1"], 
              stdout=sys.stdout)
    p.communicate()
    print("To update your Windows Operating System, open Settings and click Windows Update on the left")

def windows_firewall():
    p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\windows-firewall.ps1"], 
              stdout=sys.stdout)
    p.communicate()


# main menu and functions
menu_input = "str"
while not menu_input in ("exit"):
    menu_input = input("Input the function you would like to run from the list \n1) chrome-vulnerabilities \n2) windows-defender \n3) windows-update \n4) windows-firewall \n5) help \n")
    if menu_input == "chrome-vulnerabilities" or str(menu_input) == '1':
        is_chrome_installed()
        possible_vulnerabilities()

    elif menu_input == "windows-defender" or str(menu_input) == '2':
        windows_defender_status()

    elif menu_input == "windows-update" or str(menu_input) == '3':
        windows_update()

    elif menu_input == "windows-firewall" or str(menu_input) == '4':
        windows_firewall()

    elif menu_input == "help" or str(menu_input) == '5':
        print("The chrome-vunlerabilities function will tell you if chrome is running on your machine. It will also tell you what version you are running. If your version is out of date it will tell you what vulnerabilities you are susceptible to.")
        print("The windows-defender function will tell you the various statistics of the anti-malware running on your device")
        print("The windows-firewall functionw will tell you status of the various firewall profiles on your device")
        print("type 'chrome-vulnerabilites' or 'windows-defender' or 'windows-update' or 'windows-firewall' and hit enter")
        menu_input = "str"

    elif menu_input == "exit":
        print("exiting program")

    else:
        print("please enter one of the menu options")
