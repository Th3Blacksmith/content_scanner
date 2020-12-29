# content_scanner


## What does it do?

This program can be used to check whether any keywords from a list you supply feature in the source code of any of the URLs that you feed it.

### Requirements

Fire up the terminal and type 'pip install -r requirements.txt'.
This will install any and all packages neccessary to run the script.


# Usage

To use this script, first cd into the directory you would like to work from or make one if you need to.
Next grab a copy of this project by typing into your terminal "git clone https://github.com/Th3Blacksmith/content_scanner.git".
You might now want to change the list of words in the keywords.txt document to suit your purpose. Put each new word on its own line.
You might also want to change the list of URL's in the files.csv file. Again, keep each url on its own line.

To run this script, simply type "python Content_Scanner_Script.py". You will be presented with a message telling you that the process has started, followed by the results and then a process complete message.

On Mac/Linux, you may be shown a permission denied message. In this case, simply type 'sudo' infront of the python command. eg 'sudo python Content_Scanner_Script.py 'password'

This script will make a folder named screenshots in the current working directory and update it with the screenshots it takes. There is a 5 second delay between the loading of each webpage to allow for the loading of the page. Feel free to adjust this to suit by modifying the time.sleep() value on line 38 in the Content_Scanner_Script.py file.
