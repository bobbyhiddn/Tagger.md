# Tagger.md
## Markdown Folder File Tagger

## Overview

The Markdown File Tagger is a Python script designed to automatically tag Markdown files based on their folder structure. It scans through a given folder tree and appends tags to the top of each Markdown file. These tags are generated from the names of the folders that contain the file.

## Features

- **Automatic Tagging**: The script automatically generates tags based on folder names.
- **Front Matter Support**: The script detects existing front matter sections and places the tags appropriately.
- **Idempotent**: Running the script multiple times on the same folder will not duplicate tags.
- **Customizable**: Easy to adapt and extend for more specialized tagging needs.

## Requirements

- Python 3.x

## Usage

### Basic Usage

Run the script from the command line and pass in the root folder you'd like to start tagging from:

```bash
python tagger.py /path/to/root/folder
```

This will recursively go through all the Markdown files in that folder and its subfolders, appending or updating a tag section to each.

### Example 1

For a directory tree like:

Test
└── test.md


The `test.md` file will get a tag `#Test` appended to the top.

### Example 2

For a more complex directory tree like:

Test
└── Testing
├── test.md
└── testing.md

Both `test.md` and `testing.md` will get tags `#Test #Testing` appended to the top like this: 

```markdown

#### Tags
#Testing #Test

----


```

### Advanced Usage

Feel free to modify the script to suit your specific needs. The script is structured in a modular way, making it easy to adapt for more specialized tagging logic.

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make your changes, and create a pull request.

## License

This project is open-source and available under the MIT License.
