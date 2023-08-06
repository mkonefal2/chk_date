# chk_date
This script is used to find and sort CSV files in a given directory that contain "2023" in the file name. The script then checks the modification date of each file and compares it to the current date.

The main functions of the script:

File search: The script searches for files with the .csv extension in the given directory (the directory path is defined as "/path/to/file/") that contain "2023" in their name.

File sorting: Found files are sorted from newest to oldest based on the date they were last modified.

Checking Modified Date: For each file, the script retrieves the last modified date and compares it with the current date.

Displaying file information: For each file, the script will print its name, information whether it is up-to-date (that is, if its modification date is today's date), and the last modification date. If the file's last modified date is not today's date, the script will print a message that the file is too old.
