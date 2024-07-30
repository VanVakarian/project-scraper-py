# Project Scraper

Project Scraper is a utility for collecting the contents of files from a specified directory and saving them into a single text file. This is useful for archiving and analyzing the source code of a project.

## Usage

To use the script, run the following command:

```bash
python project-scraper.py --path <directory_path> [--output-filename <filename>]
```

Parameters:

- `--path`: (required) the path to the directory from which files need to be collected.
- `--output-filename`: (optional) the name of the output file. If not specified, the root folder name will be used with a `.txt` extension.

Example:

```bash
python project-scraper.py --path ./my_project --output-filename collected_files.txt
```

## Settings

### extensions

The `options.py` file contains a list of file extensions to be collected:

```python
extensions = [
    '.js',
    '.ts',
]
```

### ignore_dirs

A list of directories to be ignored when collecting files:

```python
ignore_dirs = [
    'node_modules',
    'public',
]
```

### ignore_files

A list of files to be ignored when collecting:

```python
ignore_files = [
    'package-lock.json',
    'package.json',
]
```
