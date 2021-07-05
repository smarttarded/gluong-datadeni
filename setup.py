import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["tkinter", "random", "sys", "subprocess", "cryptography", "shutil"],
                     "excludes": ["pygame", "pytz", "matplotlib"],
                     "include_files": ['favicon.ico','matrix.gif', "hideimg.png", "unhideimg.png", "lockimg.png", "unlockimg.png"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="gluong datadeni",
      version="2.0",
      description="hides and encrypts files from folders",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="gluong-datadeni.py", base=base, icon="favicon.ico")])
