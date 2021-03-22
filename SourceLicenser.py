import os, fnmatch
import shutil
from distutils.dir_util import copy_tree

src_directory_location = ""
license_location = ""
file_patterns = ["*.c", "*.h", "*.cpp", "*.hpp", "*.cs", ".java"]

def prepend_license_to_files(src_directory_location, license_location):

    license_f = open(license_location, 'r')
    license_content = license_f.read()
    commented_license_content = apply_c_style_inline_comments(license_content)

    for path, dirs, files in os.walk(os.path.abspath(src_directory_location)):
        for i in file_patterns:
            for filename in fnmatch.filter(files, i):
                filepath = os.path.join(path, filename)
                with open(filepath) as f:
                    src_content = f.read()
                with open(filepath, "w") as f:
                    f.seek(0, 0)
                    f.write(commented_license_content + '\n' + src_content)


def apply_c_style_inline_comments(license_content):
    commented_license_content = "// "
    
    for i in range(0, len(license_content), 1):
        commented_license_content += license_content[i]
        if license_content[i] == "\n":
            commented_license_content += "// "

    commented_license_content += "\n"
    
    return commented_license_content

def main():
    src_directory_location = input("Enter the src directory path: ")
    license_location = input("Enter the license filepath: ")
    
    print("Backing up '" + src_directory_location + "' ...")
    if (os.path.exists(src_directory_location + "_backup")):
        copy_tree(src_directory_location, src_directory_location + "_alt_backup")
    else:
        copy_tree(src_directory_location, src_directory_location + "_backup")
    prepend_license_to_files(src_directory_location, license_location)
    
    print("Done.\n")
    input("Press any key to exit.")

if __name__ == "__main__":
    main()
