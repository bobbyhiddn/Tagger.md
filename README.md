# Tagger.md
## Markdown Folder File Tagger

## Overview

The Markdown File Tagger is a Python script designed to automatically tag Markdown files based on their folder structure. It scans through a given folder tree and appends tags to the front matter of each Markdown file. These tags are generated from the names of the folders that contain the file.

## Features

- **Automatic Tagging**: The script automatically generates tags based on folder names.
- **Front Matter Support**: The script detects existing front matter sections and places the tags appropriately. If a file doesn't have front matter, the script will create it and add the tags.
- **Idempotent**: Running the script multiple times on the same folder will not duplicate tags.
- **Markdown Files Only**: The script will only process markdown files, which should prevent errors when running it on directories containing other types of files.
- **Customizable**: Easy to adapt and extend for more specialized tagging needs.

## Requirements

- Python 3.x

## Usage

### Basic Usage

Run the script from the command line and pass in the root folder you'd like to start tagging from:

```bash
tagger_md /path/to/root/folder
```

This will recursively go through all the Markdown files in that folder and its subfolders, appending or updating a tag section to each.

### Example 1

For a directory tree like:

```css
Test
└── test.md
```

The test.md file will get a tag Test added to its front matter like this: 

```yaml
---
tags:
  - Test
---
```

### Example 2

For a more complex directory tree like:

```css
Test
└── Test_1
    ├── test.md
```

The test.md file will get tags Test and Test_1 added to its front matter like this:  

```yaml
---
tags:
  - Test
  - Test_1
---
```

### Advanced Usage

You can also specify additional tags to be added to all files:

```bash
tagger_md /path/to/root/folder tag1 tag2
```

This will add 'tag1' and 'tag2' to all files, in addition to the directory-based tags.

### Apologies 

For those who used the first version and want to switch over, I wrote a script called cleanup.py. It will remove the #### Tags section from all files in a directory tree. It's not pretty, but it works. Here is the usage:

```bash
python cleanup.py /path/to/root/folder
```