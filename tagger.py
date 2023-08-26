import os
import sys

def find_last_front_matter_end(lines):
    last_end = None
    in_front_matter = False
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if stripped_line == "---":
            if in_front_matter:
                last_end = i
            in_front_matter = not in_front_matter
    return last_end

def find_tag_header(lines):
    for i, line in enumerate(lines):
        if line.strip() == "#### Tags":
            return i
    return None

def tag_file(file_path, tags):
    unique_tags = set(tags)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_tag_line = ' '.join([f"#{tag}" for tag in unique_tags if tag]) + '\n'

    last_front_matter_end = find_last_front_matter_end(lines)
    tag_header_index = find_tag_header(lines)

    if tag_header_index is not None:
        # Replace tags under "#### Tags"
        lines[tag_header_index + 1] = new_tag_line
    elif last_front_matter_end is not None:
        # Insert "#### Tags" and tags right after the last front matter
        lines.insert(last_front_matter_end + 1, "\n#### Tags\n" + new_tag_line + "\n----\n")
    else:
        # Prepend "#### Tags" and tags at the beginning of the file
        lines.insert(0, "#### Tags\n" + new_tag_line + "\n----\n")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def tag_markdown_files(folder_path, tags=[]):
    folder_name = os.path.basename(folder_path).replace(" ", "")
    current_tags = tags + [folder_name]
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            tag_markdown_files(entry.path, current_tags)
        elif entry.name.endswith('.md'):
            tag_file(entry.path, set(current_tags))

if __name__ == '__main__':
    # Take root folder as a command line argument
    root_folder = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else '.'
    tag_markdown_files(root_folder)
