## Packages:
+ [wxpython 4.0.0a3](http://wxpython.org/)
    `pip install wxpython`
+ [win32com](https://pypi.python.org/pypi/pywin32)
    `pip install pywin32`

## Hotkeys:
+ **Alt+e**, show dialog, extract tags
+ **Alt+a**, activate dialog, without extracting tags
+ **Alt+r**, refresh tags
+ **Esc**, minimize the dialog to system tray
+ **Enter**, 
    - add the tags, 
            e.g.:
                `TagA, TagB, TagC`
                `TagA TagB TagC`
    - set the tags with : in any place of the command 
        (existing tags will be removed)
            e.g.:
                `TagA TagB TagC:`
                `TagA: TagB TagC`
## Usages:
### append tags:
- select all the messages to be tagged in Outlook,
- **Alt+e** to extract existing tags, input the tags (seperated with space or comma) and press **Enter**
e.g. `TagA, TagB, TagC` or `TagA TagB TagC`. 
Please note existing tags will not be removed.

### set tags:
- select all the messages to be tagged in Outlook,
- **Alt+a** to activate the Matags window, 
input the tags (seperated with space or comma) and add : in any place, press **Enter**
e.g. `TagA, TagB, TagC:` or `TagA: TagB TagC`. 
Please note existing tags will be replaced with the new tags.

### refresh tags
- select the messages including both the messages already tagged and the messages to be tagged (with Ctrl or Shift) in Outlook 
- **Alt+r**, all the messages to be tagged will be refreshed with the existing tags

## To make Windows EXE
- install [py2exe](http://py2exe.org/)
- run `python setup.py py2exe`