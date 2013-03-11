import shutil
import os

'''
create 26 directories
loop through all the files in original_files directory and organize each of those files into 
the directory that their name starts with.
Example:
    The file named 'artichoke.txt' would go into the directory 'a',
    'bartholomew.txt' would go into 'b'.
Concepts required:
    * for loops
    * conditionals
    * lists
    * paths
    * substrings
'''

# get a list of all the files

# for each file name, move the file into the directory that corresponds to the first 
# letter of the file name

def moveFiles(src,dst):
	shutil.move(src,dst)

for file in os.listdir('original_files'):
    first_letter = file[0]

    src = 'original_files/' + file
    dst = first_letter + '/'
    newpath = dst + '/' + file
    
    if os.path.exists(newpath):
        continue
    else:
        if os.path.exists(first_letter):
            moveFiles(src,dst)
        else: 
            os.mkdir(first_letter)
            moveFiles(src,dst)
       


