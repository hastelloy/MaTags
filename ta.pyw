import win32com.client
import pyperclip as clip
outlook = win32com.client.Dispatch("Outlook.Application")
# http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartClientCom.html
selected = outlook.ActiveExplorer().Selection
tags_str = clip.paste()
tags = set(tags_str.split(", "))
for item in selected:
    # print(item.Subject, item.To, tags_str)
    old_tags=set(item.Categories.split(', '))
    new_tags = old_tags|tags
    new_tags_str = ', '.join(new_tags)
    item.Categories = new_tags_str
    item.Save()