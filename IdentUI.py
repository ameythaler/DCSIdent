# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DCS Identification Test", pos = wx.DefaultPosition, size = wx.Size( 797,518 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_MainToolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.m_QuizBtn = self.m_MainToolbar.AddLabelTool( wx.ID_ANY, u"Quiz", wx.Bitmap( u"Icons/QuizBtn.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Launch Quiz", wx.EmptyString, None )

		self.m_WeaponBtn = self.m_MainToolbar.AddLabelTool( wx.ID_ANY, u"Weapons", wx.Bitmap( u"Icons/WeaponBtn.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None )

		self.m_ClassifyBtn = self.m_MainToolbar.AddLabelTool( wx.ID_ANY, u"Classify", wx.Bitmap( u"Icons/ClassifyBtn.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None )

		self.m_InfoBtn = self.m_MainToolbar.AddLabelTool( wx.ID_ANY, u"Info", wx.Bitmap( u"Icons/InfoBtn.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None )

		self.m_MainToolbar.AddSeparator()

		self.m_EditBtn = self.m_MainToolbar.AddLabelTool( wx.ID_ANY, u"Edit", wx.Bitmap( u"Icons/EditBtn.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Edit Questions", wx.EmptyString, None )

		self.m_MainToolbar.Realize()

		bSizer4.Add( self.m_MainToolbar, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_TOOL, self.OnEditBtnClicked, id = self.m_EditBtn.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnEditBtnClicked( self, event ):
		event.Skip()


###########################################################################
## Class SyncDlg
###########################################################################

class SyncDlg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 296,148 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_Status = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Status.Wrap( -1 )
		bSizer3.Add( self.m_Status, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_Progress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_Progress.SetValue( 0 )
		bSizer3.Add( self.m_Progress, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActivate )
		self.Bind( wx.EVT_CLOSE, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActivate( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class ViewUnitsDlg
###########################################################################

class ViewUnitsDlg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 456,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		m_UnitsListChoices = []
		self.m_UnitsList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_UnitsListChoices, 0 )
		bSizer4.Add( self.m_UnitsList, 1, wx.ALL|wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 10 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_AddBtn = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_AddBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_EditBtn = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_EditBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_RemoveBtn = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_RemoveBtn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_ClearBtn = wx.Button( self, wx.ID_ANY, u"Clear Cache", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_ClearBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.m_OkBtn = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_OkBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		bSizer6.Add( bSizer7, 1, wx.ALIGN_RIGHT, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActivate )
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_AddBtn.Bind( wx.EVT_BUTTON, self.OnAddBtnClick )
		self.m_EditBtn.Bind( wx.EVT_BUTTON, self.OnEditBtnClick )
		self.m_RemoveBtn.Bind( wx.EVT_BUTTON, self.OnRemoveBtnClick )
		self.m_ClearBtn.Bind( wx.EVT_BUTTON, self.OnClearBtnClick )
		self.m_OkBtn.Bind( wx.EVT_BUTTON, self.OnOkBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActivate( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnAddBtnClick( self, event ):
		event.Skip()

	def OnEditBtnClick( self, event ):
		event.Skip()

	def OnRemoveBtnClick( self, event ):
		event.Skip()

	def OnClearBtnClick( self, event ):
		event.Skip()

	def OnOkBtnClick( self, event ):
		event.Skip()


###########################################################################
## Class AddEditUnitDlg
###########################################################################

class AddEditUnitDlg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 979,571 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer1 = wx.GridSizer( 2, 2, 10, 10 )

		sbNationalitySizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nationality" ), wx.VERTICAL )

		m_NationalityListChoices = []
		self.m_NationalityList = wx.ListBox( sbNationalitySizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_NationalityListChoices, wx.LB_SINGLE )
		sbNationalitySizer.Add( self.m_NationalityList, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( sbNationalitySizer, 1, wx.EXPAND, 5 )

		bInfoSizer = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Unit Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_UnitNameTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_UnitNameTxt, 1, wx.ALL, 5 )


		bInfoSizer.Add( bSizer10, 0, wx.EXPAND|wx.TOP, 30 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer16.Add( self.m_staticText4, 0, wx.ALL, 5 )

		m_ThreatChoiceChoices = []
		self.m_ThreatChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ThreatChoiceChoices, 0 )
		self.m_ThreatChoice.SetSelection( 0 )
		bSizer16.Add( self.m_ThreatChoice, 1, wx.ALL, 5 )


		bSizer15.Add( bSizer16, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Effective Range", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer14.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_RangeTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer14.Add( self.m_RangeTxt, 1, wx.ALL, 5 )


		bSizer15.Add( bSizer14, 0, wx.EXPAND, 5 )


		bInfoSizer.Add( bSizer15, 1, wx.EXPAND, 5 )


		gSizer1.Add( bInfoSizer, 1, wx.EXPAND, 5 )

		sbUnitTypeSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Unit Type" ), wx.VERTICAL )

		m_UnitTypeListChoices = []
		self.m_UnitTypeList = wx.ListBox( sbUnitTypeSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_UnitTypeListChoices, wx.LB_SINGLE )
		sbUnitTypeSizer.Add( self.m_UnitTypeList, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( sbUnitTypeSizer, 1, wx.EXPAND, 5 )

		sbThreatsSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Threats" ), wx.VERTICAL )

		m_ThreatsListChoices = []
		self.m_ThreatsList = wx.ListBox( sbThreatsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ThreatsListChoices, wx.LB_MULTIPLE )
		sbThreatsSizer.Add( self.m_ThreatsList, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( sbThreatsSizer, 1, wx.EXPAND, 5 )


		bSizer8.Add( gSizer1, 2, wx.EXPAND|wx.RIGHT, 10 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Images" ), wx.VERTICAL )

		m_ImgListChoices = []
		self.m_ImgList = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ImgListChoices, wx.LB_MULTIPLE )
		sbSizer5.Add( self.m_ImgList, 8, wx.ALL|wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_AddImgBtn = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_AddImgBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.m_RemoveImgBtn = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_RemoveImgBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		sbSizer5.Add( bSizer21, 1, wx.ALIGN_RIGHT, 5 )


		bSizer12.Add( sbSizer5, 3, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_CancelBtn = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_CancelBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.m_OkBtn = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_OkBtn, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		bSizer12.Add( bSizer20, 1, wx.ALIGN_RIGHT, 5 )


		bSizer8.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.OnActivate )
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_ThreatChoice.Bind( wx.EVT_CHOICE, self.OnThreatChoiceSelect )
		self.m_RangeTxt.Bind( wx.EVT_TEXT_ENTER, self.OnRangeTxtEnter )
		self.m_ThreatsList.Bind( wx.EVT_LISTBOX, self.OnThreatsListSelection )
		self.m_ImgList.Bind( wx.EVT_LISTBOX, self.OnImgListSelect )
		self.m_AddImgBtn.Bind( wx.EVT_BUTTON, self.OnAddImgBtnClick )
		self.m_RemoveImgBtn.Bind( wx.EVT_BUTTON, self.OnRemoveImgBtnClick )
		self.m_CancelBtn.Bind( wx.EVT_BUTTON, self.OnCancelBtnClick )
		self.m_OkBtn.Bind( wx.EVT_BUTTON, self.OnOkBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnActivate( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnThreatChoiceSelect( self, event ):
		event.Skip()

	def OnRangeTxtEnter( self, event ):
		event.Skip()

	def OnThreatsListSelection( self, event ):
		event.Skip()

	def OnImgListSelect( self, event ):
		event.Skip()

	def OnAddImgBtnClick( self, event ):
		event.Skip()

	def OnRemoveImgBtnClick( self, event ):
		event.Skip()

	def OnCancelBtnClick( self, event ):
		event.Skip()

	def OnOkBtnClick( self, event ):
		event.Skip()


