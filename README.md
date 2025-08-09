# CSV Consolidate

Tool for Windows users (that should just learn Unix and use AWK) to consolidate several same-schema CSV files.

The tool consists of a Python3 CLI application with a little GUI app that allows you to select a directory that has ONLY the CSV files in it that you want to consolidate. Using the app, you pick this directory and the tool grabs everything in it that has a file name ending in `.csv`, reads those, and dumps their data into a consolidated CSV file that it writes to your Documents directory with the current datetime of when it was processed as part of the file name.

For example, you will select the directory `monthly_data_files_copy` (or whatever) in the directory picker and the tool will grab all the \*.csv files and create something like `/Users/cwkingjr/Documents/csv_consolidated_20250809_094601.csv`.

Advice, always use copies of your data when dealing with tools you get off some wanker on the internet, and two, rename the consolidated CSV file once you check it to ensure it's what you want so when you come back to it or share it, you can tell what data is really in it. For example, `all_tickets_2024Q3_2025Q2.csv`.

## Just Use Git Bash and AWK :-)

You can consolidate CSV files on Windows via the Git Bash Terminal using awk:

```bash
>awk '(NR == 1) || (FNR > 1)' monthly_report_*.csv > monthly_combined.csv
```

## Install UV

- Install uv on your host machine: https://docs.astral.sh/uv/getting-started/installation/

- If you already have uv, update it:

```bash
uv self update
```

## Install CSV Consolidate

```bash
uv tool install https://github.com/cwkingjr/csv-consolidate.git
```

This downloads the repository info, builds the package into a python virtual environment (isolated for this tool only), and installs what's called an entrypoint. An entrypoint basically is just a program name that is loaded into your system path so that you can call the entrypoint from anywhere on your computer and your system will find it and go to the right place to start the program. Entrypoints on different operating systems can use differnt names.

On Linux, the entrypoint for this tool is `csv_consolidate` and on Windows it's `csv_consolidate.exe`.

## Invoke CSV Consolidate

On Linux, open any terminal and run:

```bash
csv_consolidate
```

On Windows, open PS or the Git Bash Terminal and run:

```bash
csv_consolidate.exe
```

## Output

When you run CSV Consolidate you will get the consolidated file in your Documents folder but will also get some terminal output that will tell you the directory you selected, give a print out of a collapsed text version of the consilidated file contents (basically so you can see that it worked and what some of the headers were), and tell you where your file was written and what the name is.

## Uninstall CSV Consolidate

Using one of the terminals mentioned above, run the below command. Pay attention to the dash in the name because here we are uninstalling the entire project and above, where we used the underscore in the name, we were calling the entrypoint (the entrypoint named csv_consolidate or csv_consolidate.exe just calls into the program/project called csv-consolidate so be careful with the names).

```bash
uv tool uninstall csv-consolidate
```
