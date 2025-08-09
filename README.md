# CSV Consolidate
WIP: Tool for Windows users (that should just learn Unix and use AWK) to consolidate several same-schema CSV files.

You can consolidate CSV files on Windows via the Git Bash Terminal using awk:
```
>awk '(NR == 1) || (FNR > 1)' monthly_report_*.csv > monthly_combined.csv
```
My intention for this tool is to create a python CLI app that also uses NiceGUI to grab the directory name, consolidate all the CSV files in it, and write the consolidated CSV file to the user's Documents directory.

We'll see if I can make that happen.

For now, this is an incomplete project.
