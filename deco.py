import settings
from helpers import createcopy, createfolder


def prepare_input(function):
    """
    Decorator.

    Turns all input to a list and batch process.

    Makes a copy of all files, in a temp or destination dir.
    """
    def wrapper(media, *args, **kwargs):
        createfolder(settings.destination)
        createfolder(settings.temp_dir)
        # If one string instead of list, make string a list
        if type(media) is not list: media = [media]
        for m in media: m = createcopy(m)

        return function(media, *args, **kwargs)

    return wrapper
