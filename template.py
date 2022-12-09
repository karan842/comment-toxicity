## THIS FILE CONTAINS THE DIRECTORY STRUCTURE
## OF THE PROJECT

import os


dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    "notebooks",
    "src",
    "saved_models",
    "references",
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"),"w") as f:
        pass
    
files = [
    "dvc.yaml",
    "params.yaml",
    "README.md",
    ".gitignore",
    ".dockerfile",
    ".dockerignore"
]

for file_ in files:
    with open(file_, "w") as f:
        pass