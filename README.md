# File Organiser Script python

This project is a Python script designed to automatically organize files based on their creation month and year, and save them into a structured "super folder" for safekeeping. The script categorizes the items into folders named by year, with subfolders for each month.

## Features
- **Automatic File Organization**: The script scans a specified directory and moves files into subdirectories named by year and month of creation.
- **Flexible File Type Handling**: By default, the script supports a variety of file extensions including **jpg**, **jpeg**, **png**, **mov**, **mp4**, **mp3**, **txt**, **docx**, **rar**, and **pdf**. Additional file types can easily be added by editing the code.
- **Modern Python Syntax**: Utilizes Python 3.10's match case statements, offering a clean and intuitive way to handle different file extensions without needing **break** statements.

## Technologies Used
**Python 3.10**: The core programming language used for the script, leveraging new features such as **match case** statements for improved code clarity and efficiency.

## Usage
1. **Configure the Script:** Edit the script to specify the directory you want to organize and any additional file extensions you want to include.
2. **Run the Script:**
```bash
  python file_organizer.py
```
3. **Check the Super Folder:** After running the script, navigate to the specified "super folder" to see your files neatly organized into year and month subdirectories.
