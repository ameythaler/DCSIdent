import IdentUI
from ViewUnitsDlg import ViewUnitsDlg


class MainFrame(IdentUI.MainFrame):
    def __init__(self, parent, app):
        IdentUI.MainFrame.__init__(self, parent)
        self.app = app

    def OnClose(self, event):
        self.app.Exit()

    def OnEditBtnClicked(self, event):
        dlg = ViewUnitsDlg(None, self.app)
        dlg.ShowModal()
