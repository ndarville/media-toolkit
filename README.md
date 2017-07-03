README
======
The idea was originally to do a PySide project to try my hand at writing a self-contained app with a simple GUI, but turns out the PySide people haven’t bothered to update the project since [PySide stopped working on macOS Sierra][pyside-bug].

Right now, the project uses a mix of Python and Homebrew packages, the latter of which have to be installed manually by Windows users.

If I don’t packages this into an app, I’ll try to check out some wrappers for ffmpeg and exiftool so this can work as a CLI-based Python packages.

TODO
----
* Brewfile seems to ignore options
* A GUI sure would be nice
    - Failing that, CLI functionality


[pyside-bug]: https://stackoverflow.com/a/41782161
