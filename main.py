# Required Modules
import os
import re
import platform
import datetime

# Getting Flders for arrage files
source = "/home/neeraj/Documents/Codes/Project/file-orgeniser-python/unarranged"
target = "/home/neeraj/Documents/Codes/Project/file-orgeniser-python/arranged"

# Created the list of extension for file
exts = ("jpg", "jpeg", "png", "mov", "mp4")
# Created default date pattern if pattern doesn't match it will not perform well
date_pattern = '.*(20\d\d)-?([01]\d)-?([0123]\d).*'

# listing all files present in the folder
files = os.listdir(source)

# This function for creation date if file name doesnot have date pattern
def creation_date(path_to_file):
    # Try to get data that a file was created. falling back to when it was
    # last modified if that isn't possible
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Getting file data(month and year)
def get_file_data(folder, file):
    matchObj = re.match(date_pattern,file)
    if(matchObj):
        year = matchObj.group(1)
        month = matchObj.group(2)
        print(year)
        print(month)
    else:
        date_created = creation_date(folder+'/'+file)
        matchObj = re.match(date_pattern,date_created)
        year = matchObj.group(1)
        month = matchObj.group(2)
        print(year)
        print(month)
        

for file in files:
    if(file.lower().endswith(tuple(exts))):
        get_file_data(source, file)