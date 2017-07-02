import ntpath
import subprocess

import settings
from deco import prepare_input


@prepare_input
def convert(media):
    """Convert input to another file type."""
    for m in media:
        subprocess.call(["ffmpeg",
            "-y" if settings.destination else "-n",
            "-i",
            m,
            settings.destination + ntpath.basename(m).split(".")[0] + "." + settings.extension
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
        print "%s" % settings.destination
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

        with open(settings.destination + ntpath.basename(m) + ".txt", "wb") as text_file:
            text_file.write(metadata)


convert("./samples/foo.mkv")
get_metadata("./samples/foo.mkv")
strip_metadata("./samples/foo.png")
