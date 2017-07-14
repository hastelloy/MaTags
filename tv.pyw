import win32com.client
import pyperclip as clip
outlook = win32com.client.Dispatch("Outlook.Application")
# http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartClientCom.html
selected = outlook.ActiveExplorer().Selection
tags_str = clip.paste()
for item in selected:
    # print(item.Subject, item.To, tags_str)
    item.Categories = tags_str
    item.Save()