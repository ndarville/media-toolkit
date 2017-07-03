Installation
============
You will need the following for the media toolkit to work:

* ffmpeg with (at least) libvidstab
* exiftool

The project currently works on the latest version of both Windows 10 and macOS, but you’ll have to manually install `ffmpeg` and `exiftool` without the help of Homebrew on Windows. It’s just a matte of downloading thw two yourself, moving them to a destination like `C:\` and adding them to your PATH environment variable.

macOS
-----

```sh
$ brew bundle --file=dependencies/Brewfile
```

If you already have ffmpeg installed, you may want to `brew uninstall ffmpeg` and re-install it using the above method to make sure you get `libvidstab`.

I’ve included all the ffmpeg options that might be useful to you, but strictly speaking, you should only need `--with-libstab`.
