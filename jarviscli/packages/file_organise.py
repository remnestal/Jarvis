from __future__ import print_function
from colorama import Fore
import os
import six


def source_path(dir_name):
    all_paths = []
    # Changing static path to get the home path from PATH variables.
    # The '/home' was causing script to exit with "file not found" error
    # on Darwin.
    home_dir = os.environ.get("HOME")
    user_name = os.environ.get("USER")
    home_path = home_dir.split(user_name)[0].rstrip('/')
    for root in os.walk(home_path):
        print(Fore.LIGHTBLUE_EX + "Searching in {}...".format((root[0])[:70]), end="\r")
        sys.stdout.flush()
        if dir_name == root[0].split('/')[-1]:
            all_paths.append(root[0])

    for i, path_info in enumerate(all_paths):
        print()
        print("{}. {}".format(i + 1, path_info))

    if len(all_paths) == 0:
        print(Fore.LIGHTRED_EX + 'No directory found')
        exit()

    if six.PY2:
        choice = int(raw_input('\nEnter the option number: '))
    else:
        choice = int(input('\nEnter the option number: '))

    if choice < 1 or choice > len(all_paths):
        path = ''
        print(Fore.LIGHTRED_EX + 'Wrong choice entered')
        exit()

    else:
        path = all_paths[choice - 1]

    return path


def print_before(path):
    print("Cleaning {} located at {}\n".format(path.split('/')[-1], path))

    print(Fore.LIGHTBLUE_EX + "Folders before cleaning\n" + Fore.RESET)

    for files in os.listdir(path):
        print(files, end='\t')
    print()


def destination_path(path):
    os.chdir(path)
    extension = set()
    for f in os.listdir(path):
        ext = (os.path.splitext(f))[1]

        extension.add(ext[1:])

    new_dir = "New" + path.split('/')[-1]
    new_dir_path = os.path.join(path, new_dir)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)

    return new_dir_path, new_dir, extension

def organise(new_dir_path, new_dir, path, extension):
    branch = set()
    _organise(new_dir_path, new_dir, path, extension, branch)
    with open('organise@file_organise.py.branch', 'a') as branch_file:
        branch_file.write('total: %s\n' % str(11))
        branch_file.write('activated: %s\n' % str(len(branch)))
        branch_file.write('set: %s\n' % str(branch))
        branch_file.write('--------------\n')

def _organise(new_dir_path, new_dir, path, extension, branch):
    for ext in extension:
        branch.add(82)
        folder = os.path.join(new_dir_path, ext)

        if not os.path.exists(folder):
            branch.add(86)
            os.mkdir(folder)

        if ext != '':
            branch.add(90)
            for f in os.listdir(path):
                branch.add(92)
                if os.path.splitext(f)[1].strip('.') == ext:
                    branch.add(94)
                    os.rename(f, os.path.join(folder, f))

        else:
            branch.add(98)
            for f in os.listdir(path):
                branch.add(100)
                if f != new_dir and os.path.splitext(f)[1].strip('.') == ext:
                    branch.add(102)
                    inner_folder = os.path.join(new_dir_path, f)

                    if os.path.exists(inner_folder):
                        branch.add(106)
                        os.chdir(os.path.join(path, f))
                        for file in os.listdir():
                            branch.add(109)
                            new_path = os.path.join(inner_folder, file)
                            os.rename(file, new_path)
                        os.rmdir(os.path.join(path, f))

                    else:
                        branch.add(115)
                        os.rename(f, inner_folder)


def print_after(path):
    print(Fore.LIGHTBLUE_EX + "\nFolders after cleaning\n" + Fore.RESET)

    for files in os.listdir(path):
        print(files, sep=',\t')

    print(Fore.LIGHTMAGENTA_EX + "\nCLEANED\n" + Fore.RESET)


def file_manage(self):
    if six.PY2:
        dir_name = raw_input('Enter the name of directory you want to clear: ')
    else:
        dir_name = input('Enter the name of directory you want to clear: ')
    dir_path = source_path(dir_name)
    print_before(dir_path)
    new_dir_path, new_dir, extension = destination_path(dir_path)
    organise(new_dir_path, new_dir, dir_path, extension)
    print_after(dir_path)
