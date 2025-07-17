import os

# Create directory
os.mkdir("my_folder")  # Creates folder in current directory

# Create nested folders
os.makedirs("parent/child", exist_ok=True)

# Rename directory
os.rename("my_folder", "renamed_folder")

# Remove folder with content (use shutil)
import shutil
shutil.rmtree("parent")


print("Files in current dir:")
for file in os.listdir("."):
    print(file)


# Copy file to another folder
# shutil.copy("data.txt", "backup/data_copy.txt")

# Move file to another folder
# shutil.move("data.txt", "moved/data.txt")


# Remove a single empty directory
os.rmdir("renamed_folder")

print("Does 'backup' folder exist?", os.path.exists("backup"))
print("Is it a directory?", os.path.isdir("backup"))
print("Is it a file?", os.path.isfile("backup/data_copy.txt"))


stats = os.stat("03 Files & OS Operations/05_os_shutil.py")
print("Size:", stats.st_size, "bytes")
print("Last modified:", stats.st_mtime)