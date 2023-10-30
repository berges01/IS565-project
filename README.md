# IS565-project
This repo is a project for IS 565 Digital Forensics and Incident Response. Our code can be run on any python capable machine and checks if your machine is following best security practices.

Group Members: Erik Berges, Jo Windley, Jake Hadley

## Documentation V - 1.0

### How it works
- First the code checks if the file path where Google Chrome is installed exists
- Then a command is run that will determine what version of chrome is running
- If you version of chrome is 117 it will let you know if your application is up to date
- If your version of chrome is 115-116 you will be alerted that your application is out of date and instructions will be provided on how to update chrome
- If your version of chrome is 112-114 you will be alerted that your application is out of date, instructions will be provided on how to update chrome, and a list of your current vulnerabilites will be provided

### Proof of Value
The provided image includes the results of the scan being run locally on a machine. The results inform the user of the version of Chrome they are currently using and provides a link that allows them to update to the newest version.

![Locally Ran Scan](img/scan-ran-locally-on-machine.png)

Further down in the results it provides a list of known vulnerabilities with that version of Chrome. It gives details about each of the vulnerabilities to help inform the user of the risks they are facing by continuing to run that version of Chrome.

## Documentation Version 1.1 - New Features

### How It Works

- The new features include a menu at the beginning when using the tool so users can choose a function or ask for help.
    - chrome-vulnerabilities
    - windows-defender
    - help
    
- After giving an input to the menu the tool will...

- This will give an output displaying ....

- The new function will then display if your built-in antivrus is working and if has detected any malicious activity.

### Proof of Value

The following images with their descriptions are the new features and updates in action using the security check Chrome extension.

Added a menu so users can choose the old chrome function, the new function, or ask for help.

![Menu](img/menu.png)

Here is the menu when giving an input.

![Input on Menu](img/menu-and-beginning-on-input.png)

Here is the result with the output.

![Output](img/result-of-output.png)

The new function will tell you if your built-in antivrus is working and if has detected any malicious activity.

![Locally Ran Scan](img/scan-ran-locally-on-machine.png)
