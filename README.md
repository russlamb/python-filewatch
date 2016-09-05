# Pattern Watch 
## Monitor and move incoming files
### Overview
This python script will monitor a directory for files with names that match patterns specified and move to a target directory

### Default files
The default files used are:
* *pattern_file.py* - each line should be a file pattern for files that will be moved.  For example, "*.xml" for XML files or "something_*.xls" for a more specific name.
* *ignore_file.py* - each line should be a file pattern for files that will be ignored.  For example, ".git" to ignore git stuff or ".DS_Store" for mac devices.

### Other Info
If the folder you're running this code in is managed by git, there can be some funny behavior when it comes to lock files.  For this reason th default ignore_pattern.txt file includes *.lock to ignore lock files.

I tested the code using files in a separate directory.  You can pass the directory that is to be monitored ni the first argument.  

### Usage
python pattern\_watch.py *"directory_to_watch"* *"target_directory"* *pattern_file* *ignore_file*