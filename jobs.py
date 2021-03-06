import ntpath
import subprocess

import settings
from deco import prepare_input


@prepare_input
def convert(media):
    """Convert input to another file type."""
    for m in media:
        subprocess.call(["ffmpeg",
            "-y" if settings.overwrite else "-n",
            "-i",
            m,
            settings.destination \
                + ntpath.basename(m).split(".")[0] + "." + settings.extension
        ])

@prepare_input
def stabilize_video(media, shakiness=5):
    """
    Stabilizes video and takes a 1-10 shakiness argument.

    Installation instructions at <git.io/vQ0SA>.
    """
    for m in media:
        # Generate `transforms.crf` analysis of video
        if shakiness < 10:
            subprocess.call(["ffmpeg",
                "-y",  # Overwrite automatically
                "-i",
                m,
                "-vf",
                "vidstabdetect=result=" \
                    + settings.temp_dir + "transforms.crf",
                "-f",
                "null",
                "-"
            ])
        else:
            subprocess.call(["ffmpeg",
                "-y",  # Overwrite automatically
                "-i",
                m,
                "-vf",
                "vidstabdetect=result=" \
                    + settings.temp_dir + "transforms.crf" \
                    + ":shakiness=" + str(shakiness) + ":accuracy=15",
                "-f",
                "null",
                "-"
            ])

        # Use `transforms.crf` to stabilize video
        subprocess.call(["ffmpeg",
            "-y",  # Overwrite automatically
            "-i",
            m,
            "-vf",
            "vidstabtransform=smoothing=30:input='" \
                + settings.temp_dir + "transforms.crf",
            settings.destination + ntpath.basename(m).split(".")[0] \
                + ".stable." + ntpath.basename(m).split(".")[1]
        ])


@prepare_input
def strip_metadata(media):
    """Strips metadata and logs remaining metadata."""
    for m in media:
        subprocess.call(["exiftool",
            "v3",  # Verbose logging
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
            "-duplicates",
            m
        ])

        with open(settings.destination + ntpath.basename(m) + ".txt", "wb") as text_file:
            text_file.write(metadata)
