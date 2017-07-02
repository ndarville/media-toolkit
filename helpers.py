import os, shutil

import settings


def createcopy(filename):
    """
    Copies a file and returns a path to the top.

    Automatically overwrites.
    """
    newfilename = shutil.copy(filename, settings.temp_dir)

    return newfilename


def createfolder(dir):
    """
    Creates a folder if it doesn't exist.

    Handles 2.7 race condition cf. stackoverflow.com/a/14364249.
    """
    try:
        os.makedirs(dir)
    except OSError:
        if not os.path.isdir(dir): raise
