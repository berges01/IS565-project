import os
import subprocess 

def chrome_data():
    chrome_file_path = "C:\Program Files\Google\Chrome"
    
    if os.path.exists(chrome_file_path):
        output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',shell=True)
        print("Google Chrome is running the following version: \n")
        print(output.decode('utf-8').strip())
        return True
    else:
        print("Goolge Chrome is not installed \n")