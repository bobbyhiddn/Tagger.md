import os
import argparse
import logging

def remove_all_front_matters(file_path):
    print(f"Processing file: {file_path}")  # print file path
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except IOError as e:
        logging.error(f"Unable to open file {file_path}: {e}")
        return

    new_lines = []
    in_front_matter = False
    for line in lines:
        stripped_line = line.strip()
        if stripped_line == "---":
            in_front_matter = not in_front_matter
            continue
        if not in_front_matter:
            new_lines.append(line)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except IOError as e:
        logging.error(f"Unable to write to file {file_path}: {e}")

def clean_markdown_files(folder_path):
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            clean_markdown_files(entry.path)
        elif entry.name.endswith('.md'):
            remove_all_front_matters(entry.path)

def main():
    parser = argparse.ArgumentParser(description='Remove front matter sections in markdown files.')
    parser.add_argument('directory', type=str, help='Directory to clean files in')
    args = parser.parse_args()
    clean_markdown_files(args.directory)

if __name__ == '__main__':
    main()