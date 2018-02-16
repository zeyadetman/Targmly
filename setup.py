from cx_Freeze import setup, Executable
from multiprocessing import Queue
import os, sys
from multiprocessing import Queue
base = 'none'
if sys.platform == 'win32':
	base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r'C:/Program Files (x86)/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'C:/Program Files (x86)/Python36-32/tcl/tk8.6'
setup(
    name = "Targmly",
    version = "1.0",
    description = '<any description>',
    options = {"build_exe": {"packages":["idna","plyer"]}},
    executables = [Executable("trans.py", base=base)]
)