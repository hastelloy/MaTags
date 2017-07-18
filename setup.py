from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

setup(
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            'bundle_files': 1, 
            'compressed': True,
                    },
                    },
    windows = [{'script': "matags.py"}]
    )