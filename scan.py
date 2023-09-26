import os
import subprocess

def chrome_data():
    file = open(r"D:\results.txt", "w+")
    chrome_file_path = "C:\Program Files\Google\Chrome"
    
    if os.path.exists(chrome_file_path):
        output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
        file.write("Google Chrome is running the following version: \n")
        file.write(output.decode('utf-8').strip())
        #print("Google Chrome is running the following version:")
        #print(print(output.decode('utf-8').strip()))
        return True
    else:
        file.write("Goolge Chrome is not installed")
        #print("Goolge Chrome is not installed")
        return False
    file.close()
    
def firewall_data():
    print("Here is the current status of your firewall profiles:")
    subprocess.check_call('netsh advfirewall show domainprofile state')
    subprocess.check_call('netsh advfirewall show privateprofile state')
    subprocess.check_call('netsh advfirewall show publicprofile state')
    print("if any of these profiles are set to 'OFF'")



chrome_data()
firewall_data()






# print what version of chrome you have running
# print if that version is up to date
# if your version is out of date print what vulnerabilities you may be susceptible to.