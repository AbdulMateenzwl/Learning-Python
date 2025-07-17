from pathlib import Path

p = Path("/home/abdul/projects/")

print("Full Path:", p)
print("Parent Directory:", p.parent)   # /home/abdul/projects
print("File Name:", p.name)            # myfile.txt
print("File Stem:", p.stem)            # myfile
print("Extension:", p.suffix)          # .txt
print("Is Absolute Path:", p.is_absolute())  # True
print("Is File:", p.is_file())         # True if it exists
print("Is Directory:", p.is_dir())     # True if it exists


base = Path("/home/abdul/projects")
full = base / "python" / "main.py"  # Like os.path.join()
print(full)  # /home/abdul/projects/python/main.py


# Create directory (does not error if exists)
Path("data/logs").mkdir(parents=True, exist_ok=True)

# Create empty file
Path("data/logs/log.txt").touch()

folder = Path("")

# List all files and folders
for item in folder.iterdir():
    print("Item:", item)

# Only list .txt files
for txt in folder.glob("*.txt"):
    print("Text File:", txt)

from pathlib import Path

# Delete a file
Path("data/logs/log.txt").unlink(missing_ok=True)

# Delete an empty folder
Path("data/logs").rmdir()

# List all files in a directory
root = Path("")
for py_file in root.rglob("*.py"):
    print(py_file)
