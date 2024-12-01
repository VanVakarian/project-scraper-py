import os
import argparse
import locale
import time
from options import FILE_EXTENSIONS_INCLUDE, DIR_NAMES_IGNORE, FILE_NAMES_IGNORE
locale.setlocale(locale.LC_ALL, '')


def collect_files(directory, include_paths):
    collected_text = ""
    file_count = 0

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in DIR_NAMES_IGNORE]

        for file in files:
            if file in FILE_NAMES_IGNORE:
                continue
            if any(file.endswith(ext) for ext in FILE_EXTENSIONS_INCLUDE):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                with open(file_path, 'r', encoding='utf-8') as f:
                    if include_paths:
                        collected_text += f"==== /{relative_path} \n\n\n"
                    collected_text += f.read()
                    collected_text += f"\n\n\n\n\n"
                file_count += 1
                print(f"\r{file_count:n} files processed", end='')

    print()
    return collected_text


def save_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    num_lines = len(text.splitlines())
    num_chars = len(text)
    return num_lines, num_chars


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Collect and save files content.')
    parser.add_argument('--path', required=True, help='Path to the directory to collect files from')
    parser.add_argument('--output-filename', required=False, help='Name of the output file (optional)')
    parser.add_argument('--no-paths', action='store_true', help='Exclude file paths from the output text')
    args = parser.parse_args()

    directory = args.path
    if directory == './':
        directory = os.getcwd()
    root_folder_name = os.path.basename(os.path.abspath(directory))
    output_file = args.output_filename if args.output_filename else f"{root_folder_name}.project_src"
    include_paths = not args.no_paths

    collected_text = collect_files(directory, include_paths)
    num_lines, num_chars = save_to_file(collected_text, output_file)

    execution_time = time.time() - start_time
    print(f"Done, {num_lines:n} lines and {num_chars:n} characters scraped into {output_file} (execution time: {execution_time:.2f} seconds)")


if __name__ == "__main__":
    main()
