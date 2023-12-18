# Required Modules
import os
import re
import platform
import datetime
import shutil

# Getting Flders for arrage files
source = "/home/neeraj/Documents/Codes/Project/file-orgeniser-python/unarranged"
target = "/home/neeraj/Documents/Codes/Project/file-orgeniser-python/arranged"

# Created the list of extension for file
exts = ("jpg", "jpeg", "png", "mov", "mp4")
# Created default date pattern if pattern doesn't match it will not perform well
date_pattern = '.*(20\d\d)-?([01]\d)-?([0123]\d).*'

# listing all files present in the folder
files = os.listdir(source)

# This will get folder for files according to their month number
def get_folder(year, monthNumber):
    match monthNumber:
        case '01':
            monthFolder = '01 January'
        case '02':
            monthFolder = '02 February'
        case '03':
            monthFolder = '03 March'
        case '04':
            monthFolder = '04 April'
        case '05':
            monthFolder = '04 May'
        case '06':
            monthFolder = '06 June'
        case '07':
            monthFolder = '07 July'
        case '08':
            monthFolder = '08 August'
        case '09':
            monthFolder = '09 September'
        case '10':
            monthNumber = '10 October'
        case '11':
            monthFolder = '11 November'
        case '12':
            monthFolder = '12 December'
    
    return year + '/' + monthFolder

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
    else:
        date_created = creation_date(folder+'/'+file)
        matchObj = re.match(date_pattern,date_created)

        # If files month and year matches with the given pattern then set these variables else print the statement.
        if (matchObj):
            year = matchObj.group(1)
            month = matchObj.group(2)
        else:
            year = '0'
            month = '0'
            print("Unable to get date: "+ file)
    return {'year':year,'month':month}
        

# This loop will run for all files in that SOURCE folder
for file in files:
    if(file.lower().endswith(tuple(exts))):
        date = get_file_data(source, file)
        year = date['year']
        month = date['month']

        # If year and month has nothing
        if(year =='0' or month == '0'):
            continue;
        
        # This will get the filder by calling get_folder method.
        folder = get_folder(year,month)
        print(folder)

        # It will create target folder or we can say the collection folder for sorted files if it is not present.
        targetFolder = target+'/'+folder
        if(not os.path.exists(targetFolder)):
            os.makedirs(targetFolder)

        # It will create final target files in the targetfolder if it is not present.
        sourceFile = source +'/'+file
        targetFile = targetFolder + '/' + file
        if(not os.path.exists(targetFile)):
            shutil.move(sourceFile, targetFile)
        else:
            # It will delete that file if it is already exist.
            if (os.stat(sourceFile).st_size == os.stat(targetFile).st_size):
                print("Duplicate File, Deleting "+file)
                os.remove(sourceFile)
            else:
                print("Duplicate File, different size "+ file)