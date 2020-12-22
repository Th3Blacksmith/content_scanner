# content_scanner

This python3 script can be used a way to check whether any supplied keywords feature in the source code of any of the supplied URLs.

## What does it do?

To use this script, first cd into the directory you would like to work from.
Next grab a copy of this project by typing into your terminal "git clone https://github.com/Th3Blacksmith/content_scanner.git".
You might now want to change the list of words in the keywords.txt document to suit your purpose. Put each new word on its own line.
You might also want to change the list of URL's in the files.csv file. Again, keep each url on its own line.

### Requirements

After creating a new environment using python3 -m venv env, you will want to install all the needed requirements to run the script.
To do this, simply type in the terminal "pip install -r requirements.txt".
You will then also have to give the .py file executive permissions by typing chmod 777 content_scanner.py.


# Usage - MAC/LINUX

To run this script, simply type "sudo ./content_scanner.py". You will be presented with a message telling you that the process has started, followed by the results and then a process complete message.

# Usage - Windows (Coming Soon)...
