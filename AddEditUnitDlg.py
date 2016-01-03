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

        if self.unit is not None:
            # TODO: Handle editing existing units
            pass

    def OnClose(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnOkBtnClick(self, event):
        newUnit = self.ValidateData()
        if newUnit is not None:
            self.unit = newUnit
            self.EndModal(wx.ID_OK)

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

    def OnAddImgBtnClick(self, event):
        dlg = wx.FileDialog(None, message='Select Image File', wildcard='JPEG Files (*.jpg)|*.jpg',
                            style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            for path in dlg.Paths:
                img = os.path.split(path)[1]
                self.imagePaths.append([img, path])
                self.m_ImgList.Append(img)

    def OnRemoveImgBtnClick(self, event):
        selIndices = self.m_ImgList.GetSelections()
        if len(selIndices) > 0:
            for idx in selIndices:
                itm = self.m_ImgList.GetItems()[idx]
                self.m_ImgList.GetItems().remove(itm)
                imgPath = self.imagePaths[idx]
                self.imagePaths.remove(imgPath)

    def ValidateData(self):
        """ Validate the data entered into the forms.

        :return: None, if data is invalid; otherwise, a valid Unit
        """
        unitName = self.m_UnitNameTxt.GetValue()
        nationality = self.m_NationalityList.GetSelection()
        unitType = self.m_UnitTypeList.GetSelection()

        # Make sure required data is present
        if unitName is None or unitName == '' or unitName == ' ':
            self.DisplayValidationError('A unit name must be specified')
            return None

        if nationality is None:
            self.DisplayValidationError('A nationality must be selected')
            return None

        if unitType is None:
            self.DisplayValidationError('A unit type must be selected')
            return None

        if len(self.imagePaths) == 0:
            self.DisplayValidationError('At least one unit image must be added')
            return None

        for threat in self.threats:
            if threat[1] == '':
                rangeTxt = self.m_RangeTxt.GetValue()
                if rangeTxt is not None and rangeTxt != '':
                    self.DisplayValidationError('Threats must have ranges specified.\
                     \'Enter\' must be pressed after entering a range to store it.')
                else:
                    self.DisplayValidationError('Threats must have ranges specified')
                return None

        # If no threats are specified, make sure it's intentional.
        if len(self.threats) == 0:
            mbx = wx.MessageDialog(None, 'No threats specified for selected unit. Continue and create unarmed unit?',
                                   'Warning', style=wx.YES | wx.NO | wx.CANCEL)
            if mbx.ShowModal() != wx.YES:
                return None

        # Unit data is valid, create and return new unit object based on this data.
        retVal = Unit(unitName, nationality, unitType)
        for img in self.imagePaths:
            retVal.AddImage(img[1])
        for threat in self.threats:
            retVal.AddThreat(threat)
        return retVal

    def DisplayValidationError(self, errMsg):
        """ Display a data validation error message.

        :param errMsg: The specific message to display.
        """
        mbx = wx.MessageDialog(None, errMsg, 'Invalid Unit Definition', style=wx.OK)
        mbx.ShowModal()