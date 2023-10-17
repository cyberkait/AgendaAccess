import wx
import quickCopy

from calData import all_apps

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        list_sizer = wx.BoxSizer(wx.VERTICAL)        
        lst = wx.ListBox(panel, choices = all_apps, style = wx.LB_SINGLE)
        list_sizer.Add(lst, 0, wx.ALL | wx.CENTER | wx.EXPAND, 5)
        action_sizer = wx.BoxSizer(wx.HORIZONTAL)
        copy_btn = wx.Button(panel, label='Copy all')
        copy_btn.Bind(wx.EVT_BUTTON, self.on_copyAll)
        action_sizer.Add(copy_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(list_sizer)
        panel.SetSizer(action_sizer)
        self.Show()

    def on_copyAll(self, event):
        quickCopy.copyList(all_apps)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()