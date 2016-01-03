import IdentUI
import wx
import os
from Unit import Unit
from AddEditUnitDlg import AddEditUnitDlg


class ViewUnitsDlg(IdentUI.ViewUnitsDlg):

    def __init__(self, parent, app):
        IdentUI.ViewUnitsDlg.__init__(self, parent)
        self.app = app
        self.units = []
        self.stagedUnits = []

    def OnActivate(self, event):
        pass

    def OnClose(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnOkBtnClick(self, event):
        self.EndModal(wx.ID_OK)

    def OnAddBtnClick(self, event):
        dlg = AddEditUnitDlg(None, self.app, None)
        # if dlg.ShowModal() == wx.ID_OK:


    def OnEditBtnClick(self, event):
        pass

    def OnRemoveBtnClick(self, event):
        pass

    def OnClearBtnClick(self, event):
        mbx = wx.MessageDialog(None, 'Are you sure you want to delete the local cache?', caption='Confirm',
                               style=wx.YES | wx.NO)
        if mbx.ShowModal() == wx.ID_YES:
            os.rmdir(self.app.dataDir)
            os.makedirs(self.app.dataDir)
            pass

    def StageAddedUnit(self, unit):
        self.units.append(unit)
        self.stagedUnits.append(unit)
        # self.m_UnitsList