"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        print("File or Directory already exist")
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ''
    name_dict = {}
    filename = filename.replace(" ", "").replace(".TXT", ".txt")
    for index, char in enumerate(filename):
        name_dict.update({index:char})
    for index, char in name_dict.items():
        if index == 0:
            new_name = char
        if index >= 1:
            if name_dict[index].isupper() and name_dict[index-1].islower:
                if name_dict[index-1] == '(':
                    new_name += char
                else:
                    new_name += '_' + char
            else:
                new_name += char


    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            # Ignore directories, just process files
             if os.path.isdir(filename):
                 continue

             new_name = get_fixed_filename(filename)
             print("Renaming {} to {}".format(filename, new_name))


            # Option 1: rename file to new name - in place
             #os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


# main()
demo_walk()