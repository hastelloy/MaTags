import win32com.client
import pyperclip as clip

outlook = win32com.client.Dispatch("Outlook.Application")
# http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartClientCom.html
selected = outlook.ActiveExplorer().Selection
tags = set()
for item in selected:
    # print(item.Categories)
    _tags = set(item.Categories.split(', '))
    tags = tags|_tags
tags_str = ", ".join(tags)
clip.copy(tags_str)