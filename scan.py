import os
import subprocess

def chrome_data():
    #file path will need to be changed to detect username and better filepath
    file = open(r"D:\results.txt", "w+")
    chrome_file_path = "C:\Program Files\Google\Chrome"
    
    if os.path.exists(chrome_file_path):
        output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
        file.write("Google Chrome is running the following version: \n")
        file.write(output.decode('utf-8').strip())
        return True
    else:
        file.write("Goolge Chrome is not installed \n")
        return False
    file.close()
    
def firewall_data():
    file = open(r"D:\results.txt", "w+")
    file.write("Here is the current status of your firewall profiles: \n")
    domain_profile = subprocess.check_call('netsh advfirewall show domainprofile state')
    file.write(str(domain_profile) + "\n")
    private_profile = str(subprocess.check_call('netsh advfirewall show privateprofile state'))
    file.write(private_profile + "\n")
    public_profile = str(subprocess.check_call('netsh advfirewall show publicprofile state'))
    file.write(public_profile + "\n")
    file.write("If any of these profiles are set to 'OFF' you may be vulnerable to an attack")
    file.write("To remidiate this __________________________________")



chrome_data()
firewall_data()






# print what version of chrome you have running
# print if that version is up to date
# if your version is out of date print what vulnerabilities you may be susceptible to.