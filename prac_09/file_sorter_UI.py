""" program to sort files by type specified by user"""

import os
import shutil

file_type_dict = {}

def main():
    """Process all subdirectories using os.walk()."""


    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
            # Ignore directories, just process files
            if os.path.isdir(filename):
                 continue

            file_type = check_file_type(filename)
            if file_type not in file_type_dict:
                new_dir = get_dir_from_user(file_type)

                try:
                    os.mkdir(new_dir)
                except FileExistsError:
                    pass

                shutil.move(filename, new_dir + '/' + filename)
            else:
                shutil.move(filename, file_type_dict[file_type] + '/' + filename)

            print("{} moved to {}".format(filename, file_type_dict[file_type] + '/' + filename))



def check_file_type(filename):
    name_split = filename.split('.')
    return name_split[1]


def get_dir_from_user(file_type):
    new_dir = input("What directory would you like to sort {} files into?".format(file_type))
    file_type_dict.update({file_type: new_dir})
    return new_dir


main()