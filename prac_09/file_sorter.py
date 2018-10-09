""" program to sort files by type"""

import os
import shutil

def main():
    """Process all subdirectories using os.walk()."""

    file_type_dirs = []

    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            # Ignore directories, just process files
            if os.path.isdir(filename):
                 continue

            file_type = check_file_type(filename)
            if file_type in file_type_dirs:
                shutil.move(filename, file_type + '/' + filename)
            else:
                os.mkdir(file_type)
                file_type_dirs.append(file_type)
                shutil.move(filename, file_type + '/' + filename)

            print("{} moved to {}".format(filename, file_type + '/' + filename))


def check_file_type(filename):
    name_split = filename.split('.')
    return name_split[1]




main()