# content_scanner


## What does it do?

This program can be used to check whether any keywords from a list you supply feature in the source code of any of the URLs that you feed it.

### Requirements

Grab a copy of this project by typing into your terminal "git clone https://github.com/Th3Blacksmith/content_scanner.git".
Fire up the terminal and type 'pip install -r requirements.txt'.
This will install any and all packages neccessary to run the script.


# Script Usage

To use this script cd into '~/content_scanner', provided you aren't already there.

You might now want to change the list of words in the keywords.txt document to suit your purpose. Put each new word on its own line.
You might also want to change the list of URL's in the files.csv file. Again, keep each url on its own line.

To run this script, simply type "python Content_Scanner_Script.py". You will be presented with a message telling you that the process has started, followed by the results and then a process complete message.

On Mac/Linux, you may be shown a permission denied message when you try to run this script. In this case, simply type 'sudo' infront of the python command. eg 'sudo python Content_Scanner_Script.py 'password'

This script will make a folder named 'screenshots' in the current working directory and update it with the screenshots it takes, label by the keyword-find that triggered it. There is a 5 second delay between the loading of each webpage to allow for the loading of the page. Feel free to adjust this to your needs by modifying the time.sleep() value on line 38 in the Content_Scanner_Script.py file.

## GUI Usage

The above instructions also hold true for the Content_Scanner_GUI.py script. The only difference here is that the Content_Scanner_GUI.py script will fire up a GUI to let browse local files for the keyword and URL files that you would like to use.