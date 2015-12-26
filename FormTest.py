import SyncDlg
import wx
import threading


class MySyncDlg(SyncDlg.SyncDlg):
    def OnActivate(self, event):
        global workThread
        global workThreadObj
        self.m_Status.SetLabel('Test')
        workThread = threading.Thread(target=workThreadObj, args=['Arg'])
        workThread.start()

    def OnClose( self, event ):
        app.ExitMainLoop()


class DoThreadedStuff:

    def __call__(self, *args, **kwargs):
        global dlg
        dlg.m_Status.SetLabel(args[0])


workThreadObj = DoThreadedStuff()
workThread = None
app = wx.App(False)
dlg = MySyncDlg(None)
dlg.Show(True)
app.MainLoop()

if workThread is not None:
    workThread.join()
