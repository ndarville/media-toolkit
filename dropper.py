"""
Drag and drop files to have a prepare_input script run on them.

1. Drag file(s) to app
2. Save file names to list
3. Display files by name with [X] to cancel
4. RUN button
    - Do the loop in Python, not shell script
    - Add QtGui.QProgressBar and add checkmark for finished files
5. Settings below

* Progress bar
"""
import sys

from PySide import QtGui, QtCore

import jobs


app = QtGui.QApplication(sys.argv)

mainwindow = QtGui.QWidget()
mainwindow.resize(550, 400)
mainwindow.setWindowTitle("Hello world")
mainwindow.setWindowIcon(QtGui.QIcon("./samples/foo.png"))
mainwindow.show()

# Drag drop

# File list with add/remove and checkmark

startbutton = QtGui.QPushButton("Start")
startbutton.clicked.connect(jobs.convert("./samples/foo.mkv"))
startbutton.show()

# Progress bar

# Settings

app.exec_()
