#!/usr/bin/env python
# -*- encoding:utf8 -*-
import wx
import wx.adv

import os
import sys



"""
Packages:
    wxpython 4.0.0a3,
    win32com

Hotkeys:
    Alt+e, show dialog, extract tags
    Alt+a, activate dialog, without extracting tags
    ---Alt+q, quit the program -- deleted..
    Esc, minimize the dialog to system tray
    Enter, 
        add the tags, 
            e.g.:
                'TagA, TagB, TagC'
                'TagA TagB TagC'
        set the tags with : in any place of the command 
        (existing tags will be removed)
            e.g.:
                'TagA TagB TagC:'
                'TagA: TagB TagC'
"""



class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        style = wx.DEFAULT_FRAME_STYLE & ~(
            wx.RESIZE_BORDER | wx.MAXIMIZE_BOX |
            wx.MINIMIZE_BOX)

        wx.Frame.__init__(self, parent, title=title, 
            style=style, size=(400,60))
        self.textbox = wx.TextCtrl(self)
        
        img = wx.Image("matags.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(bmp)
        self.SetIcon(self.icon)

        self.tbIcon = wx.adv.TaskBarIcon()
        self.tbIcon.SetIcon(self.icon)

        self.Show(True)
        self.Centre()

        self.reg_hot_keys()        
        self.Bind(wx.EVT_HOTKEY, self.on_extract_tag, 
            id=self.hotkeys['extract_tag'][0])
        # self.Bind(wx.EVT_HOTKEY, self.on_close, 
        #     id=self.hotkeys['quit'][0])
        self.Bind(wx.EVT_HOTKEY, self.on_activate, 
            id=self.hotkeys['activate'][0])
        self.textbox.Bind(wx.EVT_CHAR, self.check_key)
        # do not use EVT_KEY_DOWN, 
        # it becomes difficult to get lower case
        # self.textbox.Bind(wx.EVT_KEY_DOWN, self.check_key)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_ICONIZE, self.on_iconify)
        try:
            from matags_utils import MaTags
            self.matags = MaTags()
        except Exception as e:
            self.textbox.ChangeValue(e.args[0].decode('utf8', 'ignore'))
            self.textbox.Disable()

    def check_key(self, evt):
        """
        hotkeys:
            Alt+e, show dialog, also extract tags
            Alt+a, show dialog, without extracting tags
            ---Alt+q, quit the program -- deleted..
            Esc, minimize the dialog to system tray
            Enter, add the tags
        """
        char = evt.GetUnicodeKey()
        if char == wx.WXK_ESCAPE:
            # Esc
            self.Hide()
        elif char == wx.WXK_RETURN:
            tags_str = self.textbox.GetValue()
            if ":" in tags_str:
                tags_str = tags_str.replace(':', '')
                self.set_tags(tags_str)
            self.append_tags(tags_str)
        else:
            # self.textbox.WriteText("%c"%char)
            evt.Skip()

    def reg_hot_keys(self):
        """
        hotkeys:
            Alt+e, show dialog, also extract tags
            Alt+a, show dialog, without extracting tags
            Alt+q, quit the program
            Esc, minimize the dialog to system tray
            Enter, add the tags
        """
        self.hotkeys = {'extract_tag': (
                            wx.NewId(), wx.MOD_ALT, 0x45), # alt+e
                        'activate': (
                            wx.NewId(), wx.MOD_ALT, 0x41), # alt+a
                        # 'quit': (
                        #     wx.NewId(), wx.MOD_ALT, 0x51), # alt+q
                        }
        # https://msdn.microsoft.com/en-us/library/windows/desktop/ms646309(v=vs.85).aspx
        # https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
        for _, key in self.hotkeys.items():
            # print(_, key)
            self.RegisterHotKey(*key)

    def unreg_hot_keys(self):
        for _, key in self.hotkeys.items():
            self.UnregisterHotKey(key[0])

    def on_extract_tag(self, evt):
        """
        """
        self.Show()
        self.Iconize(False)
        self.Raise() #bring to front
        self.Centre()
        tags_str = self.matags.extract()
        self.textbox.ChangeValue(tags_str)
    
    def set_tags(self, tags_str):
        self.matags.set_tags(tags_str)

    def append_tags(self, tags_str):
        self.matags.append(tags_str)

    def on_activate(self, evt):
        self.Show()
        self.Iconize(False)
        self.Raise() #bring to front
        self.Centre()

    def on_iconify(self, evt):
        if self.IsIconized():
            self.Hide()

    def on_close(self, evt):
        self.unreg_hot_keys()
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        print("closing...")
        self.Destroy()

app = wx.App(False)
frame = MyFrame(None, 'MaTags')
app.MainLoop()