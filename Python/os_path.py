import os

test_path = "/baz/foo"
basename = os.path.basename(test_path)
print("Basename of", test_path, "is", basename)

dirname = os.path.dirname("/baz/foo")
print("Dirname of", test_path, "is", dirname)

is_abs = os.path.isabs(test_path)
print("Path", test_path, "is absolute", is_abs)

test_path1 = "C:\\Users"
is_dir = os.path.isdir(test_path1)
print(test_path1, "is directory", is_abs)

test_path2 = "C:\\Users\\Admin\\PythonPractice\\bit_manipulations.py"
is_file = os.path.isfile(test_path2)
print(test_path2, "is file", is_file)

test_path3 = "/BAz"
normcase_path = os.path.normcase(test_path3)
print(test_path3, "normcase is", normcase_path)

test_path4 = "foo/./bar"
normpath = os.path.normpath(test_path4)
print(test_path4, "normpath is", normpath)
