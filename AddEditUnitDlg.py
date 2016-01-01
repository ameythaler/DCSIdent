import IdentUI
import wx
from Unit import Unit
import os


class AddEditUnitDlg(IdentUI.AddEditUnitDlg):
    def __init__(self, parent, app, unit):
        IdentUI.AddEditUnitDlg.__init__(self, parent)
        self.app = app
        self.unit = unit
        self.threats = []
        self.imagePaths = []

    def OnActivate(self, event):
        self.m_ThreatsList.Set(self.app.threats)
        self.m_NationalityList.Set(self.app.nationalities)
        self.m_UnitTypeList.Set(self.app.classifications)
        self.m_RemoveImgBtn.Enable(False)

        if self.unit is not None:
            self.m_UnitNameTxt.SetValue(self.unit.name)
            # for threat in self.unit.threats:

    def OnClose(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnOkBtnClick(self, event):
        pass

    def OnCancelBtnClick(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnThreatsListSelection(self, event):
        selections = self.m_ThreatsList.GetSelections()

        if len(selections) > len(self.threats):
            for index in selections:
                item = self.app.threats[index]

                containsThreat = False
                for threat in self.threats:
                    if threat[0] == item:
                        containsThreat = True
                        break

                if not containsThreat:
                    self.threats.append([item, ''])
                    self.m_ThreatChoice.Append(item)
        else:
            for item in self.threats:
                index = self.app.threats.index(item[0])
                if index not in selections:
                    self.threats.remove(item)
                    choiceItems = self.m_ThreatChoice.Items
                    choiceItems.remove(item[0])
                    self.m_ThreatChoice.SetItems(choiceItems)
                    break

    def OnThreatChoiceSelect(self, event):
        selectedIndex = self.m_ThreatChoice.GetSelection()
        self.m_RangeTxt.SetValue(self.threats[selectedIndex][1])

    def OnRangeTxtEnter(self, event):
        selectedIndex = self.m_ThreatChoice.GetSelection()
        if selectedIndex > -1:
            self.threats[selectedIndex][1] = self.m_RangeTxt.GetValue()

    def OnImgListSelect(self, event):
        imgSel = self.m_ImgList.GetSelections()
        if len(imgSel) > 0:
            self.m_RemoveImgBtn.Enable(True)
        else:
            self.m_RemoveImgBtn.Enable(False)

    def OnAddImgBtnClick(self, event):
        dlg = wx.FileDialog(None, message='Select Image File', wildcard='JPEG Files (*.jpg)|*.jpg',
                            style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            for path in dlg.Paths:
                img = os.path.split(path)[1]
                self.imagePaths.append([img, path])
                self.m_ImgList.Append(img)

    def OnRemoveImgBtnClick(self, event):
        imgSel = self.m_ImgList.GetSelections()
        pass
