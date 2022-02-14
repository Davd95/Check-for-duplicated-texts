from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Check for duplicate texts.py", base=base)]

packages = ["os","xml.dom.minidom","__TextExtractor__", "pathlib", "shutil", "bs4"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Check for duplicate texts",
    options = options,
    version = "0.9",
    description = 'Check for duplicate texts, Version 0.9',
    executables = executables
)