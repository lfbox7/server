#!/usr/bin/env python3

"""
AAlta3 Research | LFBox
Pushing files around using shutil and os from the standard library
"""

# import external modules
import shutil
import os


def main():
    """
    code to move and duplicate files
    """

    # start in this directory
    os.chdir("/home/student/mycode/")

    # make a copy of a file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # create new folder with the same content as original folder
    shutil.copytree("5g_research/", "5g_research_backup/")

    # copy directory to new directory
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

# calling main()
if __name__ == '__main__':
    main()
