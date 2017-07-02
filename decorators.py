import ntpath
import os
import shutil
import subprocess


settings = {
    "delete_temp": False, # Checkbox
    # Consider abs path instead of relative
    "destination": "./output/", # String/dir
    "extension": "mp4", # String
    "overwrite": True, # Checkbox or radio button
    "temp_dir": "./temp/" # String/dir
}


def createcopy(filename, temp=False):
    """
    Copies a file and returns a path to the top.

    Automatically overwrites.
    """
    newfilename = shutil.copy(filename, settings["temp_dir"])

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


def prepare_input(function):
    """
    Decorator.

    Turns all input to a list and batch process.

    Makes a copy of all files, in a temp or destination dir.
    """
    def wrapper(media):
        createfolder(settings["destination"])
        createfolder(settings["temp_dir"])
        # If one string instead of list, make string a list
        if type(media) is not list: media = [media]
        for m in media: m = createcopy(m)

        return function(media)

    return wrapper


@prepare_input
def convert(media):
    """Convert input to another file type."""
    for m in media:
        subprocess.call(["ffmpeg",
            "-y" if settings["destination"] else "-n",
            "-i",
            m,
            settings["destination"] + ntpath.basename(m).split(".")[0] + "." + settings["extension"]
        ])


@prepare_input
def strip_metadata(media):
    """Strips metadata and logs remaining metadata."""
    for m in media:
        subprocess.call(["exiftool",
            "v3",
            "-all:all=",
            m
        ])

        print "\nThe remaining metadata has been saved to"
        print "%s" % settings["destination"]
        get_metadata(m)


@prepare_input
def get_metadata(media):
    """
    Logs media metadata.

    Takes list as input for uniformity's sake. Will always loop once.
    """
    for m in media:
        metadata = subprocess.check_output(["exiftool",
            "-a",
            m
        ])

        with open(settings["destination"] + ntpath.basename(m) + ".txt", "wb") as text_file:
            text_file.write(metadata)


convert("./foo.mkv")
get_metadata("./samples/foo.mkv")
strip_metadata("./samples/foo.png")
