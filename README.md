# s3-tree

Print an S3 bucket as a hierarchical tree.

# Runtime Dependencies

`tree` (brew install tree)

Python > 3.9

# Installation

```make setup.env``` to create the dev virtual environment and install dev dependencies.

Alternatively, clone this repo and install it  ```pip install .``` This will also install the `s3-tree` command as a console entry-point.

Or directly install it from GitHub: ```python -m pip install \"s3-tree @ git+https://git@github.com/selimonat/s3-tree.git" ```

# Usage

```
$ python s3-tree --help

Usage: s3-tree [OPTIONS] PROFILE_NAME BUCKET_NAME PREFIX [MAX_DEPTH]
               [SHOW_FILES] [MAX_FILES_TO_SHOW] [VERBOSE]

  Prints all files in a S3 bucket as a tree.

Arguments:
  PROFILE_NAME         AWS profile name  [required]
  BUCKET_NAME          Bucket name  [required]
  PREFIX               Prefix to filter  [required]
  [MAX_DEPTH]          Max depth to traverse  [default: 3]
  [SHOW_FILES]         Show files or not  [default: False]
  [MAX_FILES_TO_SHOW]  If show, how many files to show  [default: 10]
  [VERBOSE]            Verbose or not  [default: False]
```

# Example

```python s3-tree TENANT_NAME MY_BUCKET PREFIX/```

to get:
```
PREFIX/
    ├── Folder 1
    │         ├── subfolder1
    │         │         ├── subfolder X
    │         │         └── subfolder Y
    │         ├── subfolder2
    │         └── subfolder3
    ├── Folder 2
   ...
```