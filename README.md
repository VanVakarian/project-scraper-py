# Project Scraper

Project Scraper is a utility for collecting the contents of files from a specified directory and saving them into a single text file. This is useful for archiving and analyzing the source code of a project.

## Usage

To use the script, run the following command:

```bash
python project-scraper.py --path <directory_path> [--output-filename <filename>] [--no-paths]
```

Parameters:

- `--path`: (required) the path to the directory from which files need to be collected.
- `--output-filename`: (optional) the name of the output file. If not specified, the root folder name will be used with `.project_src` extension.
- `--no-paths`: (optional) exclude file paths from the output text.

Example:

```bash
python project-scraper.py --path ./my_project --output-filename collected_files.project_src
```

## Settings

### FILE_EXTENSIONS_INCLUDE

The `options.py` file contains a list of file extensions to be collected:

```python
FILE_EXTENSIONS_INCLUDE = [
    '.js',
    '.ts',
    '.json',
    '.html',
    '.css',
    '.scss',
    '.py',
    '.example',
    '.md',
]
```

### DIR_NAMES_IGNORE

A list of directories to be ignored when collecting files:

```python
DIR_NAMES_IGNORE = [
    'node_modules',
    'public',
    'assets',
    '.angular',
    '.vscode',
]
```

### FILE_NAMES_IGNORE

A list of files to be ignored when collecting:

```python
FILE_NAMES_IGNORE = [
    'package-lock.json',
    'package.json',
    'tsconfig.json',
]
```
