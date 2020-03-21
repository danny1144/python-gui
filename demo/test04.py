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
import urllib
from bs4 import BeautifulSoup as bs
###########################################################################
## Class MyFrame
###########################################################################


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=u"蜂鸟网图片批量下载(佳能影像专区)",
                          pos=wx.DefaultPosition,
                          size=wx.Size(531, 143),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"请输入下载的网址：",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)
        bSizer7.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                    5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_textCtrl1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"0",
                                           wx.DefaultPosition, wx.Size(30, 30),
                                           wx.ALIGN_CENTRE | wx.SUNKEN_BORDER)
        self.m_staticText1.Wrap(-1)
        bSizer8.Add(self.m_staticText1, 0,
                    wx.ALIGN_RIGHT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer8.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer6.Add(bSizer8, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer6)
        self.Layout()
        self.Centre(wx.BOTH)
        self.n = len(os.listdir(u'C:/Users/root/Pictures/猎豹安全浏览器截图'))
        self.m_staticText1.SetLabel(str(self.n))
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.on_save)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_save(self, event):
        url = self.m_textCtrl1.GetValue()
        request = urllib.urlopen(url).read()
        html = bs(request, 'html.parser')
        div_list = html.find_all('div', class_='img')
        for div in div_list:
            a = div.find('a')
            img = a.find('img')
            src = img.get('src').split('?')[0]
            urllib.urlretrieve(
                src,
                u'C:/Users/root/Pictures/猎豹安全浏览器截图/{}.'.format(self.n + 1) +
                src.split('.')[-1])
            self.m_staticText1.SetLabel(str(self.n + 1))
            self.n += 1
            print(src)
        self.m_staticText1.SetLabel('ok')
        self.m_textCtrl1.Clear()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
