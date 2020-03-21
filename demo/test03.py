# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=u"batch change file name",
                          pos=wx.DefaultPosition,
                          size=wx.Size(500, 300),
                          style=wx.CAPTION | wx.CLOSE_BOX
                          | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 75, 90, 90, False,
                    "@Microsoft YaHei UI Light"))
        self.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_dirPicker2 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString,
                                             u"Select a folder",
                                             wx.DefaultPosition,
                                             wx.DefaultSize,
                                             wx.DIRP_DEFAULT_STYLE)
        self.m_dirPicker2.SetFont(wx.Font(9, 74, 90, 92, False, "微软雅黑"))

        bSizer4.Add(self.m_dirPicker2, 1, wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"change file name",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button4, 0, wx.ALL, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_dirPicker2.Bind(wx.EVT_DIRPICKER_CHANGED, self.dirChangeHandler)
        self.m_button4.Bind(wx.EVT_BUTTON, self.btnClickHandler)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def dirChangeHandler(self, event):
        self.dir = event.GetPath()

    def btnClickHandler(self, event):
        print(os.listdir(self.dir))
        n = 1
        for f in os.listdir(self.dir):
            oldname = self.dir + '\\' + f
            newname = self.dir + '\\{}.'.format(n) + f.split('.')[1] + ''
            os.rename(oldname, newname)
            n += 1
            print(oldname, '======>', newname)
        print('ok')


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
