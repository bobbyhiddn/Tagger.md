import os
import argparse
import logging
import yaml

def find_front_matter(lines):
    front_matter = []
    in_front_matter = False
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if stripped_line == "---":
            if in_front_matter:  # end of front matter
                return front_matter, i
            else:  # start of front matter
                in_front_matter = True
        elif in_front_matter:
            front_matter.append(line)
    return None, 0

def tag_file(file_path, tags):
    print(f"Processing file: {file_path}")  # print file path
    unique_tags = set(tags)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except IOError as e:
        logging.error(f"Unable to open file {file_path}: {e}")
        return

    front_matter, front_matter_end_line = find_front_matter(lines)
    if front_matter is not None:
        try:
            front_matter_yaml = yaml.safe_load("\n".join(front_matter))
        except yaml.YAMLError as e:
            logging.error(f"Unable to parse front matter in file {file_path}: {e}")
            return
        if not isinstance(front_matter_yaml, dict):
            front_matter_yaml = {}
        if 'tags' in front_matter_yaml:
            existing_tags = set(front_matter_yaml['tags'])
            unique_tags |= existing_tags  # merge existing tags with unique_tags
            front_matter_yaml['tags'] = list(unique_tags)  # convert back to list
        else:
            front_matter_yaml['tags'] = list(unique_tags)
        new_front_matter = yaml.safe_dump(front_matter_yaml)
        lines = lines[front_matter_end_line+1:]  # remove old front matter
    else:
        # If no front matter, create a new one
        front_matter_yaml = {'tags': list(unique_tags)}
        new_front_matter = yaml.safe_dump(front_matter_yaml)
    lines.insert(0, "---\n" + new_front_matter + "---\n")  # insert new front matter

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except IOError as e:
        logging.error(f"Unable to write to file {file_path}: {e}")
        
def tag_markdown_files(folder_path, tags=[]):
    root_folder_name = os.path.basename(os.path.abspath(folder_path)).replace(" ", "")
    current_tags = tags + [root_folder_name]
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            tag_markdown_files(entry.path, current_tags)
        elif entry.name.endswith('.md'):
            tag_file(entry.path, set(current_tags))

def main():
    parser = argparse.ArgumentParser(description='Tag markdown files.')
    parser.add_argument('directory', type=str, help='Directory to tag files in')
    parser.add_argument('--tags', nargs='+', help='Additional tags to add to files')
    args = parser.parse_args()
    tag_markdown_files(args.directory, args.tags if args.tags else [])

if __name__ == '__main__':
    main()