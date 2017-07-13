#!/usr/bin/env python
import wx
import wx.adv

from icon import email_icon


# class CustomTaskBarIcon(wx.TaskBarIcon):
    # """"""

    # #----------------------------------------------------------------------
    # def __init__(self, frame):
    #     """Constructor"""
    #     wx.TaskBarIcon.__init__(self)
    #     self.frame = frame

    #     img = wx.Image("email-icon.png", wx.BITMAP_TYPE_ANY)
    #     bmp = wx.BitmapFromImage(img)
    #     self.icon = wx.EmptyIcon()
    #     self.icon.CopyFromBitmap(bmp)
    #     self.tbicon = wx.TaskBarIcon()
    #     self.SetIcon(self.icon, "Restore")
    #     self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)

    # #----------------------------------------------------------------------
    # def OnTaskBarActivate(self, evt):
    #     """"""
    #     pass

    # #----------------------------------------------------------------------
    # def OnTaskBarClose(self, evt):
    #     """
    #     Destroy the taskbar icon and frame from the taskbar icon itself
    #     """
    #     self.frame.Close()

    # #----------------------------------------------------------------------
    # def OnTaskBarLeftClick(self, evt):
    #     """
    #     Create the right-click menu
    #     """
    #     self.frame.Show()
    #     self.frame.Restore()

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self, parent, title=title, 
            style=style, size=(400,60))
        self.control = wx.TextCtrl(self)
        
        img = wx.Image("email-icon.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(bmp)
        self.SetIcon(email_icon.GetIcon())
        self.tbIcon = wx.adv.TaskBarIcon()
        self.tbIcon.SetIcon(email_icon.GetIcon())

        # self.Bind(wx.EVT_CLOSE, self.on_close)
        # self.Bind(wx.EVT_ICONIZE, self.on_iconify)
        self.Show(True)
        self.Centre()

    def on_iconify(self, evt):
        if self.IsIconized():
            self.Hide()
    def on_close(self, evt):
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

app = wx.App(False)
frame = MyFrame(None, 'MaTags')
app.MainLoop()