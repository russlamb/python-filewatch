import sys
from cx_Freeze import setup, Executable

setup(
    name = "pattern_watch",
    version = "0.1",
    description = "Monitor and move incoming files",
    executables = [Executable("pattern_watch.py", base = "Win32GUI")])