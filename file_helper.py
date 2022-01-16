import os, sys
import shutil


try:
    # Gets the home path
    home = os.path.expanduser('~')
    source_dir = rf"{home}\Downloads"
    destination_dir = rf"{home}\Documents\{sys.argv[1]}"

    try:
        shutil.copytree(source_dir, destination_dir)
    except FileExistsError:
        print('File already exists!')
    except OSError:
        print("Illegal Filename Character!")
except IndexError:
    print("Command Requires a Filepath Argument!")



