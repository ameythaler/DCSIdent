import wx
from MainFrame import MainFrame
import os
import Unit


class IdentApplication:
    def __init__(self):
        self.wxApp = wx.App(False)
        if os.name == 'posix':
            self.dataDir = os.path.expanduser('~/Library/Caches/DCSIdent')
        else:
            self.dataDir = os.path.expanduser('~/AppData/Roaming/DCSIdent')
        if not os.path.exists(self.dataDir):
            os.makedirs(self.dataDir)
        self.units = []
        self.nationalities = ['Russia', 'USA']
        self.threats = ['LMG', 'HMG', 'Autocannon', 'Cannon', 'ATGM', 'IR SAM', 'RDR SAM']
        self.classifications = ['Utility', 'Artillery', 'MLRS', 'AAA', 'SAM', 'APC', 'Armor']

    def Run(self):
        self.wxApp.MainLoop()

    def Exit(self):
        self.wxApp.ExitMainLoop()

    def LoadCachedUnits(self):
        self.units = []
        unitDirs = os.listdir(self.dataDir)

        for dir in unitDirs:
            unitName = os.path.split(dir)[1]
            unitFile = os.path.join(dir, '{0}.dat'.format(unitName))

            if os.path.exists(unitFile):
                pass

app = IdentApplication()
mainFrame = MainFrame(None, app)
mainFrame.Show(True)
app.Run()
