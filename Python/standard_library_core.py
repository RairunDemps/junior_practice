import os
import time
import sys

new_folder_name = "Test_mkdir_folder"
project_dir = os.getcwd()
print("Current folder is ", project_dir)
print(f"os.mkdir({new_folder_name})", os.mkdir(new_folder_name))
print(f"os.chdir({new_folder_name})", os.chdir(new_folder_name))
print("Current folder is ", os.getcwd())
print(f"os.chdir({project_dir})", os.chdir(project_dir))
print("Current folder is ", os.getcwd())
time.sleep(1)
print(f"os.rmdir({new_folder_name})", os.rmdir(new_folder_name))
listdir = os.listdir(project_dir)
print(f"List of files and directories {listdir}")

print("sys.version: ", sys.version)

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f"Input: {line}")
print("Exit")

sys.stdout.write("Geeks\n")

sys.stderr.write("Hello World\n")


n = len(sys.argv)
print("Total arguments passed:", n)
print("Arguments:", sys.argv)

print("List sys.path", sys.path)

print("List of modules sys.modules", sys.modules)

print("project_name references count:", sys.getrefcount(project_dir))

sys.exit("This is sys.exit() message")
