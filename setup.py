from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

Mydata_files = [('', ['MaTags.png'])]

setup(
    data_files = Mydata_files,
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            # 'icon_resources':[(1, 'matags.png')],
            'bundle_files': 1, 
            'compressed': True,
                    },
                    },
    windows = [{'script': "matags.py"}]
    )