import cx_Freeze
import os
import sys
base = None

if sys.platform == 'win32':
    base = "win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\\Users\\Bilal\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\\Users\\Bilal\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Mpad Text Editor",
    options = {"build_exe": {"packages":['tkinter', "os"], "include_files":["icon.ico", 'tcl86t.dll', 'tk86t.dll', 'icons2']}},
    version = "0.1",
    description = "It is a simple text editor made by rey programmer.",
    executables = executables,
)
