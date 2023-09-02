import wx
import wx.html2 as webview


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 600))

        self.panel = wx.Panel(self)

        self.web_view = webview.WebView.New(self.panel)
        self.web_view.LoadURL("https://your-django-website.com/face-login")

        self.load_button = wx.Button(self.panel, label="Load Website")
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load_button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.load_button, 0, wx.ALL, 10)
        self.sizer.Add(self.web_view, 1, wx.EXPAND)

        self.panel.SetSizer(self.sizer)

    def on_load_button(self, event):
        self.web_view.LoadURL("https://bustrack.pythonanywhere.com")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "BOSS")
    frame.Show()
    app.MainLoop()
