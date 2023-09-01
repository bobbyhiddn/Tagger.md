import os
import argparse

def remove_old_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except IOError as e:
        print(f"Unable to open file {file_path}: {e}")
        return

    in_old_tags_section = False
    new_lines = []
    for line in lines:
        if line.strip() == "#### Tags":
            in_old_tags_section = True
        elif line.strip() == "----":
            in_old_tags_section = False
        elif not in_old_tags_section:
            new_lines.append(line)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except IOError as e:
        print(f"Unable to write to file {file_path}: {e}")

def remove_old_tags_from_files(folder_path):
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            remove_old_tags_from_files(entry.path)
        elif entry.name.endswith('.md'):
            remove_old_tags(entry.path)

def main():
    parser = argparse.ArgumentParser(description='Remove old tags headers from markdown files.')
    parser.add_argument('directory', type=str, help='Directory to remove old tags headers from')
    args = parser.parse_args()
    remove_old_tags_from_files(args.directory)

if __name__ == '__main__':
    main()