# Python Backup (Packup) script

- Specify a source folder and destination folder
- Automatically makes a backup in the destination folder with the date appended to the zip file name
- Checks if destination folder has 3 zips, if so deletes the oldest one based on the date the backup was made

```
0 0 * * 0 /path/to/python /path/to/packup.py -s src -d dest
```
