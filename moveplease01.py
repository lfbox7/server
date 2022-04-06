#!/usr/bin/env python3

"""
Alta3 Research | LFBox
Moving and Renaming Files and Folders
"""

# import external modules
import shutil
import os

def main():
    """
    code to manipulate files and folders
    """

    # move to working directory
    os.chdir('/home/student/mycode/')

    # move file to new directory
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # rename file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


# calling main()
if __name__ == '__main__':
    main()
