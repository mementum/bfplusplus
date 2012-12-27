# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from gui.controls.dropdownbutton import OptionButton
import wx
import wx.grid
import wx.html

###########################################################################
## Class CustomizeColours
###########################################################################

class CustomizeColours ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Customize Colours", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer8 = wx.FlexGridSizer( 5, 4, 0, 0 )
		fgSizer8.AddGrowableCol( 1 )
		fgSizer8.AddGrowableCol( 2 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		fgSizer8.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText542 = wx.StaticText( self, wx.ID_ANY, u"Background", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText542.Wrap( -1 )
		self.m_staticText542.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		fgSizer8.Add( self.m_staticText542, 0, wx.ALL, 5 )
		
		self.m_staticText543 = wx.StaticText( self, wx.ID_ANY, u"Foreground", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText543.Wrap( -1 )
		self.m_staticText543.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		fgSizer8.Add( self.m_staticText543, 0, wx.ALL, 5 )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		fgSizer8.Add( self.m_staticText77, 0, wx.ALL, 5 )
		
		self.m_staticTextBack = wx.StaticText( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextBack.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextBack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_colourPickerBack = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerBack, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_colourPickerBackText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerBackText, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextLay = wx.StaticText( self, wx.ID_ANY, u"Lay", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextLay.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextLay, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_colourPickerLay = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerLay, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerLayText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerLayText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline401 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline401, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_staticline40 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline40, 0, wx.EXPAND, 5 )
		
		self.m_staticline41 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline41, 0, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextMatched = wx.StaticText( self, wx.ID_ANY, u"Matched Bets", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextMatched.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextMatched, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerMatched = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMatched, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerMatchedText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMatchedText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextUnmatched = wx.StaticText( self, wx.ID_ANY, u"Unmatched Bets", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextUnmatched.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextUnmatched, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerUnmatched = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerUnmatched, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_colourPickerUnmatchedText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerUnmatchedText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline4011 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4011, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_staticline4012 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4012, 0, wx.EXPAND, 5 )
		
		self.m_staticline4013 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4013, 0, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextInPlay = wx.StaticText( self, wx.ID_ANY, u"In-Play On", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextInPlay.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextInPlay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerInPlay = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerInPlay, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_colourPickerInPlayText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerInPlayText, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button511 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button511, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextInPlayOff = wx.StaticText( self, wx.ID_ANY, u"In-Play Off", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextInPlayOff.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextInPlayOff, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerInPlayOff = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerInPlayOff, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerInPlayOffText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerInPlayOffText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5111 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button5111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline4014 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4014, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_staticline4015 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4015, 0, wx.EXPAND, 5 )
		
		self.m_staticline4016 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4016, 0, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextMarketActive = wx.StaticText( self, wx.ID_ANY, u"Market Active", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextMarketActive.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextMarketActive, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerMarketActive = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMarketActive, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerMarketActiveText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMarketActiveText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button51111 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button51111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextMarketSuspClosed = wx.StaticText( self, wx.ID_ANY, u"Market Suspended/Closed", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextMarketSuspClosed.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextMarketSuspClosed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerMarketSuspClosed = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMarketSuspClosed, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerMarketSuspClosedText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerMarketSuspClosedText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button511111 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button511111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline4017 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4017, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_staticline4018 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4018, 0, wx.EXPAND, 5 )
		
		self.m_staticline4019 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer8.Add( self.m_staticline4019, 0, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextNetworkOK = wx.StaticText( self, wx.ID_ANY, u"Network OK", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextNetworkOK.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextNetworkOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_colourPickerNetworkOK = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerNetworkOK, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerNetworkOKText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerNetworkOKText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5111111 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button5111111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextNetworkErrors = wx.StaticText( self, wx.ID_ANY, u"Network Errors", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextNetworkErrors.Wrap( -1 )
		fgSizer8.Add( self.m_staticTextNetworkErrors, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_colourPickerNetworkErrors = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerNetworkErrors, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPickerNetworkErrorsText = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer8.Add( self.m_colourPickerNetworkErrorsText, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button51111111 = wx.Button( self, wx.ID_ANY, u"Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button51111111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 6), 1, wx.EXPAND, 5 )
		
		
		fgSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer40.Add( fgSizer8, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer40.Add( self.m_staticline22, 0, wx.EXPAND|wx.BOTTOM, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		bSizer40.Add( m_sdbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.SetSizer( bSizer40 )
		self.Layout()
		bSizer40.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_colourPickerBack.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerBackText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursBackDefaults )
		self.m_colourPickerLay.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerLayText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button49.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursLayDefaults )
		self.m_colourPickerMatched.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerMatchedText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button50.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursMatchedDefaults )
		self.m_colourPickerUnmatched.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerUnmatchedText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursUnmatchedDefaults )
		self.m_colourPickerInPlay.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerInPlayText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button511.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursInPlayDefaults )
		self.m_colourPickerInPlayOff.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerInPlayOffText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button5111.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursInPlayOffDefaults )
		self.m_colourPickerMarketActive.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerMarketActiveText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button51111.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursMarketActiveDefaults )
		self.m_colourPickerMarketSuspClosed.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerMarketSuspClosedText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button511111.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursMarketSuspClosedDefaults )
		self.m_colourPickerNetworkOK.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerNetworkOKText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button5111111.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursNetworkOKDefaults )
		self.m_colourPickerNetworkErrors.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_colourPickerNetworkErrorsText.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnColourChangedAll )
		self.m_button51111111.Bind( wx.EVT_BUTTON, self.OnButtonClickColoursNetworkErrorsDefaults )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnColourChangedAll( self, event ):
		event.Skip()
	
	
	def OnButtonClickColoursBackDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursLayDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursMatchedDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursUnmatchedDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursInPlayDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursInPlayOffDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursMarketActiveDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursMarketSuspClosedDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursNetworkOKDefaults( self, event ):
		event.Skip()
	
	
	
	def OnButtonClickColoursNetworkErrorsDefaults( self, event ):
		event.Skip()
	

###########################################################################
## Class EditModParams
###########################################################################

class EditModParams ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Module Params", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer72 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Property" ), wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer6.AddGrowableCol( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		fgSizer6.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextName = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextName.Wrap( -1 )
		fgSizer6.Add( self.m_staticTextName, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		fgSizer6.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextType = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextType.Wrap( -1 )
		fgSizer6.Add( self.m_staticTextType, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )
		fgSizer6.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlValue, 1, wx.ALL, 5 )
		
		sbSizer12.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		bSizer75.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_button50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer72.Add( bSizer75, 1, wx.EXPAND, 5 )
		
		self.m_staticline34 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer72.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer10 = wx.StdDialogButtonSizer()
		self.m_sdbSizer10OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer10.AddButton( self.m_sdbSizer10OK )
		self.m_sdbSizer10Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer10.AddButton( self.m_sdbSizer10Cancel )
		m_sdbSizer10.Realize();
		bSizer72.Add( m_sdbSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		self.SetSizer( bSizer72 )
		self.Layout()
		bSizer72.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button50.Bind( wx.EVT_BUTTON, self.OnButtonClickDefault )
		self.m_sdbSizer10OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickDefault( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class EditPattern
###########################################################################

class EditPattern ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Pattern", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"Pattern name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		self.m_staticText64.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer47.Add( self.m_staticText64, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer48 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlPatternName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		bSizer48.Add( self.m_textCtrlPatternName, 0, wx.ALL, 5 )
		
		self.m_buttonPatternNameEdit = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer48.Add( self.m_buttonPatternNameEdit, 0, wx.ALL, 5 )
		
		bSizer47.Add( bSizer48, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer47.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText641 = wx.StaticText( self, wx.ID_ANY, u"Market names to be matched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText641.Wrap( -1 )
		self.m_staticText641.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer47.Add( self.m_staticText641, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer481 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlPatternMarketNames = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		bSizer481.Add( self.m_textCtrlPatternMarketNames, 0, wx.ALL, 5 )
		
		self.m_buttonPatternMarketNamesEdit = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer481.Add( self.m_buttonPatternMarketNamesEdit, 0, wx.ALL, 5 )
		
		bSizer47.Add( bSizer481, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_staticline251 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer47.Add( self.m_staticline251, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText6411 = wx.StaticText( self, wx.ID_ANY, u"Menu names to be matched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6411.Wrap( -1 )
		self.m_staticText6411.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer47.Add( self.m_staticText6411, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer4811 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBoxPatternMenuNamesPositiveChoices = []
		self.m_listBoxPatternMenuNamesPositive = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,100 ), m_listBoxPatternMenuNamesPositiveChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		bSizer4811.Add( self.m_listBoxPatternMenuNamesPositive, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button36 = wx.Button( self, wx.ID_ANY, u"New ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button36, 0, wx.ALL, 5 )
		
		self.m_buttonPatternMenuNamesPositiveEdit = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_buttonPatternMenuNamesPositiveEdit, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button37, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline33 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer59.Add( self.m_staticline33, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, u"Move Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button40, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Move Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_button41, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer4811.Add( bSizer59, 1, wx.EXPAND, 5 )
		
		bSizer47.Add( bSizer4811, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"Each line will be \"AND\" matched", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText74.Wrap( -1 )
		bSizer47.Add( self.m_staticText74, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText741 = wx.StaticText( self, wx.ID_ANY, u"Items in each line will be  \"or\" matched", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText741.Wrap( -1 )
		bSizer47.Add( self.m_staticText741, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2511 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer47.Add( self.m_staticline2511, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText64111 = wx.StaticText( self, wx.ID_ANY, u"Menu names NOT to be matched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64111.Wrap( -1 )
		self.m_staticText64111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer47.Add( self.m_staticText64111, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer48111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlPatternMenuNegative = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		bSizer48111.Add( self.m_textCtrlPatternMenuNegative, 0, wx.ALL, 5 )
		
		self.m_buttonPatternMenuNamesNegativeEdit = wx.Button( self, wx.ID_ANY, u"Edit...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer48111.Add( self.m_buttonPatternMenuNamesNegativeEdit, 0, wx.ALL, 5 )
		
		bSizer47.Add( bSizer48111, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_staticline252 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer47.Add( self.m_staticline252, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();
		bSizer47.Add( m_sdbSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.SetSizer( bSizer47 )
		self.Layout()
		bSizer47.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonPatternNameEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternNameEdit )
		self.m_buttonPatternMarketNamesEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternMarketNamesEdit )
		self.m_button36.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternMenuNamesPositiveNew )
		self.m_buttonPatternMenuNamesPositiveEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternMenuNamesPositiveEdit )
		self.m_button37.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternMenuNamesPositiveDelete )
		self.m_button40.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveUp )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveDown )
		self.m_buttonPatternMenuNamesNegativeEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternMenuNamesNegativeEdit )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickPatternNameEdit( self, event ):
		event.Skip()
	
	def OnButtonClickPatternMarketNamesEdit( self, event ):
		event.Skip()
	
	def OnButtonClickPatternMenuNamesPositiveNew( self, event ):
		event.Skip()
	
	def OnButtonClickPatternMenuNamesPositiveEdit( self, event ):
		event.Skip()
	
	def OnButtonClickPatternMenuNamesPositiveDelete( self, event ):
		event.Skip()
	
	def OnButtonClickMoveUp( self, event ):
		event.Skip()
	
	def OnButtonClickMoveDown( self, event ):
		event.Skip()
	
	def OnButtonClickPatternMenuNamesNegativeEdit( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class EditString
###########################################################################

class EditString ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Enter Value", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlString = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_textCtrlString, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		bSizer58.Add( m_sdbSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.SetSizer( bSizer58 )
		self.Layout()
		bSizer58.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer4OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class EditStringList
###########################################################################

class EditStringList ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Items", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBoxItemListChoices = []
		self.m_listBoxItemList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), m_listBoxItemListChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		bSizer62.Add( self.m_listBoxItemList, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonNew = wx.Button( self, wx.ID_ANY, u"New ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.m_buttonNew, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonEdit = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonEdit.Enable( False )
		
		bSizer63.Add( self.m_buttonEdit, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonDelete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDelete.Enable( False )
		
		bSizer63.Add( self.m_buttonDelete, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline32 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer63.Add( self.m_staticline32, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonMoveUp = wx.Button( self, wx.ID_ANY, u"Move Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMoveUp.Enable( False )
		
		bSizer63.Add( self.m_buttonMoveUp, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonMoveDown = wx.Button( self, wx.ID_ANY, u"Move Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMoveDown.Enable( False )
		
		bSizer63.Add( self.m_buttonMoveDown, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline321 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer63.Add( self.m_staticline321, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonSort = wx.Button( self, wx.ID_ANY, u"Sort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSort.Enable( False )
		
		bSizer63.Add( self.m_buttonSort, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonReverse = wx.Button( self, wx.ID_ANY, u"Reverse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonReverse.Enable( False )
		
		bSizer63.Add( self.m_buttonReverse, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer62.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		bSizer60.Add( bSizer62, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		self.m_staticline37 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer60.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer6 = wx.StdDialogButtonSizer()
		self.m_sdbSizer6OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer6.AddButton( self.m_sdbSizer6OK )
		self.m_sdbSizer6Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer6.AddButton( self.m_sdbSizer6Cancel )
		m_sdbSizer6.Realize();
		bSizer60.Add( m_sdbSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		self.SetSizer( bSizer60 )
		self.Layout()
		bSizer60.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_listBoxItemList.Bind( wx.EVT_LISTBOX, self.OnListBoxItemList )
		self.m_listBoxItemList.Bind( wx.EVT_LISTBOX_DCLICK, self.OnListBoxDClickItemList )
		self.m_buttonNew.Bind( wx.EVT_BUTTON, self.OnButtonClickNew )
		self.m_buttonEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickEdit )
		self.m_buttonDelete.Bind( wx.EVT_BUTTON, self.OnButtonClickDelete )
		self.m_buttonMoveUp.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveUp )
		self.m_buttonMoveDown.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveDown )
		self.m_buttonSort.Bind( wx.EVT_BUTTON, self.OnButtonClickSort )
		self.m_buttonReverse.Bind( wx.EVT_BUTTON, self.OnButtonClickReverse )
		self.m_sdbSizer6OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnListBoxItemList( self, event ):
		event.Skip()
	
	def OnListBoxDClickItemList( self, event ):
		event.Skip()
	
	def OnButtonClickNew( self, event ):
		event.Skip()
	
	def OnButtonClickEdit( self, event ):
		event.Skip()
	
	def OnButtonClickDelete( self, event ):
		event.Skip()
	
	def OnButtonClickMoveUp( self, event ):
		event.Skip()
	
	def OnButtonClickMoveDown( self, event ):
		event.Skip()
	
	def OnButtonClickSort( self, event ):
		event.Skip()
	
	def OnButtonClickReverse( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bfplusplus", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panelMainLeft = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer66 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookMain = wx.Notebook( self.m_panelMainLeft, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP )
		self.m_panel81 = wx.Panel( self.m_notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Login" ), wx.VERTICAL )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer4 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText821 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText821.Wrap( -1 )
		fgSizer4.Add( self.m_staticText821, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		m_comboBoxUsernameChoices = []
		self.m_comboBoxUsername = wx.ComboBox( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxUsernameChoices, wx.CB_SORT )
		fgSizer4.Add( self.m_comboBoxUsername, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer4.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrlPassword = wx.TextCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		fgSizer4.Add( self.m_textCtrlPassword, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer91.Add( fgSizer4, 3, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonLogin = wx.BitmapButton( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/user_go.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonLogin.SetDefault() 
		self.m_buttonLogin.SetToolTipString( u"Login" )
		
		self.m_buttonLogin.SetToolTipString( u"Login" )
		
		bSizer92.Add( self.m_buttonLogin, 1, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer91.Add( bSizer92, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer91.AddSpacer( ( 0, 0), 0, wx.EXPAND, 5 )
		
		sbSizer6.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonManageUsernames = wx.BitmapButton( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/group_edit.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonManageUsernames.SetToolTipString( u"Manage Usernames" )
		
		self.m_buttonManageUsernames.SetToolTipString( u"Manage Usernames" )
		
		bSizer34.Add( self.m_buttonManageUsernames, 1, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxRememberUsername = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Remember usernames", wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bfplusplus" )
		bSizer34.Add( self.m_checkBoxRememberUsername, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer34.AddSpacer( ( 0, 0), 0, wx.EXPAND, 5 )
		
		sbSizer6.Add( bSizer34, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline581 = wx.StaticLine( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer6.Add( self.m_staticline581, 0, wx.EXPAND|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.bSizer84 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panelFreeApiSettings = wx.Panel( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer135 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxFreeAPI = wx.CheckBox( self.m_panelFreeApiSettings, wx.ID_ANY, u"Free API (82)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer135.Add( self.m_checkBoxFreeAPI, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline62 = wx.StaticLine( self.m_panelFreeApiSettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer135.Add( self.m_staticline62, 0, wx.EXPAND|wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText161 = wx.StaticText( self.m_panelFreeApiSettings, wx.ID_ANY, u"Product Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer135.Add( self.m_staticText161, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.LEFT, 5 )
		
		self.m_textCtrlProductId = wx.TextCtrl( self.m_panelFreeApiSettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer135.Add( self.m_textCtrlProductId, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_panelFreeApiSettings.SetSizer( bSizer135 )
		self.m_panelFreeApiSettings.Layout()
		bSizer135.Fit( self.m_panelFreeApiSettings )
		self.bSizer84.Add( self.m_panelFreeApiSettings, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panelBfApiSettings = wx.Panel( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelBfApiSettings.Hide()
		
		bSizer136 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText95 = wx.StaticText( self.m_panelBfApiSettings, wx.ID_ANY, u"Betfair Verified Edition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )
		bSizer136.Add( self.m_staticText95, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_panelBfApiSettings.SetSizer( bSizer136 )
		self.m_panelBfApiSettings.Layout()
		bSizer136.Fit( self.m_panelBfApiSettings )
		self.bSizer84.Add( self.m_panelBfApiSettings, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer6.Add( self.bSizer84, 0, wx.EXPAND, 5 )
		
		bSizer20.Add( sbSizer6, 0, wx.EXPAND, 5 )
		
		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Funds" ), wx.VERTICAL )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer891 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkboxShowFunds = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkboxShowFunds.Enable( False )
		
		bSizer891.Add( self.m_checkboxShowFunds, 0, wx.ALL, 5 )
		
		self.m_buttonReloadFunds = wx.BitmapButton( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonReloadFunds.Enable( False )
		self.m_buttonReloadFunds.SetToolTipString( u"Reload Funds" )
		
		self.m_buttonReloadFunds.Enable( False )
		self.m_buttonReloadFunds.SetToolTipString( u"Reload Funds" )
		
		bSizer891.Add( self.m_buttonReloadFunds, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer121.Add( bSizer891, 0, wx.EXPAND, 5 )
		
		self.m_staticline26 = wx.StaticLine( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer121.Add( self.m_staticline26, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer7.AddGrowableCol( 1 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bitmap5 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/world.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap5.SetToolTipString( u"Total Funds" )
		
		fgSizer7.Add( self.m_bitmap5, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticTextFundsTotal = wx.StaticText( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextFundsTotal.Wrap( -1 )
		self.m_staticTextFundsTotal.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_staticTextFundsTotal, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_bitmap4 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-flags/gb_stretched.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap4.SetToolTipString( u"UK Wallet" )
		
		fgSizer7.Add( self.m_bitmap4, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticTextFundsUk = wx.StaticText( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextFundsUk.Wrap( -1 )
		self.m_staticTextFundsUk.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_staticTextFundsUk, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-flags/au_stretched.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap3.SetToolTipString( u"Aus Wallet" )
		
		fgSizer7.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticTextFundsAus = wx.StaticText( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextFundsAus.Wrap( -1 )
		self.m_staticTextFundsAus.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_staticTextFundsAus, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer121.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer111.Add( bSizer121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText94 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Transfer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )
		self.m_staticText94.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer81.Add( self.m_staticText94, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_bitmap41 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-flags/gb_stretched.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap41.SetToolTipString( u"UK Wallet" )
		
		bSizer81.Add( self.m_bitmap41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButtonAus2UK = wx.BitmapButton( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_left_blued_shadow_1610.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAus2UK.Enable( False )
		
		self.m_bpButtonAus2UK.Enable( False )
		
		bSizer81.Add( self.m_bpButtonAus2UK, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.m_textCtrlTransferFunds = wx.TextCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer81.Add( self.m_textCtrlTransferFunds, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_bpButtonUK2Aus = wx.BitmapButton( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_right_blued_shadow_1610.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonUK2Aus.Enable( False )
		
		self.m_bpButtonUK2Aus.Enable( False )
		
		bSizer81.Add( self.m_bpButtonUK2Aus, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_bitmap33 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-flags/au_stretched.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap33.SetToolTipString( u"Aus Wallet" )
		
		bSizer81.Add( self.m_bitmap33, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		sbSizer111.Add( bSizer81, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.TOP, 5 )
		
		bSizer20.Add( sbSizer111, 0, wx.EXPAND, 5 )
		
		sbSizer62 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Network" ), wx.VERTICAL )
		
		bSizer901 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/connect.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer901.Add( self.m_bitmap2, 0, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		fgSizer71 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer71.AddGrowableCol( 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText45 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Proxy Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		fgSizer71.Add( self.m_staticText45, 0, wx.ALIGN_BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText46 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer71.Add( self.m_staticText46, 0, wx.ALIGN_BOTTOM|wx.RIGHT, 5 )
		
		self.m_textCtrlProxyHost = wx.TextCtrl( self.m_panel81, wx.ID_ANY, u"myproxy.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_textCtrlProxyHost, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		self.m_textCtrlProxyPort = wx.TextCtrl( self.m_panel81, wx.ID_ANY, u"8888", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer71.Add( self.m_textCtrlProxyPort, 0, wx.BOTTOM, 5 )
		
		bSizer901.Add( fgSizer71, 1, wx.EXPAND, 5 )
		
		sbSizer62.Add( bSizer901, 1, wx.EXPAND, 5 )
		
		self.m_checkBoxUseProxy = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Enable Proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer62.Add( self.m_checkBoxUseProxy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline731 = wx.StaticLine( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer62.Add( self.m_staticline731, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer115 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap7 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/hourglass.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap7.SetToolTipString( u"Prices Refresh Time" )
		
		bSizer115.Add( self.m_bitmap7, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText86 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Refresh Prices", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		bSizer115.Add( self.m_staticText86, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_sliderRefresh = wx.Slider( self.m_panel81, wx.ID_ANY, 10, 10, 300, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL )
		self.m_menuSliderRefresh = wx.Menu()
		self.m_menuItemSliderRefresh_1_0 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"1.0 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_0 )
		
		self.m_menuItemSliderRefresh_1_01 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"1.5 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_01 )
		
		self.m_menuItemSliderRefresh_1_011 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"2.0 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_011 )
		
		self.m_menuItemSliderRefresh_1_012 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"3.0 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_012 )
		
		self.m_menuItemSliderRefresh_1_0121 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"5.0 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_0121 )
		
		self.m_menuItemSliderRefresh_1_01211 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"10 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_01211 )
		
		self.m_menuItemSliderRefresh_1_012111 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"15 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_012111 )
		
		self.m_menuItemSliderRefresh_1_0121111 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"20 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_0121111 )
		
		self.m_menuItemSliderRefresh_1_01211111 = wx.MenuItem( self.m_menuSliderRefresh, wx.ID_ANY, u"30 sec", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderRefresh.AppendItem( self.m_menuItemSliderRefresh_1_01211111 )
		
		self.m_sliderRefresh.Bind( wx.EVT_RIGHT_DOWN, self.m_sliderRefreshOnContextMenu ) 
		
		bSizer115.Add( self.m_sliderRefresh, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextRefresh = wx.StaticText( self.m_panel81, wx.ID_ANY, u"1.0 sec", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextRefresh.Wrap( -1 )
		bSizer115.Add( self.m_staticTextRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sbSizer62.Add( bSizer115, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline7311 = wx.StaticLine( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer62.Add( self.m_staticline7311, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer116 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap14 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/compress.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer116.Add( self.m_bitmap14, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxOptimizeNetwork = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Reduce Network Traffic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxOptimizeNetwork.SetToolTipString( u"If this box is checked only market prices will be fetched\nreducing traffic load by 66%.\n\nBetting activity will trigger fetching of Bets and Profit and Loss\naccounting, until unmatched bets are cancelled or matched.\n\nThe \"Guard time\" indicates how much time has to be waited after betting activity ceases before only prices are fetched" )
		
		bSizer116.Add( self.m_checkBoxOptimizeNetwork, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_spinCtrlOptimizeGuard = wx.SpinCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 5, 20, 7 )
		bSizer116.Add( self.m_spinCtrlOptimizeGuard, 0, wx.ALL, 5 )
		
		self.m_staticTextOptimizeNetworkSafety = wx.StaticText( self.m_panel81, wx.ID_ANY, u"ticks guard", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextOptimizeNetworkSafety.Wrap( -1 )
		bSizer116.Add( self.m_staticTextOptimizeNetworkSafety, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sbSizer62.Add( bSizer116, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer20.Add( sbSizer62, 0, wx.EXPAND, 5 )
		
		sbSizer91 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Colours" ), wx.HORIZONTAL )
		
		
		sbSizer91.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/color_wheel.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer91.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonCustomizeColours = wx.Button( self.m_panel81, wx.ID_ANY, u"Customize colours", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer91.Add( self.m_buttonCustomizeColours, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT, 5 )
		
		
		sbSizer91.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer20.Add( sbSizer91, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Configuration" ), wx.VERTICAL )
		
		bSizer912 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap6 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/cog_delete.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer912.Add( self.m_bitmap6, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonClearRegistryStorage = wx.Button( self.m_panel81, wx.ID_ANY, u"Clear Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer912.Add( self.m_buttonClearRegistryStorage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer9.Add( bSizer912, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBoxExitAfterRegCleanUp = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Exit after clearing", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBoxExitAfterRegCleanUp, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer36.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer92 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel81, wx.ID_ANY, u"Update" ), wx.VERTICAL )
		
		bSizer198 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap35 = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/world_link.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer198.Add( self.m_bitmap35, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonLookForUpdates = wx.Button( self.m_panel81, wx.ID_ANY, u"Check Now", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer198.Add( self.m_buttonLookForUpdates, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer92.Add( bSizer198, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBoxSeekUpdateOnAppStart = wx.CheckBox( self.m_panel81, wx.ID_ANY, u"Check on start", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer92.Add( self.m_checkBoxSeekUpdateOnAppStart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer36.Add( sbSizer92, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.EXPAND, 5 )
		
		bSizer20.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		self.m_panel81.SetSizer( bSizer20 )
		self.m_panel81.Layout()
		bSizer20.Fit( self.m_panel81 )
		self.m_notebookMain.AddPage( self.m_panel81, u"General", True )
		self.m_panel6 = wx.Panel( self.m_notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookFavs = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel36 = wx.Panel( self.m_notebookFavs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonTreeEventsCollapseAll = wx.BitmapButton( self.m_panel36, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/application_view_list.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonTreeEventsCollapseAll.Enable( False )
		self.m_buttonTreeEventsCollapseAll.SetToolTipString( u"Collapse All" )
		
		self.m_buttonTreeEventsCollapseAll.Enable( False )
		self.m_buttonTreeEventsCollapseAll.SetToolTipString( u"Collapse All" )
		
		bSizer68.Add( self.m_buttonTreeEventsCollapseAll, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonTreeEventsReloadAll = wx.BitmapButton( self.m_panel36, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonTreeEventsReloadAll.Enable( False )
		self.m_buttonTreeEventsReloadAll.SetToolTipString( u"Reload All" )
		
		self.m_buttonTreeEventsReloadAll.Enable( False )
		self.m_buttonTreeEventsReloadAll.SetToolTipString( u"Reload All" )
		
		bSizer68.Add( self.m_buttonTreeEventsReloadAll, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonTreeEventsReloadSelected = wx.BitmapButton( self.m_panel36, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonTreeEventsReloadSelected.Enable( False )
		self.m_buttonTreeEventsReloadSelected.SetToolTipString( u"Reload the selected item" )
		
		self.m_buttonTreeEventsReloadSelected.Enable( False )
		self.m_buttonTreeEventsReloadSelected.SetToolTipString( u"Reload the selected item" )
		
		bSizer68.Add( self.m_buttonTreeEventsReloadSelected, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonTreeEventsEdit = wx.BitmapButton( self.m_panel36, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_white_wrench.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonTreeEventsEdit.Enable( False )
		self.m_buttonTreeEventsEdit.SetToolTipString( u"Edit Events" )
		
		self.m_buttonTreeEventsEdit.Enable( False )
		self.m_buttonTreeEventsEdit.SetToolTipString( u"Edit Events" )
		
		bSizer68.Add( self.m_buttonTreeEventsEdit, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButtonGenerateSearchPattern = wx.BitmapButton( self.m_panel36, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/magnifier_zoom_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonGenerateSearchPattern.Enable( False )
		self.m_bpButtonGenerateSearchPattern.SetToolTipString( u"Generate Search Patterns" )
		
		self.m_bpButtonGenerateSearchPattern.Enable( False )
		self.m_bpButtonGenerateSearchPattern.SetToolTipString( u"Generate Search Patterns" )
		
		bSizer68.Add( self.m_bpButtonGenerateSearchPattern, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer113.Add( bSizer68, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline721 = wx.StaticLine( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer113.Add( self.m_staticline721, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer155 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxLoadMarketsAfterLogin = wx.CheckBox( self.m_panel36, wx.ID_ANY, u"Load Markets on Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer155.Add( self.m_checkBoxLoadMarketsAfterLogin, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticline89 = wx.StaticLine( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer155.Add( self.m_staticline89, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxVirtualPrices = wx.CheckBox( self.m_panel36, wx.ID_ANY, u"Virtual Prices", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer155.Add( self.m_checkBoxVirtualPrices, 0, wx.ALL, 5 )
		
		bSizer113.Add( bSizer155, 0, wx.EXPAND, 5 )
		
		self.m_staticline88 = wx.StaticLine( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer113.Add( self.m_staticline88, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer961 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxAutoExpand = wx.CheckBox( self.m_panel36, wx.ID_ANY, u"Auto Expand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxAutoExpand.SetValue(True) 
		bSizer961.Add( self.m_checkBoxAutoExpand, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline621 = wx.StaticLine( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer961.Add( self.m_staticline621, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxCacheMarkets = wx.CheckBox( self.m_panel36, wx.ID_ANY, u"Market Cache", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCacheMarkets.SetValue(True) 
		bSizer961.Add( self.m_checkBoxCacheMarkets, 0, wx.ALL, 5 )
		
		self.m_staticline66 = wx.StaticLine( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer961.Add( self.m_staticline66, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxUseBfOrder = wx.CheckBox( self.m_panel36, wx.ID_ANY, u"Betfair order", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer961.Add( self.m_checkBoxUseBfOrder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer113.Add( bSizer961, 0, 0, 5 )
		
		self.m_treeEvents = wx.TreeCtrl( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT )
		self.m_menuTreeEvents = wx.Menu()
		self.m_menuItemTreeItemSelect = wx.MenuItem( self.m_menuTreeEvents, wx.ID_ANY, u"Select", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemTreeItemSelect.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/tick.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuTreeEvents.AppendItem( self.m_menuItemTreeItemSelect )
		
		self.m_menuTreeEvents.AppendSeparator()
		
		self.m_menuItemTreeCollapseAll = wx.MenuItem( self.m_menuTreeEvents, wx.ID_ANY, u"Collapse All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemTreeCollapseAll.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/application_view_list.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuTreeEvents.AppendItem( self.m_menuItemTreeCollapseAll )
		
		self.m_menuItemTreeItemReloadAll = wx.MenuItem( self.m_menuTreeEvents, wx.ID_ANY, u"Reload All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemTreeItemReloadAll.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuTreeEvents.AppendItem( self.m_menuItemTreeItemReloadAll )
		self.m_menuItemTreeItemReloadAll.Enable( False )
		
		self.m_menuItemTreeItemReload = wx.MenuItem( self.m_menuTreeEvents, wx.ID_ANY, u"Reload", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemTreeItemReload.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh_small.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuTreeEvents.AppendItem( self.m_menuItemTreeItemReload )
		
		self.m_menuTreeEvents.AppendSeparator()
		
		self.m_menuItemGenerateSearchPattern = wx.MenuItem( self.m_menuTreeEvents, wx.ID_ANY, u"Generate Search Pattern ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemGenerateSearchPattern.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/magnifier_zoom_in.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuTreeEvents.AppendItem( self.m_menuItemGenerateSearchPattern )
		
		self.m_treeEvents.Bind( wx.EVT_RIGHT_DOWN, self.m_treeEventsOnContextMenu ) 
		
		bSizer113.Add( self.m_treeEvents, 1, wx.EXPAND, 5 )
		
		self.m_panel36.SetSizer( bSizer113 )
		self.m_panel36.Layout()
		bSizer113.Fit( self.m_panel36 )
		self.m_notebookFavs.AddPage( self.m_panel36, u"All Markets", True )
		self.m_panel121 = wx.Panel( self.m_notebookFavs, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer401 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBoxSavedMarketsChoices = []
		self.m_listBoxSavedMarkets = wx.ListBox( self.m_panel121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxSavedMarketsChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_SORT )
		self.m_menuSavedMarkets = wx.Menu()
		self.m_menuItemSavedMarketsLoad = wx.MenuItem( self.m_menuSavedMarkets, wx.ID_ANY, u"Load Market", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemSavedMarketsLoad.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/page_go.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuSavedMarkets.AppendItem( self.m_menuItemSavedMarketsLoad )
		
		self.m_menuItemSavedMarketsSelectAll = wx.MenuItem( self.m_menuSavedMarkets, wx.ID_ANY, u"Select All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSavedMarkets.AppendItem( self.m_menuItemSavedMarketsSelectAll )
		
		self.m_menuItemSavedMarketsDeleteSelected = wx.MenuItem( self.m_menuSavedMarkets, wx.ID_ANY, u"Delete Selected", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSavedMarkets.AppendItem( self.m_menuItemSavedMarketsDeleteSelected )
		
		self.m_menuItemSavedMarketsDeleteAll = wx.MenuItem( self.m_menuSavedMarkets, wx.ID_ANY, u"Delete All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSavedMarkets.AppendItem( self.m_menuItemSavedMarketsDeleteAll )
		
		self.m_listBoxSavedMarkets.Bind( wx.EVT_RIGHT_DOWN, self.m_listBoxSavedMarketsOnContextMenu ) 
		
		bSizer401.Add( self.m_listBoxSavedMarkets, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel121.SetSizer( bSizer401 )
		self.m_panel121.Layout()
		bSizer401.Fit( self.m_panel121 )
		self.m_notebookFavs.AddPage( self.m_panel121, u"Favourites", False )
		self.m_panel12 = wx.Panel( self.m_notebookFavs, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer431 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap10 = wx.StaticBitmap( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/magnifier.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer431.Add( self.m_bitmap10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonPatternManager = wx.Button( self.m_panel12, wx.ID_ANY, u"Pattern Search Manager ...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer431.Add( self.m_buttonPatternManager, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticline76 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer431.Add( self.m_staticline76, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText99 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Refresh Now", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )
		bSizer431.Add( self.m_staticText99, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_bpButton33 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer431.Add( self.m_bpButton33, 0, wx.ALL, 5 )
		
		bSizer40.Add( bSizer431, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline632 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer40.Add( self.m_staticline632, 0, wx.EXPAND|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText77 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Refresh search data every", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		bSizer97.Add( self.m_staticText77, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_sliderMarketDataRefresh = wx.Slider( self.m_panel12, wx.ID_ANY, 5, 0, 25, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL )
		bSizer97.Add( self.m_sliderMarketDataRefresh, 1, wx.EXPAND, 5 )
		
		self.m_staticTextMarkeDataRefresh = wx.StaticText( self.m_panel12, wx.ID_ANY, u"20 mins", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticTextMarkeDataRefresh.Wrap( -1 )
		bSizer97.Add( self.m_staticTextMarkeDataRefresh, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer40.Add( bSizer97, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer971 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText771 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Available markets to search:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText771.Wrap( -1 )
		bSizer971.Add( self.m_staticText771, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextAvailableAllMarkets = wx.StaticText( self.m_panel12, wx.ID_ANY, u"UK: 0 / Aus: 0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticTextAvailableAllMarkets.Wrap( -1 )
		bSizer971.Add( self.m_staticTextAvailableAllMarkets, 0, wx.ALL, 5 )
		
		bSizer40.Add( bSizer971, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer38211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4021 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Updated: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4021.Wrap( -1 )
		self.m_staticText4021.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer38211.Add( self.m_staticText4021, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextMarketsUpdate = wx.StaticText( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticTextMarketsUpdate.Wrap( -1 )
		bSizer38211.Add( self.m_staticTextMarketsUpdate, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer40.Add( bSizer38211, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_listCtrlFavs = wx.ListCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES|wx.STATIC_BORDER )
		self.m_menuFavSearch = wx.Menu()
		self.m_menuItemFavSearchLoad = wx.MenuItem( self.m_menuFavSearch, wx.ID_ANY, u"Load Market", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemFavSearchLoad.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/page_go.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuFavSearch.AppendItem( self.m_menuItemFavSearchLoad )
		
		self.m_menuFavSearch.AppendSeparator()
		
		self.m_menuItemPatternManager = wx.MenuItem( self.m_menuFavSearch, wx.ID_ANY, u"Pattern Manager ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemPatternManager.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/magnifier.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuFavSearch.AppendItem( self.m_menuItemPatternManager )
		
		self.m_menuFavSearch.AppendSeparator()
		
		self.m_menuItemReloadPattern = wx.MenuItem( self.m_menuFavSearch, wx.ID_ANY, u"Reload Last Patterns", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemReloadPattern.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh_small.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuFavSearch.AppendItem( self.m_menuItemReloadPattern )
		
		self.m_menuFavSearch.AppendSeparator()
		
		self.m_listCtrlFavs.Bind( wx.EVT_RIGHT_DOWN, self.m_listCtrlFavsOnContextMenu ) 
		
		bSizer40.Add( self.m_listCtrlFavs, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline842 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer40.Add( self.m_staticline842, 0, wx.EXPAND, 5 )
		
		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlSearch = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer151.Add( self.m_textCtrlSearch, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButtonSearch = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/magnifier.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer151.Add( self.m_bpButtonSearch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer40.Add( bSizer151, 0, wx.EXPAND, 5 )
		
		self.m_panel12.SetSizer( bSizer40 )
		self.m_panel12.Layout()
		bSizer40.Fit( self.m_panel12 )
		self.m_notebookFavs.AddPage( self.m_panel12, u"Search", False )
		
		bSizer18.Add( self.m_notebookFavs, 1, wx.EXPAND, 5 )
		
		self.m_panel6.SetSizer( bSizer18 )
		self.m_panel6.Layout()
		bSizer18.Fit( self.m_panel6 )
		self.m_notebookMain.AddPage( self.m_panel6, u"Markets", False )
		self.m_panel241 = wx.Panel( self.m_notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer82 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonCurrentBetsCollapse = wx.BitmapButton( self.m_panel241, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/application_view_list.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonCurrentBetsCollapse.SetToolTipString( u"Collapse All" )
		
		self.m_buttonCurrentBetsCollapse.SetToolTipString( u"Collapse All" )
		
		bSizer33.Add( self.m_buttonCurrentBetsCollapse, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonCurrentBetsLoadMarket = wx.BitmapButton( self.m_panel241, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_go.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonCurrentBetsLoadMarket.SetToolTipString( u"Load Market" )
		
		self.m_buttonCurrentBetsLoadMarket.SetToolTipString( u"Load Market" )
		
		bSizer33.Add( self.m_buttonCurrentBetsLoadMarket, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline841 = wx.StaticLine( self.m_panel241, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer33.Add( self.m_staticline841, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonCurrentBets = wx.BitmapButton( self.m_panel241, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonCurrentBets.Enable( False )
		self.m_buttonCurrentBets.SetToolTipString( u"Reload Current Bets" )
		
		self.m_buttonCurrentBets.Enable( False )
		self.m_buttonCurrentBets.SetToolTipString( u"Reload Current Bets" )
		
		bSizer33.Add( self.m_buttonCurrentBets, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxCurrentBetsAutoRefresh = wx.CheckBox( self.m_panel241, wx.ID_ANY, u"Auto Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBoxCurrentBetsAutoRefresh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer82.Add( bSizer33, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline55 = wx.StaticLine( self.m_panel241, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer82.Add( self.m_staticline55, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer382 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText40 = wx.StaticText( self.m_panel241, wx.ID_ANY, u"Bets: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		self.m_staticText40.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer382.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextCurrentBetsNum = wx.StaticText( self.m_panel241, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextCurrentBetsNum.Wrap( -1 )
		bSizer382.Add( self.m_staticTextCurrentBetsNum, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer82.Add( bSizer382, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3821 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText402 = wx.StaticText( self.m_panel241, wx.ID_ANY, u"Update: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )
		self.m_staticText402.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3821.Add( self.m_staticText402, 0, wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextCurrentBetsUpdate = wx.StaticText( self.m_panel241, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticTextCurrentBetsUpdate.Wrap( -1 )
		bSizer3821.Add( self.m_staticTextCurrentBetsUpdate, 1, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer82.Add( bSizer3821, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_notebookCurrentBets = wx.Notebook( self.m_panel241, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel25 = wx.Panel( self.m_notebookCurrentBets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer871 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrlCurrentBetsUK = wx.TreeCtrl( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES )
		self.m_menuCurrentBetsUK = wx.Menu()
		self.m_menuCurrentBetsLoadMarket = wx.MenuItem( self.m_menuCurrentBetsUK, wx.ID_ANY, u"Load Market", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCurrentBetsLoadMarket.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/page_go.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuCurrentBetsUK.AppendItem( self.m_menuCurrentBetsLoadMarket )
		
		self.m_menuCurrentBetsUK.AppendSeparator()
		
		self.m_menuItemCurrentBetsCancelBet = wx.MenuItem( self.m_menuCurrentBetsUK, wx.ID_ANY, u"Cancel Bet", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemCurrentBetsCancelBet.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuCurrentBetsUK.AppendItem( self.m_menuItemCurrentBetsCancelBet )
		
		self.m_menuItemCurrentBetsModifyBet = wx.MenuItem( self.m_menuCurrentBetsUK, wx.ID_ANY, u"Modify Bet ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemCurrentBetsModifyBet.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/application_form_edit.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuCurrentBetsUK.AppendItem( self.m_menuItemCurrentBetsModifyBet )
		
		self.m_treeCtrlCurrentBetsUK.Bind( wx.EVT_RIGHT_DOWN, self.m_treeCtrlCurrentBetsUKOnContextMenu ) 
		
		bSizer871.Add( self.m_treeCtrlCurrentBetsUK, 1, wx.EXPAND, 5 )
		
		self.m_panel25.SetSizer( bSizer871 )
		self.m_panel25.Layout()
		bSizer871.Fit( self.m_panel25 )
		self.m_notebookCurrentBets.AddPage( self.m_panel25, u"UK Wallet", True )
		self.m_panel26 = wx.Panel( self.m_notebookCurrentBets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8711 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrlCurrentBetsAus = wx.TreeCtrl( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES )
		self.m_menuCurrentBetsAus = wx.Menu()
		self.m_treeCtrlCurrentBetsAus.Bind( wx.EVT_RIGHT_DOWN, self.m_treeCtrlCurrentBetsAusOnContextMenu ) 
		
		bSizer8711.Add( self.m_treeCtrlCurrentBetsAus, 1, wx.EXPAND, 5 )
		
		self.m_panel26.SetSizer( bSizer8711 )
		self.m_panel26.Layout()
		bSizer8711.Fit( self.m_panel26 )
		self.m_notebookCurrentBets.AddPage( self.m_panel26, u"Aus Wallet", False )
		
		bSizer82.Add( self.m_notebookCurrentBets, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer83 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap13 = wx.StaticBitmap( self.m_panel241, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/drink_empty.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer83.Add( self.m_bitmap13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxCurrentBetsMatched = wx.CheckBox( self.m_panel241, wx.ID_ANY, u"Matched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCurrentBetsMatched.SetValue(True) 
		bSizer83.Add( self.m_checkBoxCurrentBetsMatched, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxCurrentBetsUnmatched = wx.CheckBox( self.m_panel241, wx.ID_ANY, u"Unmatched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCurrentBetsUnmatched.SetValue(True) 
		bSizer83.Add( self.m_checkBoxCurrentBetsUnmatched, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxCurrentBetsBack = wx.CheckBox( self.m_panel241, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCurrentBetsBack.SetValue(True) 
		bSizer83.Add( self.m_checkBoxCurrentBetsBack, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxCurrentBetsLay = wx.CheckBox( self.m_panel241, wx.ID_ANY, u"Lay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCurrentBetsLay.SetValue(True) 
		bSizer83.Add( self.m_checkBoxCurrentBetsLay, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer82.Add( bSizer83, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline59 = wx.StaticLine( self.m_panel241, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer82.Add( self.m_staticline59, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText401 = wx.StaticText( self.m_panel241, wx.ID_ANY, u"Bet Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )
		self.m_staticText401.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer82.Add( self.m_staticText401, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_listCtrlCurrentBetsInfo = wx.ListCtrl( self.m_panel241, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer82.Add( self.m_listCtrlCurrentBetsInfo, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel241.SetSizer( bSizer82 )
		self.m_panel241.Layout()
		bSizer82.Fit( self.m_panel241 )
		self.m_notebookMain.AddPage( self.m_panel241, u"Bets", False )
		self.m_panel9 = wx.Panel( self.m_notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetToolTipString( u"Refresh" )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, u"Modules" ), wx.VERTICAL )
		
		self.m_notebookModules = wx.Notebook( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_panel13 = wx.Panel( self.m_notebookModules, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer411 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText79 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )
		bSizer37.Add( self.m_staticText79, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_dirPickerBfModules = wx.DirPickerCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE )
		bSizer37.Add( self.m_dirPickerBfModules, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer411.Add( bSizer37, 0, wx.EXPAND, 5 )
		
		self.m_checkListBfModules = wx.CheckListBox( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), [], wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT ) 
		bSizer411.Add( self.m_checkListBfModules, 1, wx.EXPAND, 5 )
		
		self.bSizer69 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap12 = wx.StaticBitmap( self.m_panel13, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/plugin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer69.Add( self.m_bitmap12, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_toggleBfModules = wx.ToggleButton( self.m_panel13, wx.ID_ANY, u"Load Modules", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer69.Add( self.m_toggleBfModules, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.bSizer69.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonBfModulesOn = wx.BitmapButton( self.m_panel13, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/control_play_blue.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonBfModulesOn.Enable( False )
		self.m_buttonBfModulesOn.SetToolTipString( u"Start checked Modules" )
		
		self.m_buttonBfModulesOn.Enable( False )
		self.m_buttonBfModulesOn.SetToolTipString( u"Start checked Modules" )
		
		self.bSizer69.Add( self.m_buttonBfModulesOn, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonBfModulesPause = wx.BitmapButton( self.m_panel13, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/control_pause_blue.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonBfModulesPause.Enable( False )
		self.m_buttonBfModulesPause.SetToolTipString( u"Pause Modules" )
		
		self.m_buttonBfModulesPause.Enable( False )
		self.m_buttonBfModulesPause.SetToolTipString( u"Pause Modules" )
		
		self.bSizer69.Add( self.m_buttonBfModulesPause, 0, wx.ALL, 5 )
		
		bSizer411.Add( self.bSizer69, 0, wx.EXPAND, 5 )
		
		self.m_staticline73 = wx.StaticLine( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer411.Add( self.m_staticline73, 0, wx.EXPAND, 5 )
		
		self.m_notebookModuleParams = wx.Notebook( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebookModuleParams.Enable( False )
		
		self.m_panel22 = wx.Panel( self.m_notebookModuleParams, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer88 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlModParams = wx.ListCtrl( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer88.Add( self.m_listCtrlModParams, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonEditModParam = wx.BitmapButton( self.m_panel22, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_edit.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonEditModParam.Enable( False )
		self.m_buttonEditModParam.SetToolTipString( u"Edit Module Params" )
		
		self.m_buttonEditModParam.Enable( False )
		self.m_buttonEditModParam.SetToolTipString( u"Edit Module Params" )
		
		bSizer71.Add( self.m_buttonEditModParam, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModParamsSend = wx.BitmapButton( self.m_panel22, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_save.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModParamsSend.Enable( False )
		self.m_buttonModParamsSend.SetToolTipString( u"Send Params to Module" )
		
		self.m_buttonModParamsSend.Enable( False )
		self.m_buttonModParamsSend.SetToolTipString( u"Send Params to Module" )
		
		bSizer71.Add( self.m_buttonModParamsSend, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModParamsReload = wx.BitmapButton( self.m_panel22, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModParamsReload.Enable( False )
		self.m_buttonModParamsReload.SetToolTipString( u"Reload Params" )
		
		self.m_buttonModParamsReload.Enable( False )
		self.m_buttonModParamsReload.SetToolTipString( u"Reload Params" )
		
		bSizer71.Add( self.m_buttonModParamsReload, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModParamsDefaults = wx.BitmapButton( self.m_panel22, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/page_red.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModParamsDefaults.Enable( False )
		self.m_buttonModParamsDefaults.SetToolTipString( u"Defaults" )
		
		self.m_buttonModParamsDefaults.Enable( False )
		self.m_buttonModParamsDefaults.SetToolTipString( u"Defaults" )
		
		bSizer71.Add( self.m_buttonModParamsDefaults, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		bSizer88.Add( bSizer71, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel22.SetSizer( bSizer88 )
		self.m_panel22.Layout()
		bSizer88.Fit( self.m_panel22 )
		self.m_notebookModuleParams.AddPage( self.m_panel22, u"Params", True )
		self.m_panel23 = wx.Panel( self.m_notebookModuleParams, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer89 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkListModulesRunners = wx.CheckListBox( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, [], wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE ) 
		bSizer89.Add( self.m_checkListModulesRunners, 1, wx.EXPAND, 5 )
		
		bSizer90 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonModuleRunnersApply = wx.BitmapButton( self.m_panel23, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/table_save.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModuleRunnersApply.Enable( False )
		self.m_buttonModuleRunnersApply.SetToolTipString( u"Apply" )
		
		self.m_buttonModuleRunnersApply.Enable( False )
		self.m_buttonModuleRunnersApply.SetToolTipString( u"Apply" )
		
		bSizer90.Add( self.m_buttonModuleRunnersApply, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModuleRunnersRefresh = wx.BitmapButton( self.m_panel23, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/table_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer90.Add( self.m_buttonModuleRunnersRefresh, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModuleRunnersCheckAll = wx.BitmapButton( self.m_panel23, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/table_row_insert.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModuleRunnersCheckAll.SetToolTipString( u"Check all" )
		
		self.m_buttonModuleRunnersCheckAll.SetToolTipString( u"Check all" )
		
		bSizer90.Add( self.m_buttonModuleRunnersCheckAll, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonModuleRunnersUncheckAll = wx.BitmapButton( self.m_panel23, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/table_row_delete.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonModuleRunnersUncheckAll.SetToolTipString( u"Uncheck all" )
		
		self.m_buttonModuleRunnersUncheckAll.SetToolTipString( u"Uncheck all" )
		
		bSizer90.Add( self.m_buttonModuleRunnersUncheckAll, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		bSizer89.Add( bSizer90, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel23.SetSizer( bSizer89 )
		self.m_panel23.Layout()
		bSizer89.Fit( self.m_panel23 )
		self.m_notebookModuleParams.AddPage( self.m_panel23, u"Runners", False )
		self.m_scrolledWindowModActions = wx.ScrolledWindow( self.m_notebookModuleParams, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.m_scrolledWindowModActions.SetScrollRate( 5, 5 )
		self.m_scrolledWindowModActions.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.sizerModActions = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_scrolledWindowModActions.SetSizer( self.sizerModActions )
		self.m_scrolledWindowModActions.Layout()
		self.sizerModActions.Fit( self.m_scrolledWindowModActions )
		self.m_notebookModuleParams.AddPage( self.m_scrolledWindowModActions, u"Actions", False )
		
		bSizer411.Add( self.m_notebookModuleParams, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_panel13.SetSizer( bSizer411 )
		self.m_panel13.Layout()
		bSizer411.Fit( self.m_panel13 )
		self.m_notebookModules.AddPage( self.m_panel13, u"User", True )
		self.m_panelRecNPlay = wx.Panel( self.m_notebookModules, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText541 = wx.StaticText( self.m_panelRecNPlay, wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )
		bSizer38.Add( self.m_staticText541, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_dirPickerRecordAndPlay = wx.DirPickerCtrl( self.m_panelRecNPlay, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_USE_TEXTCTRL )
		bSizer38.Add( self.m_dirPickerRecordAndPlay, 1, wx.ALL, 5 )
		
		bSizer87.Add( bSizer38, 0, wx.EXPAND, 5 )
		
		bSizer392 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText58 = wx.StaticText( self.m_panelRecNPlay, wx.ID_ANY, u"CSV Sep", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		bSizer392.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRecordAndPlaySeparator = wx.TextCtrl( self.m_panelRecNPlay, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_textCtrlRecordAndPlaySeparator.SetMaxLength( 1 ) 
		bSizer392.Add( self.m_textCtrlRecordAndPlaySeparator, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer392.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBoxRecordAndPlayTabSeparator = wx.CheckBox( self.m_panelRecNPlay, wx.ID_ANY, u"Use tab as separator", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer392.Add( self.m_checkBoxRecordAndPlayTabSeparator, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer87.Add( bSizer392, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_toggleBtnRecord = wx.ToggleButton( self.m_panelRecNPlay, wx.ID_ANY, u"Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtnRecord.Enable( False )
		
		bSizer43.Add( self.m_toggleBtnRecord, 0, wx.ALL, 5 )
		
		self.m_toggleBtnPlay = wx.ToggleButton( self.m_panelRecNPlay, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_toggleBtnPlay, 0, wx.ALL, 5 )
		
		bSizer87.Add( bSizer43, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline65 = wx.StaticLine( self.m_panelRecNPlay, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer87.Add( self.m_staticline65, 0, wx.EXPAND, 5 )
		
		self.m_panelRecNPlay.SetSizer( bSizer87 )
		self.m_panelRecNPlay.Layout()
		bSizer87.Fit( self.m_panelRecNPlay )
		self.m_notebookModules.AddPage( self.m_panelRecNPlay, u"Rec && Play", False )
		self.m_panel351 = wx.Panel( self.m_notebookModules, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer106 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1081 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButtonExcelUpdateWorkbooks = wx.BitmapButton( self.m_panel351, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer1081.Add( self.m_bpButtonExcelUpdateWorkbooks, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText88 = wx.StaticText( self.m_panel351, wx.ID_ANY, u"(Re)Load Workbooks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		bSizer1081.Add( self.m_staticText88, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer1081.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline70 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1081.Add( self.m_staticline70, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		
		bSizer1081.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText89 = wx.StaticText( self.m_panel351, wx.ID_ANY, u"Open new Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )
		bSizer1081.Add( self.m_staticText89, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_bpButtonExcelOpen = wx.BitmapButton( self.m_panel351, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/table_add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer1081.Add( self.m_bpButtonExcelOpen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer106.Add( bSizer1081, 0, wx.EXPAND, 5 )
		
		self.m_staticline641 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer106.Add( self.m_staticline641, 0, wx.EXPAND, 5 )
		
		bSizer1112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButtonExcelPlay = wx.BitmapButton( self.m_panel351, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/control_play_blue.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonExcelPlay.SetToolTipString( u"Load module and start Excel betting" )
		
		self.m_bpButtonExcelPlay.SetToolTipString( u"Load module and start Excel betting" )
		
		bSizer1112.Add( self.m_bpButtonExcelPlay, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bpButtonExcelPause = wx.BitmapButton( self.m_panel351, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/control_pause_blue.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonExcelPause.Enable( False )
		self.m_bpButtonExcelPause.SetToolTipString( u"Pause Excel betting" )
		
		self.m_bpButtonExcelPause.Enable( False )
		self.m_bpButtonExcelPause.SetToolTipString( u"Pause Excel betting" )
		
		bSizer1112.Add( self.m_bpButtonExcelPause, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_bpButtonExcelStop = wx.BitmapButton( self.m_panel351, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/control_stop_blue.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonExcelStop.Enable( False )
		self.m_bpButtonExcelStop.SetToolTipString( u"Stop Excel betting and unload module" )
		
		self.m_bpButtonExcelStop.Enable( False )
		self.m_bpButtonExcelStop.SetToolTipString( u"Stop Excel betting and unload module" )
		
		bSizer1112.Add( self.m_bpButtonExcelStop, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer106.Add( bSizer1112, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6413 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer106.Add( self.m_staticline6413, 0, wx.EXPAND, 5 )
		
		bSizer110 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText861 = wx.StaticText( self.m_panel351, wx.ID_ANY, u"Starting cell:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText861.Wrap( -1 )
		bSizer110.Add( self.m_staticText861, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlExcelCell = wx.TextCtrl( self.m_panel351, wx.ID_ANY, u"A1", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer110.Add( self.m_textCtrlExcelCell, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer110.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline71 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer110.Add( self.m_staticline71, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer106.Add( bSizer110, 0, wx.EXPAND, 5 )
		
		self.m_staticline6412 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer106.Add( self.m_staticline6412, 0, wx.EXPAND, 5 )
		
		bSizer107 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText852 = wx.StaticText( self.m_panel351, wx.ID_ANY, u"Workbooks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText852.Wrap( -1 )
		bSizer107.Add( self.m_staticText852, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer106.Add( bSizer107, 0, 0, 5 )
		
		self.m_checkListExcelWorkbooks = wx.CheckListBox( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), [], wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE|wx.LB_SORT ) 
		bSizer106.Add( self.m_checkListExcelWorkbooks, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		self.m_staticline6411 = wx.StaticLine( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer106.Add( self.m_staticline6411, 0, wx.EXPAND, 5 )
		
		bSizer109 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText87 = wx.StaticText( self.m_panel351, wx.ID_ANY, u"Sheets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )
		bSizer109.Add( self.m_staticText87, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer106.Add( bSizer109, 0, wx.EXPAND, 5 )
		
		self.m_checkListExcelSheets = wx.CheckListBox( self.m_panel351, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), [], wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE|wx.LB_SORT ) 
		bSizer106.Add( self.m_checkListExcelSheets, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		self.m_panel351.SetSizer( bSizer106 )
		self.m_panel351.Layout()
		bSizer106.Fit( self.m_panel351 )
		self.m_notebookModules.AddPage( self.m_panel351, u"Excel", False )
		
		sbSizer7.Add( self.m_notebookModules, 1, wx.EXPAND, 5 )
		
		bSizer41.Add( sbSizer7, 3, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, u"Module Logging" ), wx.VERTICAL )
		
		m_listBoxModLoggingChoices = []
		self.m_listBoxModLogging = wx.ListBox( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_listBoxModLoggingChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
		self.m_menuModLogging = wx.Menu()
		self.m_menuItemModLoggingSelectAll = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Select All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingSelectAll )
		
		self.m_menuItemModLoggingDeselectAll = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Deselect All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingDeselectAll )
		
		self.m_menuItemModLoggingClearAll = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Clear All Messages", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingClearAll )
		
		self.m_menuItemModLoggingClearSelected = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Clear Selected", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingClearSelected )
		
		self.m_menuItemModLoggingCopyAll = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Copy All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingCopyAll )
		
		self.m_menuItemModLoggingCopySelected = wx.MenuItem( self.m_menuModLogging, wx.ID_ANY, u"Copy Selected", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuModLogging.AppendItem( self.m_menuItemModLoggingCopySelected )
		
		self.m_listBoxModLogging.Bind( wx.EVT_RIGHT_DOWN, self.m_listBoxModLoggingOnContextMenu ) 
		
		sbSizer11.Add( self.m_listBoxModLogging, 1, wx.EXPAND, 5 )
		
		bSizer41.Add( sbSizer11, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_panel9.SetSizer( bSizer41 )
		self.m_panel9.Layout()
		bSizer41.Fit( self.m_panel9 )
		self.m_notebookMain.AddPage( self.m_panel9, u"Modules", False )
		self.m_panel66 = wx.Panel( self.m_notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer165 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook16 = wx.Notebook( self.m_panel66, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel67 = wx.Panel( self.m_notebook16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer166 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl34 = wx.TextCtrl( self.m_panel67, wx.ID_ANY, u"Bfplusplus is a graphical interface to the Betfair Betting Exchange using the Betfair API\n\nCopyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)\nCopyright (C) 2011 Sensible Odds Ltd.\n\nYou can learn more and contact the author at:\n\n    http://code.google.com/p/bfplusplus/\n\nBfplusplus is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nBfplusplus is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License along with Bfplusplus.  If not, see <http://www.gnu.org/licenses/>.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer166.Add( self.m_textCtrl34, 1, wx.EXPAND, 5 )
		
		self.m_panel67.SetSizer( bSizer166 )
		self.m_panel67.Layout()
		bSizer166.Fit( self.m_panel67 )
		self.m_notebook16.AddPage( self.m_panel67, u"About", True )
		self.m_panel68 = wx.Panel( self.m_notebook16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer167 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl35 = wx.TextCtrl( self.m_panel68, wx.ID_ANY, u"GNU GENERAL PUBLIC LICENSE\n\nVersion 3, 29 June 2007\n\nCopyright © 2007 Free Software Foundation, Inc. <http://fsf.org/>\n\nEveryone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.\n\nPreamble\n\nThe GNU General Public License is a free, copyleft license for software and other kinds of works.\n\nThe licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.\n\nWhen we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.\n\nTo protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.\n\nFor example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.\n\nDevelopers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.\n\nFor the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.\n\nSome devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.\n\nFinally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.\n\nThe precise terms and conditions for copying, distribution and modification follow.\n\nTERMS AND CONDITIONS\n\n0. Definitions.\n“This License” refers to version 3 of the GNU General Public License.\n\n“Copyright” also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.\n\n“The Program” refers to any copyrightable work licensed under this License. Each licensee is addressed as “you”. “Licensees” and “recipients” may be individuals or organizations.\n\nTo “modify” a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a “modified version” of the earlier work or a work “based on” the earlier work.\n\nA “covered work” means either the unmodified Program or a work based on the Program.\n\nTo “propagate” a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.\n\nTo “convey” a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.\n\nAn interactive user interface displays “Appropriate Legal Notices” to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.\n\n1. Source Code.\nThe “source code” for a work means the preferred form of the work for making modifications to it. “Object code” means any non-source form of a work.\n\nA “Standard Interface” means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.\n\nThe “System Libraries” of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A “Major Component”, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.\n\nThe “Corresponding Source” for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.\n\nThe Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.\n\nThe Corresponding Source for a work in source code form is that same work.\n\n2. Basic Permissions.\nAll rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.\n\nYou may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.\n\nConveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.\n\n3. Protecting Users' Legal Rights From Anti-Circumvention Law.\nNo covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.\n\nWhen you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.\n\n4. Conveying Verbatim Copies.\nYou may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.\n\nYou may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.\n\n5. Conveying Modified Source Versions.\nYou may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:\n\na) The work must carry prominent notices stating that you modified it, and giving a relevant date.\nb) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.\nc) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.\nd) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.\nA compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.\n\n6. Conveying Non-Source Forms.\nYou may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:\n\na) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.\nb) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.\nc) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.\nd) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.\ne) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.\nA separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.\n\nA “User Product” is either (1) a “consumer product”, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, “normally used” refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.\n\n“Installation Information” for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.\n\nIf you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).\n\nThe requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.\n\nCorresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.\n\n7. Additional Terms.\n“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.\n\nWhen you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.\n\nNotwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:\n\na) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or\nb) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or\nc) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or\nd) Limiting the use for publicity purposes of names of licensors or authors of the material; or\ne) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or\nf) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.\nAll other non-permissive additional terms are considered “further restrictions” within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.\n\nIf you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.\n\nAdditional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.\n\n8. Termination.\nYou may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).\n\nHowever, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.\n\nMoreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.\n\nTermination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.\n\n9. Acceptance Not Required for Having Copies.\nYou are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so.\n\n10. Automatic Licensing of Downstream Recipients.\nEach time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.\n\nAn “entity transaction” is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.\n\nYou may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.\n\n11. Patents.\nA “contributor” is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's “contributor version”.\n\nA contributor's “essential patent claims” are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, “control” includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.\n\nEach contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.\n\nIn the following three paragraphs, a “patent license” is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To “grant” such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.\n\nIf you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. “Knowingly relying” means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.\n\nIf, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.\n\nA patent license is “discriminatory” if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.\n\nNothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.\n\n12. No Surrender of Others' Freedom.\nIf conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.\n\n13. Use with the GNU Affero General Public License.\nNotwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.\n\n14. Revised Versions of this License.\nThe Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.\n\nEach version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.\n\nIf the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statemen", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer167.Add( self.m_textCtrl35, 1, wx.EXPAND, 5 )
		
		self.m_panel68.SetSizer( bSizer167 )
		self.m_panel68.Layout()
		bSizer167.Fit( self.m_panel68 )
		self.m_notebook16.AddPage( self.m_panel68, u"License/Copying", False )
		self.m_panel69 = wx.Panel( self.m_notebook16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer168 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl36 = wx.TextCtrl( self.m_panel69, wx.ID_ANY, u"Bfplusplus has been developed using the following components, editors, utilities, operating systems and content:\n\nPython 2.6/2.7 (or later), a programming language that lets you work more quickly and integrate your systems more effectively. If you want to learn more about Python please visit <http://www.python.org>\n\nwxPython 2.8.11.0 (or later), a blending of the wxWidgets C++ class library with the Python programming language. If you want to learn more please visit <http://www.wxpython.org>\n\nwxFormBuilder 3.1.70 (or later), an OpenSource wxWidgets (C++, wxPython, XRC) Designer, GUI Builder, and RAD Tool. If you want to learn more please visit <http://wxformbuilder.org>\n\nbfpy 0.50 (or later), a Betfair communications library. If you want to learn more please visit <http://code.google.com/p/bfpy>\n\nsuds 0.3.9 (or later), a lightweight SOAP python client for consuming Web Services. If you want to learn more please visit <https://fedorahosted.org/suds/>. suds may be embedded in bfpy\n\nhttxlib 0.90 (or later), a HTTP library for Python. If you want to learn more please visit <http://code.google.com/p/httxlib>\n\nSlowAES (rev 38 or later), a implementations of AES in pure scripting languages. If you want to learn more please visit <http://code.google.com/p/slowaes/>\n\nPyInstaller 1.4 (or later), a program that converts (packages) Python programs into stand-alone executables. If you want to learn more please visit <http://www.pyinstaller.org/>\n\nInnoSetup 5.3.11 (or later), apowerful script based freeware installation builder for Windows. If you want to learn more please visit <http://www.jrsoftware.org/isinfo.php>\n\nInnoIDE 1.0.0.0051 (or later), a brand new interface for generating Microsoft Windows installations using InnoSetup. If you want to learn more please visit <http://www.innoide.org/>\n\nXEmacs 21.4 (patch 22) \"Instant Classic\" (or later), a highly customizable open source text editor and application development system. If you want to learn more please visit <htt://www.xemacs.org>\n\nIcoFX 1.6.4 (or later), a Freeware Icon Editor. If you want to learn more please visit <http://icofx.ro>\n\nMSYS 1.0.11 (or later), a contraction of \"Minimal SYStem\", is a Bourne Shell command line interpreter system. Offered as an alternative to Microsoft's cmd.exe, this provides a general purpose command line environment. If you want to learn more, please visit <http://www.mingw.org>\n\nCygwin 1.7.7 (or later), a Linux-like environment for Windows. If you want to learn more please visit: <http://www.cygwin.com/>\n\ngit 1.7.2.3 (or later), a free & open source, distributed version control system. If you want to learn more please visit <http://git-scm.com/>\n\nWindows XP SP3 (or later), an operating system developed by Microsoft. If you want to learn more please visit <http://www.microsoft.com>\n\n--------------------------------------\n\nSome of the programs or libraries mentioned above, do use other libraries and tools from the OpenSource world (like libpng, libjpeg, zlib and others). Although there is no direct usage of them in this program, credit has to be given to all the libraries and the authors that developed them.\n\n--------------------------------------\nIcons from the sets of icons have been used:\n\nFamFamFam Silk (licensed under Creative Commons Attribution 2.5 License). If you want to learn more please visit: <http://www.famfamfam.com/lab/icons/silk/>\n\nFamFamFam Flags (free for use for any purpose with no requirements for attribution) If you want to learn more please visit: <http://www.famfamfam.com/lab/icons/flags/>\n\nLid Grid 2007 (Free for non-commercial use) If you want to learn more please visit <http://www.antdavidson.com>\n\nSport Icon Set from the Nordic Factory (free, please link back to www.nordicfactory.com when using these icons) If you want to learn more please visit <http://www.nordicfactory.com>\n\nIcon from Everaldo.com (licensed under the LGPL - a copy should be found with this program - if you haven't received the copy, please visit <http://www.gnu.org/licenses/>) If you want to learn more please visit <http://www.everaldo.com/>\n\nIcon from Wikimedia (in the public domain, from Amada44). If you want to learn more please visit <http://commons.wikimedia.org>\n\nIcon from Zeus Box Studio. Released as Freeware. If you want to learn more please visit <http://www.zeusboxstudio.com>\n\n", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer168.Add( self.m_textCtrl36, 1, wx.EXPAND, 5 )
		
		self.m_panel69.SetSizer( bSizer168 )
		self.m_panel69.Layout()
		bSizer168.Fit( self.m_panel69 )
		self.m_notebook16.AddPage( self.m_panel69, u"Credits", False )
		self.m_panel70 = wx.Panel( self.m_notebook16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer169 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl37 = wx.TextCtrl( self.m_panel70, wx.ID_ANY, u"This program and the automated betting facilities provided will not improve your betting abilities/skills nor guarantees error free operation (read the LICENSE) and is provided AS IS.\n\nGambling is an addictive activity that can cause severe financial losses. If you think that you may have developed an addition please visit <http://www.gamcare.co.uk> or other similar organisation\n\nPlease bear in mind that in Betting Exchanges (like Betfair) you may be betting against automated software developed by other users or against automated software developed by third parties and under the control of other users. The connection of such software, functionalities, fitness of algorithms may be better than that provided by this software and/or the modules developed for use with this software by you or by third parties.\n\nPlease bear in mind that (as pointed out by Betting Exchanges like Betfair) transmissions described as \"Live\" by broadcasters may be delayed and that other users and/or software tools may have more accurate and up to date information than you or this software may have.\n\nPleae bear in mind that other users and of software tools may have quicker and/or shorter network links and therefore may find themselves in an advantageous position when compared to the network link length and/or speed available to you and this software", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer169.Add( self.m_textCtrl37, 1, wx.EXPAND, 5 )
		
		self.m_panel70.SetSizer( bSizer169 )
		self.m_panel70.Layout()
		bSizer169.Fit( self.m_panel70 )
		self.m_notebook16.AddPage( self.m_panel70, u"Gambling", False )
		self.m_panel71 = wx.Panel( self.m_notebook16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer170 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl38 = wx.TextCtrl( self.m_panel71, wx.ID_ANY, u"Betfair:\n\nThis application uses the Betfair Betting Exchange and the API. If you want to learn more, please visit: <http://www.betfair.com>\n\nBefair Data Charges Page:\n\nIf you request too many data (for data that falls under Data Request Charging Scheme), charges may apply. If you want to learn more, please visit: <http://content.betfair.com/aboutus/content.asp?product=exchange&region=GBR&locale=en_GB&brand=betfair&sWhichKey=Betfair%20Charges>\n\n\n#summary Beftair Verification Compliance\n\n= Reference =\nThe Betfair requirements for Vendor Software Certification can be found at:\n  * http://bdp.betfair.com/index.php?option=com_content&task=view&id=76&Itemid=68\n\n= Background =\nThe Vendor Software Certification process that Betfair created is geared towards closed source proprietary applications and hence it is impossible for an Open Source application to fully comply with them, since some of the requirements are about \"information hiding\" (like hiding the assigned **vendorSoftwareId**. Obviously if the sources can be read by anyone, so can the **vendorSoftwareId**, that has to be somewhere in the code to be used.\n\n= Summary =\n\nAfter doing a self-test of all requirements the results are:\n\n * Compliant: 18\n * Partially Compliant: 1\n * Non Compliant: 0\n * Not Applicable: 9\n\n (The entire \"Advertising and Marketing Guidelines\" section is \"Not Applicable\")\n\n= Compliance =\n\n== Security Authorisation Checklist ==\n\n  * An application may not communicate with the API through a proxy of any description. All communications must be directly with the API and must be over a secure channel.\n\n    _Compliant_: Bfplusplus communicates directly with the API and always over HTTPS\n\n  * A Vendor must not have visibility of a user's Betfair username, password or any other sensitive data that may link a user of a product to a Betfair account.\n\n    _Compliant_: Bfplusplus communicates directly with the API and therefore the *Vendor* (author or authors of the software) have no visibility of either Betfair usernames, passwords or any other information\n\n  * An application must communicate directly with Betfair via the API to validate a customer.\n\n    _Compliant_: Bfplusplus communicates directly with the API\n\n  * An application must never store or log the user's Betfair password.\n\n    _Compliant_: Bfplusplus never stores or logs the user's Betfair password\n\n  * An application must not store or log the username (locally - file system or registry) in plain text.  If the user has chosen to store their username locally (by performing an explicit action to indicate their wish to do so) it should be encrypted (AES with minimum 128 bits key length).\n\n    _Compliant_: Bfplusplus stores usernames locally with AES and a 128 bit key. Their user can choose whether to store usernames or not\n\n  * An application must display an agree/disagree model dialog to the user when the user indicates a desire to store their username locally. The default action of the dialog should be to not save the username.\n\n    _Compliant_: Bfplusplus presents the choice in the main panel after application start. The default action is not save the username\n\n  * An application may not implement automatic login as this would require the application storing the password locally.\n\n    _Compliant_: Bfplusplus does not implement an auto-login feature\n\n  * An application must use the Vendor-registered user ID (not Betfair) credentials to validate subscription, fetch news, update the application and all other Vendor/application specific communication.\n\n    _Not Applicable_: Bfplusplus doesn't have a *vendorSoftwareId* and doesn't use the specific Betfair Vendor API. None of the aforementioned actions are performed anyhow using any kind of user Id (Betfair or not)\n\n  * A Vendor must, at minimum, provide an md5 checksum ensuring that customer has a method of checking that the program they are installing is the same file the Security Certified version.\n\n    _Compliant_: The downloads from code.google.com have a SHA-1 (stronger than MD-5) signature for download verification. Being Bfplusplus an Open Source application, those downloading the sources can always verify their goodness.\n\n  * The provisioning (where applicable) of the account to use a Vendor product with the Betfair API must be via the Vendor Services API or Vendor Console - see Part II\n\n    _Not Applicable_: Bfplusplus doesn't do any kind of provisioning\n\n*Result*: 8 Compliant, 2 Not Applicable, 0 Non Compliant\n\n== Product Requirements ==\n\n=== Gambling Commission Requirement ===\n\n  * Where customers hold a credit or debit balance, the pages or screens used to move money into and out of accounts or products must be designed to display the customer’s current account or product balance, either in the currency of their account or the currency of the gambling product (e.g. dollars, euros or pounds sterling), whenever that customer is logged in.\n\n    _Not Applicable_: The product doesn't feature any feature to move money into and/or out the customer's account\n\n  * Where customers hold a credit or debit balance, the pages or screens used for gambling must be designed to display the customer’s current account or product balance, or where this is not practical to display a link to a page or screen that shows the balance, whenever that customer is logged in. Balances are to be presented either in the currency of the customer’s account or the currency of the gambling product (e.g. dollars, euros or pounds sterling).\n\n    _Compliant_: Funds are presented when the customer is logged in (unless the customer chooses to hide them) in the currency of the customer's account\n\n  * The gambling system must be designed to display sufficient relevant information about the customer’s gamble so that the content of the gamble is clear. This information must be made available before the customer commits to the gamble, including for example, in the artwork and textual information displayed during gaming, or on an electronic equivalent of a betting slip or lottery ticket.\n\n    _Compliant_: all available information is made available to the customer and unless the customer specifically chooses \"1-click betting\", all information about a gamble is made available prior to gample placement\n\n  * Where the gambling system uses full screen client applications that obscure the clock on the customer’s device the client application itself must display the time of day or the elapsed time since the application was started, wherever practicable.\n\n    _Compliant_: The application does not use a full screen mode and does not obscure the clock on the customer's dive\n\n  * Gambling products must not actively encourage customers to chase their losses, increase their stake or increase the amount they have decided to gamble, or continue to gamble after they have indicated that they wish to stop.\n\n    _Compliant_: No encouragement of any type is made\n\n  * Where peer-to-peer(s) customers may be gambling against programs deployed by other customers to play on their behalf, information should be made available that describes that this is possible, and if it is against the operator’s terms and conditions to use robots, how to report suspected robot use.\n\n    _Compliant_: Described in the GAMBLING tab and text file\n\n  * For time-critical events, the customer should be informed (through for example a notice at the software log-in or a warning notice within the software) that they might be at a disadvantage because of technical issues such as slower network speeds, or slower end user device performance.\n\n    _Compliant_: Described in the GAMBLING tab and text file\n\n*Result*: 6 Compliant, 1 Not Applicable\n\n=== Advertising and Marketing in the UK ===\n\n  The software does not do any kind of advertising or marketing\n\n*Result*: Not Applicable\n\n=== Data Request Management ====\nThe description of this section is convered by the checklist of the next section\n\n\n=== Product Authorisation Checklist ====\n\n  * The application includes a data request counter that accurately counts requests that fall under the Data Request charging scheme. The application by default should be throttled to make no more than 10 data requests per second.\n\n  _Partially Compliant_: The counter is not included. The application design and the use of the Free API prevent issuing more than 10 data requests (that fall under the Data Request Charging scheme) per second\n\n  * The application includes a link to the Betfair Charges page for customer reference\n\n    _Compliant_: A link is included in the application\n\n  * The application requests gzipped responses from the API\n\n    _Compliant_: The application requests gzipped responses and supports also zlib and bzip2 responses (and requests them)\n\n  * The application supports forced updates to customers\n\n    _Compliant_: Customers can change refresh periods and force update of current bets, all within the limits of the Free API (and therefore those of the Data Request Charging scheme)\n\n  * The application does not make any more than five market prices requests, per market in any one second\n\n    _Compliant_: Even if the customer chooses to use their own Personal API Product Id the application doesn't allow more than 5 requests per second per market\n\n  * The application does not reveal the assigned vendorSoftwareId to users\n\n    _Not Applicable_: The application doesn't have or use a vendorSoftwareId (therefore it could also be considered *Compliant*, since the vendorSoftwareId isn't revealed)\n\n*Result*: 4 Compliant, 1 Not Applicable, 0 Non Compliant, 1 Partially Compliant\n\n== User Provisioning ==\n\n  * User registers with the Vendor on their website (using separate credentials from their Betfair username and password)\n\n    _Not Applicable_: Bfplusplus has no website to provision users or assign user credentials. The application (and therefore the user) communicates directly with the Betfair API.\n\n  * On success, the user is forwarded to a secure Betfair validation service (Vendor Services API)\n\n    _Not Applicable_: See above\n\n  * The user enters their access request token, and then their Betfair username and password.\n\n    _Not Applicable_: See above\n\n  * The Vendor username and the Betfair username are then mapped by a ClientId and the relationship is managed by Betfair\n\n    _Not Applicable_: See above\n\n  * The Vendor may now interact with the Betfair account via Vendor Services using only the ClientId - the Betfair username shall not be used\n\n    _Not Applicable_: See above\n\n*Result*: 0 Compliant, 5 Not Applicable, 0 Non Compliant", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer170.Add( self.m_textCtrl38, 1, wx.EXPAND, 5 )
		
		self.m_panel71.SetSizer( bSizer170 )
		self.m_panel71.Layout()
		bSizer170.Fit( self.m_panel71 )
		self.m_notebook16.AddPage( self.m_panel71, u"Betfair", False )
		
		bSizer165.Add( self.m_notebook16, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_panel66.SetSizer( bSizer165 )
		self.m_panel66.Layout()
		bSizer165.Fit( self.m_panel66 )
		self.m_notebookMain.AddPage( self.m_panel66, u"About", False )
		
		bSizer66.Add( self.m_notebookMain, 1, wx.EXPAND, 5 )
		
		self.m_panelMainLeft.SetSizer( bSizer66 )
		self.m_panelMainLeft.Layout()
		bSizer66.Fit( self.m_panelMainLeft )
		bSizer35.Add( self.m_panelMainLeft, 0, wx.EXPAND, 5 )
		
		self.m_staticline74 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.LI_VERTICAL )
		bSizer35.Add( self.m_staticline74, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panelMainRight = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindowMainRight = wx.ScrolledWindow( self.m_panelMainRight, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL )
		self.m_scrolledWindowMainRight.SetScrollRate( 5, 5 )
		self.bSizerScrollWindow = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelScrolled = wx.Panel( self.m_scrolledWindowMainRight, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer117 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap16 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/time.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_bitmap16, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText101 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Updated at", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		bSizer181.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextRefreshTime = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextRefreshTime.Wrap( -1 )
		self.m_staticTextRefreshTime.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer181.Add( self.m_staticTextRefreshTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer111.Add( bSizer181, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline69 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer111.Add( self.m_staticline69, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer1811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmapExchange = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/world.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 16,16 ), 0 )
		self.m_menuWallet = wx.Menu()
		self.m_menuItemLoadGUIModules = wx.MenuItem( self.m_menuWallet, wx.ID_ANY, u"Beta - Load GUI Modules", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuWallet.AppendItem( self.m_menuItemLoadGUIModules )
		
		self.m_bitmapExchange.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmapExchangeOnContextMenu ) 
		
		bSizer1811.Add( self.m_bitmapExchange, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText191 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Wallet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		bSizer1811.Add( self.m_staticText191, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer111.Add( bSizer1811, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline2111 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer111.Add( self.m_staticline2111, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer18111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap25 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/information.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18111.Add( self.m_bitmap25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextMarketType = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextMarketType.Wrap( -1 )
		self.m_staticTextMarketType.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer18111.Add( self.m_staticTextMarketType, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer111.Add( bSizer18111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer111.Add( self.m_staticline21, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer181111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap17 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/clock.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181111.Add( self.m_bitmap17, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText11111 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText11111.Wrap( -1 )
		bSizer181111.Add( self.m_staticText11111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextStartTime = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextStartTime.Wrap( -1 )
		self.m_staticTextStartTime.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer181111.Add( self.m_staticTextStartTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer111.Add( bSizer181111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer111.Add( self.m_staticline31, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
		
		bSizer1811111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap18 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/medal_gold_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1811111.Add( self.m_bitmap18, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText1111121 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Winners", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText1111121.Wrap( -1 )
		bSizer1811111.Add( self.m_staticText1111121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextWinners = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextWinners.Wrap( -1 )
		self.m_staticTextWinners.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer1811111.Add( self.m_staticTextWinners, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer111.Add( bSizer1811111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline311 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer111.Add( self.m_staticline311, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer18111111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap22 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/television.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18111111.Add( self.m_bitmap22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText111112 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"In-Play", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText111112.Wrap( -1 )
		bSizer18111111.Add( self.m_staticText111112, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_bitmapInPlay = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/cancel.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18111111.Add( self.m_bitmapInPlay, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticline31111 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer18111111.Add( self.m_staticline31111, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bitmap23 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/time_add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap23.SetToolTipString( u"In-Play bet delay" )
		
		bSizer18111111.Add( self.m_bitmap23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextInPlayDelay = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextInPlayDelay.Wrap( -1 )
		self.m_staticTextInPlayDelay.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer18111111.Add( self.m_staticTextInPlayDelay, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText901 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText901.Wrap( -1 )
		bSizer18111111.Add( self.m_staticText901, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer111.Add( bSizer18111111, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer117.Add( bSizer111, 0, wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline221111 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer117.Add( self.m_staticline221111, 0, wx.EXPAND, 5 )
		
		bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer178 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap8 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/coins.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer178.Add( self.m_bitmap8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxShowProfitAndLoss = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Show P&&L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxShowProfitAndLoss.SetValue(True) 
		bSizer178.Add( self.m_checkBoxShowProfitAndLoss, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer1111.Add( bSizer178, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline79 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1111.Add( self.m_staticline79, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer179 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap9 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/calculator.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer179.Add( self.m_bitmap9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxDisplayPercPrices = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Show Price %", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer179.Add( self.m_checkBoxDisplayPercPrices, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer1111.Add( bSizer179, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline80 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1111.Add( self.m_staticline80, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1171 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap19 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/tick.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1171.Add( self.m_bitmap19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxVerifyBets = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Verify bets", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1171.Add( self.m_checkBoxVerifyBets, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_checkBoxVerifyRClickBets = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u" && right-click", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer1171.Add( self.m_checkBoxVerifyRClickBets, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer1111.Add( bSizer1171, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline77 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1111.Add( self.m_staticline77, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/mouse.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer119.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_checkBoxSingleClickBetting = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"1-click bets", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer119.Add( self.m_checkBoxSingleClickBetting, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer1111.Add( bSizer119, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline691 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1111.Add( self.m_staticline691, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer118 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap251 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/money.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer118.Add( self.m_bitmap251, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"1-Stake", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		self.m_staticText91.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer118.Add( self.m_staticText91, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_buttonQuickStakes = OptionButton( self.m_panelScrolled, wx.ID_ANY, u"1000.0", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.NO_BORDER )
		bSizer118.Add( self.m_buttonQuickStakes, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1111.Add( bSizer118, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline81 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1111.Add( self.m_staticline81, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer174 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap24 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/money_arrow_back_red.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer174.Add( self.m_bitmap24, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxSingleClickLiability = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Stake is Liability", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer174.Add( self.m_checkBoxSingleClickLiability, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer1111.Add( bSizer174, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer117.Add( bSizer1111, 0, wx.EXPAND, 5 )
		
		self.m_staticline22111 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer117.Add( self.m_staticline22111, 0, wx.EXPAND, 5 )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer175 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonExpandEvents = wx.BitmapButton( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/application_side_tree.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonExpandEvents.Enable( False )
		self.m_buttonExpandEvents.SetToolTipString( u"Market Tree" )
		
		self.m_buttonExpandEvents.Enable( False )
		self.m_buttonExpandEvents.SetToolTipString( u"Market Tree" )
		
		bSizer175.Add( self.m_buttonExpandEvents, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText941 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Expand Market", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText941.Wrap( -1 )
		bSizer175.Add( self.m_staticText941, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer96.Add( bSizer175, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline6311 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer96.Add( self.m_staticline6311, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonSaveAsFav = wx.BitmapButton( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/disk.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_buttonSaveAsFav.Enable( False )
		self.m_buttonSaveAsFav.SetToolTipString( u"Save Market as Favourite" )
		
		self.m_buttonSaveAsFav.Enable( False )
		self.m_buttonSaveAsFav.SetToolTipString( u"Save Market as Favourite" )
		
		bSizer173.Add( self.m_buttonSaveAsFav, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText111 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Save Market", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		bSizer173.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer96.Add( bSizer173, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline92 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer96.Add( self.m_staticline92, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer177 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap26 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer177.Add( self.m_bitmap26, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxTicksAway = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Bet at", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer177.Add( self.m_checkBoxTicksAway, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_spinCtrlTicksFromPrice = wx.SpinCtrl( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, -50, 50, 0 )
		bSizer177.Add( self.m_spinCtrlTicksFromPrice, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText921 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText921.Wrap( -1 )
		bSizer177.Add( self.m_staticText921, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer96.Add( bSizer177, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline701 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer96.Add( self.m_staticline701, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
		
		bSizer176 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap261 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer176.Add( self.m_bitmap261, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_checkBoxCompAway = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Compensate at", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCompAway.SetToolTipString( u"Place compensations also away from price" )
		
		bSizer176.Add( self.m_checkBoxCompAway, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_spinCtrlTicksFromComp = wx.SpinCtrl( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, -50, 50, 0 )
		bSizer176.Add( self.m_spinCtrlTicksFromComp, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText9211 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"ticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9211.Wrap( -1 )
		bSizer176.Add( self.m_staticText9211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer96.Add( bSizer176, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline83 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer96.Add( self.m_staticline83, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer100 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap32 = wx.StaticBitmap( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/basket_put_delete.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_bitmap32, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxFillOrKill = wx.CheckBox( self.m_panelScrolled, wx.ID_ANY, u"Fill or Kill in", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_checkBoxFillOrKill, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrlFillOrKill = wx.SpinCtrl( self.m_panelScrolled, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 999, 15 )
		bSizer100.Add( self.m_spinCtrlFillOrKill, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText82 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"sec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		bSizer100.Add( self.m_staticText82, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		bSizer96.Add( bSizer100, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer117.Add( bSizer96, 0, wx.EXPAND, 5 )
		
		self.m_staticline2211 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer117.Add( self.m_staticline2211, 0, wx.EXPAND, 5 )
		
		bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButtonPanelShowHide = wx.BitmapButton( self.m_panelScrolled, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/application_side_contract.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonPanelShowHide.SetToolTipString( u"Show/Hide main panel" )
		
		self.m_bpButtonPanelShowHide.SetToolTipString( u"Show/Hide main panel" )
		
		bSizer172.Add( self.m_bpButtonPanelShowHide, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticTextShowHidePanel = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"Hide Panel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextShowHidePanel.Wrap( -1 )
		bSizer172.Add( self.m_staticTextShowHidePanel, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer351.Add( bSizer172, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline631 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer351.Add( self.m_staticline631, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonLadder = wx.Button( self.m_panelScrolled, wx.ID_ANY, u"Ladder", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_buttonLadder.Enable( False )
		self.m_buttonLadder.Hide()
		
		bSizer351.Add( self.m_buttonLadder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer180 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText61 = wx.StaticText( self.m_panelScrolled, wx.ID_ANY, u"History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		self.m_staticText61.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer180.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		m_choiceMarketHistoryChoices = []
		self.m_choiceMarketHistory = wx.Choice( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_choiceMarketHistoryChoices, 0 )
		self.m_choiceMarketHistory.SetSelection( 0 )
		self.m_choiceMarketHistory.Enable( False )
		
		bSizer180.Add( self.m_choiceMarketHistory, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer351.Add( bSizer180, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline43 = wx.StaticLine( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer351.Add( self.m_staticline43, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_toggleBtnStopMarket = wx.ToggleButton( self.m_panelScrolled, wx.ID_ANY, u"Stop Market", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer351.Add( self.m_toggleBtnStopMarket, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer117.Add( bSizer351, 0, wx.EXPAND, 5 )
		
		self.m_splitterMarketBets = wx.SplitterWindow( self.m_panelScrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DSASH|wx.SP_NO_XP_THEME|wx.NO_BORDER )
		self.m_splitterMarketBets.Bind( wx.EVT_IDLE, self.m_splitterMarketBetsOnIdle )
		
		self.m_panelBetting = wx.Panel( self.m_splitterMarketBets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_bettingSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_gridMarket = wx.grid.Grid( self.m_panelBetting, wx.ID_ANY, wx.DefaultPosition, wx.Size( 755,-1 ), wx.STATIC_BORDER )
		
		# Grid
		self.m_gridMarket.CreateGrid( 0, 8 )
		self.m_gridMarket.EnableEditing( False )
		self.m_gridMarket.EnableGridLines( True )
		self.m_gridMarket.EnableDragGridSize( False )
		self.m_gridMarket.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridMarket.SetColSize( 0, 75 )
		self.m_gridMarket.SetColSize( 1, 75 )
		self.m_gridMarket.SetColSize( 2, 75 )
		self.m_gridMarket.SetColSize( 3, 75 )
		self.m_gridMarket.SetColSize( 4, 75 )
		self.m_gridMarket.SetColSize( 5, 75 )
		self.m_gridMarket.SetColSize( 6, 125 )
		self.m_gridMarket.SetColSize( 7, 30 )
		self.m_gridMarket.EnableDragColMove( False )
		self.m_gridMarket.EnableDragColSize( False )
		self.m_gridMarket.SetColLabelSize( 30 )
		self.m_gridMarket.SetColLabelValue( 0, wx.EmptyString )
		self.m_gridMarket.SetColLabelValue( 1, wx.EmptyString )
		self.m_gridMarket.SetColLabelValue( 2, u"Back" )
		self.m_gridMarket.SetColLabelValue( 3, u"Lay" )
		self.m_gridMarket.SetColLabelValue( 4, wx.EmptyString )
		self.m_gridMarket.SetColLabelValue( 5, wx.EmptyString )
		self.m_gridMarket.SetColLabelValue( 6, u"Compensate" )
		self.m_gridMarket.SetColLabelValue( 7, u"Ref." )
		self.m_gridMarket.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridMarket.EnableDragRowSize( False )
		self.m_gridMarket.SetRowLabelSize( 135 )
		self.m_gridMarket.SetRowLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridMarket.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.m_bettingSizer.Add( self.m_gridMarket, 1, wx.EXPAND, 5 )
		
		self.m_scrolledLadder = wx.ScrolledWindow( self.m_panelBetting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledLadder.SetScrollRate( 5, 5 )
		self.m_scrolledLadder.Hide()
		
		self.ladderScrollSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer158 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText115 = wx.StaticText( self.m_scrolledLadder, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )
		bSizer158.Add( self.m_staticText115, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline90 = wx.StaticLine( self.m_scrolledLadder, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer158.Add( self.m_staticline90, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_gridPricing = wx.grid.Grid( self.m_scrolledLadder, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridPricing.CreateGrid( 0, 3 )
		self.m_gridPricing.EnableEditing( True )
		self.m_gridPricing.EnableGridLines( True )
		self.m_gridPricing.EnableDragGridSize( False )
		self.m_gridPricing.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridPricing.SetColSize( 0, 65 )
		self.m_gridPricing.SetColSize( 1, 65 )
		self.m_gridPricing.SetColSize( 2, 75 )
		self.m_gridPricing.EnableDragColMove( False )
		self.m_gridPricing.EnableDragColSize( True )
		self.m_gridPricing.SetColLabelSize( 30 )
		self.m_gridPricing.SetColLabelValue( 0, u"Back" )
		self.m_gridPricing.SetColLabelValue( 1, u"Lay" )
		self.m_gridPricing.SetColLabelValue( 2, u"Traded" )
		self.m_gridPricing.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridPricing.AutoSizeRows()
		self.m_gridPricing.EnableDragRowSize( True )
		self.m_gridPricing.SetRowLabelSize( 45 )
		self.m_gridPricing.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridPricing.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer158.Add( self.m_gridPricing, 0, wx.ALL, 5 )
		
		self.ladderScrollSizer.Add( bSizer158, 1, wx.EXPAND, 5 )
		
		
		self.ladderScrollSizer.AddSpacer( ( 5, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_scrolledLadder.SetSizer( self.ladderScrollSizer )
		self.m_scrolledLadder.Layout()
		self.ladderScrollSizer.Fit( self.m_scrolledLadder )
		self.m_bettingSizer.Add( self.m_scrolledLadder, 1, wx.EXPAND, 5 )
		
		self.m_panelBetting.SetSizer( self.m_bettingSizer )
		self.m_panelBetting.Layout()
		self.m_bettingSizer.Fit( self.m_panelBetting )
		self.m_panelMarketBets = wx.Panel( self.m_splitterMarketBets, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer202 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookInfoLog = wx.Notebook( self.m_panelMarketBets, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_panel14 = wx.Panel( self.m_notebookInfoLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_notebook8 = wx.Notebook( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel32 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer102 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlMarketInfo = wx.ListCtrl( self.m_panel32, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES )
		bSizer102.Add( self.m_listCtrlMarketInfo, 1, wx.EXPAND, 5 )
		
		self.m_panel32.SetSizer( bSizer102 )
		self.m_panel32.Layout()
		bSizer102.Fit( self.m_panel32 )
		self.m_notebook8.AddPage( self.m_panel32, u"GetMarket", True )
		self.m_panel33 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer103 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlRunnersInfo = wx.ListCtrl( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES )
		bSizer103.Add( self.m_listCtrlRunnersInfo, 1, wx.EXPAND, 5 )
		
		self.m_panel33.SetSizer( bSizer103 )
		self.m_panel33.Layout()
		bSizer103.Fit( self.m_panel33 )
		self.m_notebook8.AddPage( self.m_panel33, u"Runners", False )
		self.m_panel34 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer104 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlGetAllMarketsInfo = wx.ListCtrl( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES )
		bSizer104.Add( self.m_listCtrlGetAllMarketsInfo, 1, wx.EXPAND, 5 )
		
		self.m_panel34.SetSizer( bSizer104 )
		self.m_panel34.Layout()
		bSizer104.Fit( self.m_panel34 )
		self.m_notebook8.AddPage( self.m_panel34, u"GetAllMarkets", False )
		
		bSizer221.Add( self.m_notebook8, 2, wx.EXPAND, 5 )
		
		self.m_notebook9 = wx.Notebook( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel35 = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer108 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_htmlWinMarketInfo = wx.html.HtmlWindow( self.m_panel35, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.html.HW_SCROLLBAR_AUTO )
		bSizer108.Add( self.m_htmlWinMarketInfo, 1, wx.EXPAND, 5 )
		
		self.m_panel35.SetSizer( bSizer108 )
		self.m_panel35.Layout()
		bSizer108.Fit( self.m_panel35 )
		self.m_notebook9.AddPage( self.m_panel35, u"Market Description", False )
		
		bSizer221.Add( self.m_notebook9, 5, wx.EXPAND, 5 )
		
		self.m_panel14.SetSizer( bSizer221 )
		self.m_panel14.Layout()
		bSizer221.Fit( self.m_panel14 )
		self.m_notebookInfoLog.AddPage( self.m_panel14, u"Market Info", False )
		self.m_panel132 = wx.Panel( self.m_notebookInfoLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer197 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButton23 = wx.BitmapButton( self.m_panel132, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/zoom.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButton23.SetToolTipString( u"Filter bets" )
		
		self.m_bpButton23.SetToolTipString( u"Filter bets" )
		
		bSizer197.Add( self.m_bpButton23, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticText93 = wx.StaticText( self.m_panel132, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )
		bSizer197.Add( self.m_staticText93, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer21.Add( bSizer197, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline633 = wx.StaticLine( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline633, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap30 = wx.StaticBitmap( self.m_panel132, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/anchor.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer171.Add( self.m_bitmap30, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.m_staticText84 = wx.StaticText( self.m_panel132, wx.ID_ANY, u"StopBet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )
		self.m_staticText84.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer171.Add( self.m_staticText84, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextStopBet = wx.StaticText( self.m_panel132, wx.ID_ANY, u"99%", wx.DefaultPosition, wx.Size( 35,-1 ), wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextStopBet.Wrap( -1 )
		bSizer171.Add( self.m_staticTextStopBet, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_sliderStopBet = wx.Slider( self.m_panel132, wx.ID_ANY, 50, 1, 99, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_BOTH|wx.SL_HORIZONTAL )
		self.m_menuSliderStopBet = wx.Menu()
		self.m_menuItem75 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"2%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem75 )
		
		self.m_menuItem751 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"5%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem751 )
		
		self.m_menuItem7511 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"10%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem7511 )
		
		self.m_menuItem75111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"15%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem75111 )
		
		self.m_menuItem751111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"20%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem751111 )
		
		self.m_menuItem7511111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"25%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem7511111 )
		
		self.m_menuItem75111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"30%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem75111111 )
		
		self.m_menuItem751111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"40%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem751111111 )
		
		self.m_menuItem7511111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"50%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem7511111111 )
		
		self.m_menuItem75111111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"60%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem75111111111 )
		
		self.m_menuItem751111111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"75%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem751111111111 )
		
		self.m_menuItem7511111111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"90%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem7511111111111 )
		
		self.m_menuItem75111111111111 = wx.MenuItem( self.m_menuSliderStopBet, wx.ID_ANY, u"95%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuSliderStopBet.AppendItem( self.m_menuItem75111111111111 )
		
		self.m_sliderStopBet.Bind( wx.EVT_RIGHT_DOWN, self.m_sliderStopBetOnContextMenu ) 
		
		bSizer171.Add( self.m_sliderStopBet, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer21.Add( bSizer171, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline84 = wx.StaticLine( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline84, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer199 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText841 = wx.StaticText( self.m_panel132, wx.ID_ANY, u"Market susp. guard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText841.Wrap( -1 )
		bSizer199.Add( self.m_staticText841, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_spinCtrlStopBetSuspGuard = wx.SpinCtrl( self.m_panel132, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 99, 7 )
		bSizer199.Add( self.m_spinCtrlStopBetSuspGuard, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText851 = wx.StaticText( self.m_panel132, wx.ID_ANY, u"secs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText851.Wrap( -1 )
		bSizer199.Add( self.m_staticText851, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer21.Add( bSizer199, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline68 = wx.StaticLine( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline68, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer120 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap31 = wx.StaticBitmap( self.m_panel132, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/money_add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer120.Add( self.m_bitmap31, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText63 = wx.StaticText( self.m_panel132, wx.ID_ANY, u"Compensate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		self.m_staticText63.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer120.Add( self.m_staticText63, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextCompensate = wx.StaticText( self.m_panel132, wx.ID_ANY, u"100%", wx.DefaultPosition, wx.Size( 35,-1 ), wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextCompensate.Wrap( -1 )
		bSizer120.Add( self.m_staticTextCompensate, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_sliderCompensate = wx.Slider( self.m_panel132, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL|wx.SL_INVERSE )
		self.m_menuCompensate = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menuCompensate, wx.ID_ANY, u"0%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCompensate.AppendItem( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menuCompensate, wx.ID_ANY, u"25%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCompensate.AppendItem( self.m_menuItem6 )
		
		self.m_menuItem7 = wx.MenuItem( self.m_menuCompensate, wx.ID_ANY, u"50%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCompensate.AppendItem( self.m_menuItem7 )
		
		self.m_menuItem8 = wx.MenuItem( self.m_menuCompensate, wx.ID_ANY, u"75%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCompensate.AppendItem( self.m_menuItem8 )
		
		self.m_menuItem9 = wx.MenuItem( self.m_menuCompensate, wx.ID_ANY, u"100%", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCompensate.AppendItem( self.m_menuItem9 )
		
		self.m_sliderCompensate.Bind( wx.EVT_RIGHT_DOWN, self.m_sliderCompensateOnContextMenu ) 
		
		bSizer120.Add( self.m_sliderCompensate, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer21.Add( bSizer120, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline91 = wx.StaticLine( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline91, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_buttonCancelAllBets = wx.Button( self.m_panel132, wx.ID_ANY, u"Cancel Bets", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_buttonCancelAllBets.Enable( False )
		
		bSizer21.Add( self.m_buttonCancelAllBets, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer59.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		self.sizerMUBets = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panelMUBetsFilter = wx.Panel( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		self.m_panelMUBetsFilter.Hide()
		
		bSizer99 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBoxShowMatched = wx.CheckBox( self.m_panelMUBetsFilter, wx.ID_ANY, u"Matched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxShowMatched.SetValue(True) 
		bSizer99.Add( self.m_checkBoxShowMatched, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxShowUnmatched = wx.CheckBox( self.m_panelMUBetsFilter, wx.ID_ANY, u"Unmatched", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxShowUnmatched.SetValue(True) 
		bSizer99.Add( self.m_checkBoxShowUnmatched, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxShowBack = wx.CheckBox( self.m_panelMUBetsFilter, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxShowBack.SetValue(True) 
		bSizer99.Add( self.m_checkBoxShowBack, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxShowLay = wx.CheckBox( self.m_panelMUBetsFilter, wx.ID_ANY, u"Lay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxShowLay.SetValue(True) 
		bSizer99.Add( self.m_checkBoxShowLay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panelMUBetsFilter.SetSizer( bSizer99 )
		self.m_panelMUBetsFilter.Layout()
		bSizer99.Fit( self.m_panelMUBetsFilter )
		self.sizerMUBets.Add( self.m_panelMUBetsFilter, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_listCtrlBets = wx.ListCtrl( self.m_panel132, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES|wx.NO_BORDER )
		self.m_menuListBets = wx.Menu()
		self.m_menuItemBetCancel = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Cancel", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemBetCancel.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemBetCancel )
		
		self.m_menuItemBetModify = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Modify", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemBetModify.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/application_form_edit.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemBetModify )
		
		self.m_menuListBets.AppendSeparator()
		
		self.m_menuItemBetCompensate = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Compensate", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemBetCompensate.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/money.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemBetCompensate )
		
		self.m_menuListBets.AppendSeparator()
		
		self.m_menuItemStopProfitProfit = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Stop Win on % of expected profit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopProfitProfit.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/money_add.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemStopProfitProfit )
		
		self.m_menuItemStopProfitRisk = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Stop Win on % of assumed risk", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopProfitRisk.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/money_add.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemStopProfitRisk )
		
		self.m_menuListBets.AppendSeparator()
		
		self.m_menuItemStopLossProfit = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Stop Loss on % of expected profit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopLossProfit.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/money_delete.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemStopLossProfit )
		
		self.m_menuItemStopLossRisk = wx.MenuItem( self.m_menuListBets, wx.ID_ANY, u"Stop Loss on % of assumed risk", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopLossRisk.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/money_delete.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuListBets.AppendItem( self.m_menuItemStopLossRisk )
		
		self.m_listCtrlBets.Bind( wx.EVT_RIGHT_DOWN, self.m_listCtrlBetsOnContextMenu ) 
		
		self.sizerMUBets.Add( self.m_listCtrlBets, 1, wx.EXPAND, 5 )
		
		bSizer59.Add( self.sizerMUBets, 1, wx.EXPAND, 5 )
		
		self.m_panel132.SetSizer( bSizer59 )
		self.m_panel132.Layout()
		bSizer59.Fit( self.m_panel132 )
		self.m_notebookInfoLog.AddPage( self.m_panel132, u"Market bets", True )
		self.m_panel242 = wx.Panel( self.m_notebookInfoLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer911 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlStopBets = wx.ListCtrl( self.m_panel242, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_VRULES )
		self.m_menuStopBet = wx.Menu()
		self.m_menuItemStopBetPause = wx.MenuItem( self.m_menuStopBet, wx.ID_ANY, u"Pause", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopBetPause.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/control_pause_blue.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuStopBet.AppendItem( self.m_menuItemStopBetPause )
		
		self.m_menuItemStopBetRestart = wx.MenuItem( self.m_menuStopBet, wx.ID_ANY, u"Restart", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopBetRestart.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/control_play_blue.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuStopBet.AppendItem( self.m_menuItemStopBetRestart )
		
		self.m_menuItemStopBetCancel = wx.MenuItem( self.m_menuStopBet, wx.ID_ANY, u"Cancel", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItemStopBetCancel.SetBitmap( wx.Bitmap( u"icons/famfamfam-silk/cancel.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menuStopBet.AppendItem( self.m_menuItemStopBetCancel )
		
		self.m_listCtrlStopBets.Bind( wx.EVT_RIGHT_DOWN, self.m_listCtrlStopBetsOnContextMenu ) 
		
		bSizer911.Add( self.m_listCtrlStopBets, 1, wx.EXPAND, 5 )
		
		self.m_panel242.SetSizer( bSizer911 )
		self.m_panel242.Layout()
		bSizer911.Fit( self.m_panel242 )
		self.m_notebookInfoLog.AddPage( self.m_panel242, u"Stop Bets", False )
		self.m_panelBettingLog = wx.Panel( self.m_notebookInfoLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer79 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBoxMessagesChoices = []
		self.m_listBoxMessages = wx.ListBox( self.m_panelBettingLog, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_listBoxMessagesChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
		self.m_menuLogMessages = wx.Menu()
		self.m_menuItemMessagesSelectAll = wx.MenuItem( self.m_menuLogMessages, wx.ID_ANY, u"Select All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessages.AppendItem( self.m_menuItemMessagesSelectAll )
		
		self.m_menuItemMessagesDeselectAll = wx.MenuItem( self.m_menuLogMessages, wx.ID_ANY, u"Deselect All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessages.AppendItem( self.m_menuItemMessagesDeselectAll )
		
		self.m_menuItemMessagesCopySelected = wx.MenuItem( self.m_menuLogMessages, wx.ID_ANY, u"Copy Selected to Clipboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessages.AppendItem( self.m_menuItemMessagesCopySelected )
		
		self.m_menuItemMessagesClearSelected = wx.MenuItem( self.m_menuLogMessages, wx.ID_ANY, u"Clear Selected", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessages.AppendItem( self.m_menuItemMessagesClearSelected )
		
		self.m_menuItemMessagesClearAll = wx.MenuItem( self.m_menuLogMessages, wx.ID_ANY, u"Clear All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessages.AppendItem( self.m_menuItemMessagesClearAll )
		
		self.m_listBoxMessages.Bind( wx.EVT_RIGHT_DOWN, self.m_listBoxMessagesOnContextMenu ) 
		
		bSizer79.Add( self.m_listBoxMessages, 1, wx.EXPAND, 5 )
		
		self.m_panelBettingLog.SetSizer( bSizer79 )
		self.m_panelBettingLog.Layout()
		bSizer79.Fit( self.m_panelBettingLog )
		self.m_notebookInfoLog.AddPage( self.m_panelBettingLog, u"Betting Log", False )
		self.m_panelErrorLog = wx.Panel( self.m_notebookInfoLog, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer80 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBoxMessagesErrorChoices = []
		self.m_listBoxMessagesError = wx.ListBox( self.m_panelErrorLog, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_listBoxMessagesErrorChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL|wx.NO_BORDER )
		self.m_menuLogMessagesError = wx.Menu()
		self.m_menuItemMessagesErrorSelectAll = wx.MenuItem( self.m_menuLogMessagesError, wx.ID_ANY, u"Select All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessagesError.AppendItem( self.m_menuItemMessagesErrorSelectAll )
		
		self.m_menuItemMessagesErrorDeselectAll = wx.MenuItem( self.m_menuLogMessagesError, wx.ID_ANY, u"Deselect All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessagesError.AppendItem( self.m_menuItemMessagesErrorDeselectAll )
		
		self.m_menuItemMessagesErrorCopySelected = wx.MenuItem( self.m_menuLogMessagesError, wx.ID_ANY, u"Copy Selected to Clipboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessagesError.AppendItem( self.m_menuItemMessagesErrorCopySelected )
		
		self.m_menuItemMessagesErrorClearSelected = wx.MenuItem( self.m_menuLogMessagesError, wx.ID_ANY, u"Clear Selected", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessagesError.AppendItem( self.m_menuItemMessagesErrorClearSelected )
		
		self.m_menuItemMessagesErrorClearAll = wx.MenuItem( self.m_menuLogMessagesError, wx.ID_ANY, u"Clear All", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLogMessagesError.AppendItem( self.m_menuItemMessagesErrorClearAll )
		
		self.m_listBoxMessagesError.Bind( wx.EVT_RIGHT_DOWN, self.m_listBoxMessagesErrorOnContextMenu ) 
		
		bSizer80.Add( self.m_listBoxMessagesError, 1, wx.EXPAND, 5 )
		
		self.m_panelErrorLog.SetSizer( bSizer80 )
		self.m_panelErrorLog.Layout()
		bSizer80.Fit( self.m_panelErrorLog )
		self.m_notebookInfoLog.AddPage( self.m_panelErrorLog, u"Error Log", False )
		
		bSizer202.Add( self.m_notebookInfoLog, 1, wx.EXPAND, 5 )
		
		self.m_panelMarketBets.SetSizer( bSizer202 )
		self.m_panelMarketBets.Layout()
		bSizer202.Fit( self.m_panelMarketBets )
		self.m_splitterMarketBets.SplitHorizontally( self.m_panelBetting, self.m_panelMarketBets, 350 )
		bSizer117.Add( self.m_splitterMarketBets, 1, wx.EXPAND, 5 )
		
		self.m_panelScrolled.SetSizer( bSizer117 )
		self.m_panelScrolled.Layout()
		bSizer117.Fit( self.m_panelScrolled )
		self.bSizerScrollWindow.Add( self.m_panelScrolled, 1, wx.EXPAND, 5 )
		
		self.m_scrolledWindowMainRight.SetSizer( self.bSizerScrollWindow )
		self.m_scrolledWindowMainRight.Layout()
		self.bSizerScrollWindow.Fit( self.m_scrolledWindowMainRight )
		bSizer12.Add( self.m_scrolledWindowMainRight, 1, wx.EXPAND, 5 )
		
		self.m_panelMainRight.SetSizer( bSizer12 )
		self.m_panelMainRight.Layout()
		bSizer12.Fit( self.m_panelMainRight )
		bSizer35.Add( self.m_panelMainRight, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer35 )
		self.Layout()
		bSizer35.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_textCtrlPassword.Bind( wx.EVT_TEXT_ENTER, self.OnTextEnterPassword )
		self.m_buttonLogin.Bind( wx.EVT_BUTTON, self.OnButtonClickLogin )
		self.m_buttonManageUsernames.Bind( wx.EVT_BUTTON, self.OnButtonClickManageUsernames )
		self.m_checkBoxRememberUsername.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxRememberUsername )
		self.m_checkBoxFreeAPI.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUseFreeApi )
		self.m_checkboxShowFunds.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowFunds )
		self.m_buttonReloadFunds.Bind( wx.EVT_BUTTON, self.OnButtonClickReloadFunds )
		self.m_bpButtonAus2UK.Bind( wx.EVT_BUTTON, self.OnButtonClickAus2UK )
		self.m_bpButtonUK2Aus.Bind( wx.EVT_BUTTON, self.OnButtonClickUK2Aus )
		self.m_checkBoxUseProxy.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUseProxy )
		self.m_sliderRefresh.Bind( wx.EVT_SCROLL, self.OnScrollSliderRefresh )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_0.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_01.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_011.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_012.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_0121.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_01211.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_012111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_0121111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderRefresh, id = self.m_menuItemSliderRefresh_1_01211111.GetId() )
		self.m_checkBoxOptimizeNetwork.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxOptimizeNetwork )
		self.m_spinCtrlOptimizeGuard.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlOptimizeGuard )
		self.m_buttonCustomizeColours.Bind( wx.EVT_BUTTON, self.OnButtonClickCustomizeColours )
		self.m_buttonClearRegistryStorage.Bind( wx.EVT_BUTTON, self.OnButtonClickClearRegistryStorage )
		self.m_buttonLookForUpdates.Bind( wx.EVT_BUTTON, self.OnButtonClickLookForUpdates )
		self.m_checkBoxSeekUpdateOnAppStart.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUpdateOnAppStart )
		self.m_notebookFavs.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChangedFavs )
		self.m_buttonTreeEventsCollapseAll.Bind( wx.EVT_BUTTON, self.OnButtonClickTreeEventsCollapseAll )
		self.m_buttonTreeEventsReloadAll.Bind( wx.EVT_BUTTON, self.OnButtonClickTreeEventsReloadAll )
		self.m_buttonTreeEventsReloadSelected.Bind( wx.EVT_BUTTON, self.OnButtonClickTreeEventsReloadSelected )
		self.m_buttonTreeEventsEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickTreeEventsEdit )
		self.m_bpButtonGenerateSearchPattern.Bind( wx.EVT_BUTTON, self.OnButtonClickGenerateSearchPattern )
		self.m_checkBoxLoadMarketsAfterLogin.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxMarketsAfterLogin )
		self.m_checkBoxVirtualPrices.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxVirtualPrices )
		self.m_checkBoxAutoExpand.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxAutoExpand )
		self.m_checkBoxCacheMarkets.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCacheMarkets )
		self.m_checkBoxUseBfOrder.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUseBfOrder )
		self.m_treeEvents.Bind( wx.EVT_TREE_ITEM_EXPANDING, self.OnTreeItemExpanding )
		self.m_treeEvents.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChanged )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeItemSelect, id = self.m_menuItemTreeItemSelect.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeCollapseAll, id = self.m_menuItemTreeCollapseAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeItemReloadAll, id = self.m_menuItemTreeItemReloadAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeItemReload, id = self.m_menuItemTreeItemReload.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionGenerateSearchPattern, id = self.m_menuItemGenerateSearchPattern.GetId() )
		self.m_listBoxSavedMarkets.Bind( wx.EVT_LISTBOX_DCLICK, self.OnListBoxDClickSavedMarkets )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSavedMarketsLoadMarket, id = self.m_menuItemSavedMarketsLoad.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSavedMarketsSelectAll, id = self.m_menuItemSavedMarketsSelectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSavedMarketsDeleteSelected, id = self.m_menuItemSavedMarketsDeleteSelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSavedMarketsDeleteAll, id = self.m_menuItemSavedMarketsDeleteAll.GetId() )
		self.m_buttonPatternManager.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternManager )
		self.m_bpButton33.Bind( wx.EVT_BUTTON, self.OnButtonClickRefreshMarkets )
		self.m_sliderMarketDataRefresh.Bind( wx.EVT_SCROLL, self.OnScrollMarketDataRefresh )
		self.m_listCtrlFavs.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnListItemActivatedFavs )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionFavSearchLoad, id = self.m_menuItemFavSearchLoad.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionPatternManager, id = self.m_menuItemPatternManager.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionReloadPattern, id = self.m_menuItemReloadPattern.GetId() )
		self.m_textCtrlSearch.Bind( wx.EVT_TEXT_ENTER, self.OnTextEnterSearch )
		self.m_bpButtonSearch.Bind( wx.EVT_BUTTON, self.OnButtonClickSearch )
		self.m_buttonCurrentBetsCollapse.Bind( wx.EVT_BUTTON, self.OnButtonClickCurrentBetsCollapseAll )
		self.m_buttonCurrentBetsLoadMarket.Bind( wx.EVT_BUTTON, self.OnButtonClickCurrentBetsLoadMarket )
		self.m_buttonCurrentBets.Bind( wx.EVT_BUTTON, self.OnButtonClickCurrentBets )
		self.m_checkBoxCurrentBetsAutoRefresh.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCurrentBetsAutoRefresh )
		self.m_notebookCurrentBets.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChangedCurrentBets )
		self.m_treeCtrlCurrentBetsUK.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnTreeItemActivatedCurrentBetsUK )
		self.m_treeCtrlCurrentBetsUK.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChangedCurrentBetsUK )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionCurrentBetsLoadMarket, id = self.m_menuCurrentBetsLoadMarket.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionCurrentBetsCancelBet, id = self.m_menuItemCurrentBetsCancelBet.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionCurrentBetsModifyBet, id = self.m_menuItemCurrentBetsModifyBet.GetId() )
		self.m_treeCtrlCurrentBetsAus.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnTreeItemActivatedCurrentBetsAus )
		self.m_treeCtrlCurrentBetsAus.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChangedCurrentBetsAus )
		self.m_checkBoxCurrentBetsMatched.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCurrentBetsFilter )
		self.m_checkBoxCurrentBetsUnmatched.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCurrentBetsFilter )
		self.m_checkBoxCurrentBetsBack.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCurrentBetsFilter )
		self.m_checkBoxCurrentBetsLay.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCurrentBetsFilter )
		self.m_notebookModules.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChangedModules )
		self.m_checkListBfModules.Bind( wx.EVT_LISTBOX, self.OnCheckListBoxBfModules )
		self.m_checkListBfModules.Bind( wx.EVT_CHECKLISTBOX, self.OnCheckListBoxBfModulesToggle )
		self.m_toggleBfModules.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleButtonBfModules )
		self.m_buttonBfModulesOn.Bind( wx.EVT_BUTTON, self.OnButtonClickBfModulesSwitchOn )
		self.m_buttonBfModulesPause.Bind( wx.EVT_BUTTON, self.OnButtonClickBfModulesPause )
		self.m_listCtrlModParams.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnListItemActivatedModParam )
		self.m_listCtrlModParams.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.OnListItemDeSelectedModParam )
		self.m_listCtrlModParams.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnListItemSelectedModParam )
		self.m_buttonEditModParam.Bind( wx.EVT_BUTTON, self.OnButtonClickModParamsEdit )
		self.m_buttonModParamsSend.Bind( wx.EVT_BUTTON, self.OnButtonClickModParamsSend )
		self.m_buttonModParamsReload.Bind( wx.EVT_BUTTON, self.OnButtonClickModParamsReload )
		self.m_buttonModParamsDefaults.Bind( wx.EVT_BUTTON, self.OnButtonClickModParamsDefaults )
		self.m_checkListModulesRunners.Bind( wx.EVT_CHECKLISTBOX, self.OnCheckListBoxToggledModuleRunners )
		self.m_buttonModuleRunnersApply.Bind( wx.EVT_BUTTON, self.OnButtonClickModuleRunnersApply )
		self.m_buttonModuleRunnersRefresh.Bind( wx.EVT_BUTTON, self.OnButtonClickModuleRunnersRefresh )
		self.m_buttonModuleRunnersCheckAll.Bind( wx.EVT_BUTTON, self.OnButtonClickModuleRunnersCheckAll )
		self.m_buttonModuleRunnersUncheckAll.Bind( wx.EVT_BUTTON, self.OnButtonClickModuleRunnersUncheckAll )
		self.m_checkBoxRecordAndPlayTabSeparator.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUseTabAsSeparator )
		self.m_toggleBtnRecord.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleButtonRecord )
		self.m_toggleBtnPlay.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleButtonPlay )
		self.m_bpButtonExcelUpdateWorkbooks.Bind( wx.EVT_BUTTON, self.OnButtonClickExcelUpdateWorkbooks )
		self.m_bpButtonExcelOpen.Bind( wx.EVT_BUTTON, self.OnButtonClickExcelOpen )
		self.m_bpButtonExcelPlay.Bind( wx.EVT_BUTTON, self.OnButtonClickExcelPlay )
		self.m_bpButtonExcelPause.Bind( wx.EVT_BUTTON, self.OnButtonClickExcelPause )
		self.m_bpButtonExcelStop.Bind( wx.EVT_BUTTON, self.OnButtonClickExcelStop )
		self.m_checkListExcelWorkbooks.Bind( wx.EVT_LISTBOX, self.OnCheckListBoxExcelWorkbooks )
		self.m_checkListExcelWorkbooks.Bind( wx.EVT_CHECKLISTBOX, self.OnCheckListBoxToggleExcelWorkbooks )
		self.m_checkListExcelSheets.Bind( wx.EVT_CHECKLISTBOX, self.OnCheckListBoxToggleExcelSheets )
		self.m_listBoxModLogging.Bind( wx.EVT_CHAR, self.OnCharListBoxModLogging )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingSelectAllMessages, id = self.m_menuItemModLoggingSelectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingDeselectAllMessages, id = self.m_menuItemModLoggingDeselectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingClearAllMessages, id = self.m_menuItemModLoggingClearAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingClearSelectedMessages, id = self.m_menuItemModLoggingClearSelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingCopyAllMessages, id = self.m_menuItemModLoggingCopyAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModuleLoggingCopySelectedMessages, id = self.m_menuItemModLoggingCopySelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionWalletLoadGUIModules, id = self.m_menuItemLoadGUIModules.GetId() )
		self.m_checkBoxShowProfitAndLoss.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowProfitAndLoss )
		self.m_checkBoxDisplayPercPrices.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDisplayPercPrices )
		self.m_checkBoxVerifyBets.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxVerifyBets )
		self.m_checkBoxVerifyRClickBets.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxVerifyRClickBets )
		self.m_checkBoxSingleClickBetting.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxSingleClickBetting )
		self.m_buttonQuickStakes.Bind( wx.EVT_BUTTON, self.OnButtonClickQuickStakes )
		self.m_checkBoxSingleClickLiability.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxSingleClickBettingStakeLiability )
		self.m_buttonExpandEvents.Bind( wx.EVT_BUTTON, self.OnButtonClickExpandMarket )
		self.m_buttonSaveAsFav.Bind( wx.EVT_BUTTON, self.OnButtonClickSaveMarket )
		self.m_checkBoxTicksAway.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxTicksAway )
		self.m_spinCtrlTicksFromPrice.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlTicksFromPrice )
		self.m_checkBoxCompAway.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxCompAway )
		self.m_spinCtrlTicksFromComp.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlTicksFromComp )
		self.m_checkBoxFillOrKill.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxFillOrKill )
		self.m_spinCtrlFillOrKill.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlFillOrKill )
		self.m_bpButtonPanelShowHide.Bind( wx.EVT_BUTTON, self.OnButtonClickPanelShowHide )
		self.m_buttonLadder.Bind( wx.EVT_BUTTON, self.OnButtonClickLadder )
		self.m_choiceMarketHistory.Bind( wx.EVT_CHOICE, self.OnChoiceMarketHistory )
		self.m_toggleBtnStopMarket.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleButtonStopMarket )
		self.m_gridMarket.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridCellLeftClick )
		self.m_gridMarket.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridCellLeftDClick )
		self.m_gridMarket.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnGridCellRightClick )
		self.m_gridMarket.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnGridLabelLeftClick )
		self.m_gridMarket.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.OnGridLabelLeftDClick )
		self.m_notebookInfoLog.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChangedInfoLog )
		self.m_bpButton23.Bind( wx.EVT_BUTTON, self.OnButtonClickMUBetsFilter )
		self.m_sliderStopBet.Bind( wx.EVT_SCROLL, self.OnScrollStopBet )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem75.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem751.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem7511.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem75111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem751111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem7511111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem75111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem751111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem7511111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem75111111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem751111111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem7511111111111.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderStopBet, id = self.m_menuItem75111111111111.GetId() )
		self.m_spinCtrlStopBetSuspGuard.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrlStopBetGuard )
		self.m_sliderCompensate.Bind( wx.EVT_SCROLL, self.OnScrollCompensate )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderCompensate, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderCompensate, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderCompensate, id = self.m_menuItem7.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderCompensate, id = self.m_menuItem8.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSliderCompensate, id = self.m_menuItem9.GetId() )
		self.m_buttonCancelAllBets.Bind( wx.EVT_BUTTON, self.OnButtonClickCancelAllBets )
		self.m_checkBoxShowMatched.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowMatched )
		self.m_checkBoxShowUnmatched.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowUnmatched )
		self.m_checkBoxShowBack.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowBack )
		self.m_checkBoxShowLay.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowLay )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionCancel, id = self.m_menuItemBetCancel.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionModify, id = self.m_menuItemBetModify.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionCompensate, id = self.m_menuItemBetCompensate.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetProfitProfit, id = self.m_menuItemStopProfitProfit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetProfitRisk, id = self.m_menuItemStopProfitRisk.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetLossProfit, id = self.m_menuItemStopLossProfit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetLossRisk, id = self.m_menuItemStopLossRisk.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetPause, id = self.m_menuItemStopBetPause.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetRestart, id = self.m_menuItemStopBetRestart.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionStopBetCancel, id = self.m_menuItemStopBetCancel.GetId() )
		self.m_listBoxMessages.Bind( wx.EVT_CHAR, self.OnCharListBoxMessages )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesSelectAll, id = self.m_menuItemMessagesSelectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesDeselectAll, id = self.m_menuItemMessagesDeselectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesCopySelectedToClipBoard, id = self.m_menuItemMessagesCopySelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesClearSelected, id = self.m_menuItemMessagesClearSelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesClearAll, id = self.m_menuItemMessagesClearAll.GetId() )
		self.m_listBoxMessagesError.Bind( wx.EVT_CHAR, self.OnCharListBoxMessagesError )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesErrorSelectAll, id = self.m_menuItemMessagesErrorSelectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesErrorDeselectAll, id = self.m_menuItemMessagesErrorDeselectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesErrorCopySelectedToClipBoard, id = self.m_menuItemMessagesErrorCopySelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesErrorClearSelected, id = self.m_menuItemMessagesErrorClearSelected.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionLogMessagesErrorClearAll, id = self.m_menuItemMessagesErrorClearAll.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnSize( self, event ):
		event.Skip()
	
	def OnTextEnterPassword( self, event ):
		event.Skip()
	
	def OnButtonClickLogin( self, event ):
		event.Skip()
	
	def OnButtonClickManageUsernames( self, event ):
		event.Skip()
	
	def OnCheckBoxRememberUsername( self, event ):
		event.Skip()
	
	def OnCheckBoxUseFreeApi( self, event ):
		event.Skip()
	
	def OnCheckBoxShowFunds( self, event ):
		event.Skip()
	
	def OnButtonClickReloadFunds( self, event ):
		event.Skip()
	
	def OnButtonClickAus2UK( self, event ):
		event.Skip()
	
	def OnButtonClickUK2Aus( self, event ):
		event.Skip()
	
	def OnCheckBoxUseProxy( self, event ):
		event.Skip()
	
	def OnScrollSliderRefresh( self, event ):
		event.Skip()
	
	def OnMenuSelectionSliderRefresh( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	def OnCheckBoxOptimizeNetwork( self, event ):
		event.Skip()
	
	def OnSpinCtrlOptimizeGuard( self, event ):
		event.Skip()
	
	def OnButtonClickCustomizeColours( self, event ):
		event.Skip()
	
	def OnButtonClickClearRegistryStorage( self, event ):
		event.Skip()
	
	def OnButtonClickLookForUpdates( self, event ):
		event.Skip()
	
	def OnCheckBoxUpdateOnAppStart( self, event ):
		event.Skip()
	
	def OnNotebookPageChangedFavs( self, event ):
		event.Skip()
	
	def OnButtonClickTreeEventsCollapseAll( self, event ):
		event.Skip()
	
	def OnButtonClickTreeEventsReloadAll( self, event ):
		event.Skip()
	
	def OnButtonClickTreeEventsReloadSelected( self, event ):
		event.Skip()
	
	def OnButtonClickTreeEventsEdit( self, event ):
		event.Skip()
	
	def OnButtonClickGenerateSearchPattern( self, event ):
		event.Skip()
	
	def OnCheckBoxMarketsAfterLogin( self, event ):
		event.Skip()
	
	def OnCheckBoxVirtualPrices( self, event ):
		event.Skip()
	
	def OnCheckBoxAutoExpand( self, event ):
		event.Skip()
	
	def OnCheckBoxCacheMarkets( self, event ):
		event.Skip()
	
	def OnCheckBoxUseBfOrder( self, event ):
		event.Skip()
	
	def OnTreeItemExpanding( self, event ):
		event.Skip()
	
	def OnTreeSelChanged( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeItemSelect( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeCollapseAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeItemReloadAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeItemReload( self, event ):
		event.Skip()
	
	def OnMenuSelectionGenerateSearchPattern( self, event ):
		event.Skip()
	
	def OnListBoxDClickSavedMarkets( self, event ):
		event.Skip()
	
	def OnMenuSelectionSavedMarketsLoadMarket( self, event ):
		event.Skip()
	
	def OnMenuSelectionSavedMarketsSelectAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionSavedMarketsDeleteSelected( self, event ):
		event.Skip()
	
	def OnMenuSelectionSavedMarketsDeleteAll( self, event ):
		event.Skip()
	
	def OnButtonClickPatternManager( self, event ):
		event.Skip()
	
	def OnButtonClickRefreshMarkets( self, event ):
		event.Skip()
	
	def OnScrollMarketDataRefresh( self, event ):
		event.Skip()
	
	def OnListItemActivatedFavs( self, event ):
		event.Skip()
	
	def OnMenuSelectionFavSearchLoad( self, event ):
		event.Skip()
	
	def OnMenuSelectionPatternManager( self, event ):
		event.Skip()
	
	def OnMenuSelectionReloadPattern( self, event ):
		event.Skip()
	
	def OnTextEnterSearch( self, event ):
		event.Skip()
	
	def OnButtonClickSearch( self, event ):
		event.Skip()
	
	def OnButtonClickCurrentBetsCollapseAll( self, event ):
		event.Skip()
	
	def OnButtonClickCurrentBetsLoadMarket( self, event ):
		event.Skip()
	
	def OnButtonClickCurrentBets( self, event ):
		event.Skip()
	
	def OnCheckBoxCurrentBetsAutoRefresh( self, event ):
		event.Skip()
	
	def OnNotebookPageChangedCurrentBets( self, event ):
		event.Skip()
	
	def OnTreeItemActivatedCurrentBetsUK( self, event ):
		event.Skip()
	
	def OnTreeSelChangedCurrentBetsUK( self, event ):
		event.Skip()
	
	def OnMenuSelectionCurrentBetsLoadMarket( self, event ):
		event.Skip()
	
	def OnMenuSelectionCurrentBetsCancelBet( self, event ):
		event.Skip()
	
	def OnMenuSelectionCurrentBetsModifyBet( self, event ):
		event.Skip()
	
	def OnTreeItemActivatedCurrentBetsAus( self, event ):
		event.Skip()
	
	def OnTreeSelChangedCurrentBetsAus( self, event ):
		event.Skip()
	
	def OnCheckBoxCurrentBetsFilter( self, event ):
		event.Skip()
	
	
	
	
	def OnNoteBookPageChangedModules( self, event ):
		event.Skip()
	
	def OnCheckListBoxBfModules( self, event ):
		event.Skip()
	
	def OnCheckListBoxBfModulesToggle( self, event ):
		event.Skip()
	
	def OnToggleButtonBfModules( self, event ):
		event.Skip()
	
	def OnButtonClickBfModulesSwitchOn( self, event ):
		event.Skip()
	
	def OnButtonClickBfModulesPause( self, event ):
		event.Skip()
	
	def OnListItemActivatedModParam( self, event ):
		event.Skip()
	
	def OnListItemDeSelectedModParam( self, event ):
		event.Skip()
	
	def OnListItemSelectedModParam( self, event ):
		event.Skip()
	
	def OnButtonClickModParamsEdit( self, event ):
		event.Skip()
	
	def OnButtonClickModParamsSend( self, event ):
		event.Skip()
	
	def OnButtonClickModParamsReload( self, event ):
		event.Skip()
	
	def OnButtonClickModParamsDefaults( self, event ):
		event.Skip()
	
	def OnCheckListBoxToggledModuleRunners( self, event ):
		event.Skip()
	
	def OnButtonClickModuleRunnersApply( self, event ):
		event.Skip()
	
	def OnButtonClickModuleRunnersRefresh( self, event ):
		event.Skip()
	
	def OnButtonClickModuleRunnersCheckAll( self, event ):
		event.Skip()
	
	def OnButtonClickModuleRunnersUncheckAll( self, event ):
		event.Skip()
	
	def OnCheckBoxUseTabAsSeparator( self, event ):
		event.Skip()
	
	def OnToggleButtonRecord( self, event ):
		event.Skip()
	
	def OnToggleButtonPlay( self, event ):
		event.Skip()
	
	def OnButtonClickExcelUpdateWorkbooks( self, event ):
		event.Skip()
	
	def OnButtonClickExcelOpen( self, event ):
		event.Skip()
	
	def OnButtonClickExcelPlay( self, event ):
		event.Skip()
	
	def OnButtonClickExcelPause( self, event ):
		event.Skip()
	
	def OnButtonClickExcelStop( self, event ):
		event.Skip()
	
	def OnCheckListBoxExcelWorkbooks( self, event ):
		event.Skip()
	
	def OnCheckListBoxToggleExcelWorkbooks( self, event ):
		event.Skip()
	
	def OnCheckListBoxToggleExcelSheets( self, event ):
		event.Skip()
	
	def OnCharListBoxModLogging( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingSelectAllMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingDeselectAllMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingClearAllMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingClearSelectedMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingCopyAllMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionModuleLoggingCopySelectedMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionWalletLoadGUIModules( self, event ):
		event.Skip()
	
	def OnCheckBoxShowProfitAndLoss( self, event ):
		event.Skip()
	
	def OnCheckBoxDisplayPercPrices( self, event ):
		event.Skip()
	
	def OnCheckBoxVerifyBets( self, event ):
		event.Skip()
	
	def OnCheckBoxVerifyRClickBets( self, event ):
		event.Skip()
	
	def OnCheckBoxSingleClickBetting( self, event ):
		event.Skip()
	
	def OnButtonClickQuickStakes( self, event ):
		event.Skip()
	
	def OnCheckBoxSingleClickBettingStakeLiability( self, event ):
		event.Skip()
	
	def OnButtonClickExpandMarket( self, event ):
		event.Skip()
	
	def OnButtonClickSaveMarket( self, event ):
		event.Skip()
	
	def OnCheckBoxTicksAway( self, event ):
		event.Skip()
	
	def OnSpinCtrlTicksFromPrice( self, event ):
		event.Skip()
	
	def OnCheckBoxCompAway( self, event ):
		event.Skip()
	
	def OnSpinCtrlTicksFromComp( self, event ):
		event.Skip()
	
	def OnCheckBoxFillOrKill( self, event ):
		event.Skip()
	
	def OnSpinCtrlFillOrKill( self, event ):
		event.Skip()
	
	def OnButtonClickPanelShowHide( self, event ):
		event.Skip()
	
	def OnButtonClickLadder( self, event ):
		event.Skip()
	
	def OnChoiceMarketHistory( self, event ):
		event.Skip()
	
	def OnToggleButtonStopMarket( self, event ):
		event.Skip()
	
	def OnGridCellLeftClick( self, event ):
		event.Skip()
	
	def OnGridCellLeftDClick( self, event ):
		event.Skip()
	
	def OnGridCellRightClick( self, event ):
		event.Skip()
	
	def OnGridLabelLeftClick( self, event ):
		event.Skip()
	
	def OnGridLabelLeftDClick( self, event ):
		event.Skip()
	
	def OnNoteBookPageChangedInfoLog( self, event ):
		event.Skip()
	
	def OnButtonClickMUBetsFilter( self, event ):
		event.Skip()
	
	def OnScrollStopBet( self, event ):
		event.Skip()
	
	def OnMenuSelectionSliderStopBet( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	def OnSpinCtrlStopBetGuard( self, event ):
		event.Skip()
	
	def OnScrollCompensate( self, event ):
		event.Skip()
	
	def OnMenuSelectionSliderCompensate( self, event ):
		event.Skip()
	
	
	
	
	
	def OnButtonClickCancelAllBets( self, event ):
		event.Skip()
	
	def OnCheckBoxShowMatched( self, event ):
		event.Skip()
	
	def OnCheckBoxShowUnmatched( self, event ):
		event.Skip()
	
	def OnCheckBoxShowBack( self, event ):
		event.Skip()
	
	def OnCheckBoxShowLay( self, event ):
		event.Skip()
	
	def OnMenuSelectionCancel( self, event ):
		event.Skip()
	
	def OnMenuSelectionModify( self, event ):
		event.Skip()
	
	def OnMenuSelectionCompensate( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetProfitProfit( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetProfitRisk( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetLossProfit( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetLossRisk( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetPause( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetRestart( self, event ):
		event.Skip()
	
	def OnMenuSelectionStopBetCancel( self, event ):
		event.Skip()
	
	def OnCharListBoxMessages( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesSelectAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesDeselectAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesCopySelectedToClipBoard( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesClearSelected( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesClearAll( self, event ):
		event.Skip()
	
	def OnCharListBoxMessagesError( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesErrorSelectAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesErrorDeselectAll( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesErrorCopySelectedToClipBoard( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesErrorClearSelected( self, event ):
		event.Skip()
	
	def OnMenuSelectionLogMessagesErrorClearAll( self, event ):
		event.Skip()
	
	def m_sliderRefreshOnContextMenu( self, event ):
		self.m_sliderRefresh.PopupMenu( self.m_menuSliderRefresh, event.GetPosition() )
		
	def m_treeEventsOnContextMenu( self, event ):
		self.m_treeEvents.PopupMenu( self.m_menuTreeEvents, event.GetPosition() )
		
	def m_listBoxSavedMarketsOnContextMenu( self, event ):
		self.m_listBoxSavedMarkets.PopupMenu( self.m_menuSavedMarkets, event.GetPosition() )
		
	def m_listCtrlFavsOnContextMenu( self, event ):
		self.m_listCtrlFavs.PopupMenu( self.m_menuFavSearch, event.GetPosition() )
		
	def m_treeCtrlCurrentBetsUKOnContextMenu( self, event ):
		self.m_treeCtrlCurrentBetsUK.PopupMenu( self.m_menuCurrentBetsUK, event.GetPosition() )
		
	def m_treeCtrlCurrentBetsAusOnContextMenu( self, event ):
		self.m_treeCtrlCurrentBetsAus.PopupMenu( self.m_menuCurrentBetsAus, event.GetPosition() )
		
	def m_listBoxModLoggingOnContextMenu( self, event ):
		self.m_listBoxModLogging.PopupMenu( self.m_menuModLogging, event.GetPosition() )
		
	def m_bitmapExchangeOnContextMenu( self, event ):
		self.m_bitmapExchange.PopupMenu( self.m_menuWallet, event.GetPosition() )
		
	def m_splitterMarketBetsOnIdle( self, event ):
		self.m_splitterMarketBets.SetSashPosition( 350 )
		self.m_splitterMarketBets.Unbind( wx.EVT_IDLE )
	
	def m_sliderStopBetOnContextMenu( self, event ):
		self.m_sliderStopBet.PopupMenu( self.m_menuSliderStopBet, event.GetPosition() )
		
	def m_sliderCompensateOnContextMenu( self, event ):
		self.m_sliderCompensate.PopupMenu( self.m_menuCompensate, event.GetPosition() )
		
	def m_listCtrlBetsOnContextMenu( self, event ):
		self.m_listCtrlBets.PopupMenu( self.m_menuListBets, event.GetPosition() )
		
	def m_listCtrlStopBetsOnContextMenu( self, event ):
		self.m_listCtrlStopBets.PopupMenu( self.m_menuStopBet, event.GetPosition() )
		
	def m_listBoxMessagesOnContextMenu( self, event ):
		self.m_listBoxMessages.PopupMenu( self.m_menuLogMessages, event.GetPosition() )
		
	def m_listBoxMessagesErrorOnContextMenu( self, event ):
		self.m_listBoxMessagesError.PopupMenu( self.m_menuLogMessagesError, event.GetPosition() )
		

###########################################################################
## Class OverlayMessage
###########################################################################

class OverlayMessage ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.FRAME_NO_TASKBAR|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer92 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer92.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextMessage = wx.StaticText( self, wx.ID_ANY, u"0000000000000000000", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextMessage.Wrap( -1 )
		self.m_staticTextMessage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer92.Add( self.m_staticTextMessage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer92.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer92 )
		self.Layout()
		bSizer92.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ICONIZE, self.OnIconize )
		self.Bind( wx.EVT_SET_FOCUS, self.OnSetFocus )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnIconize( self, event ):
		event.Skip()
	
	def OnSetFocus( self, event ):
		event.Skip()
	

###########################################################################
## Class PatternManager
###########################################################################

class PatternManager ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pattern Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer65 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkListPatterns = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,200 ), [], wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SORT ) 
		bSizer66.Add( self.m_checkListPatterns, 0, wx.ALL, 5 )
		
		bSizer67 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonPatternNew = wx.Button( self, wx.ID_ANY, u"New ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer67.Add( self.m_buttonPatternNew, 0, wx.ALL, 5 )
		
		self.m_buttonPatternEdit = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPatternEdit.Enable( False )
		
		bSizer67.Add( self.m_buttonPatternEdit, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonPatternCopy = wx.Button( self, wx.ID_ANY, u"Copy ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPatternCopy.Enable( False )
		
		bSizer67.Add( self.m_buttonPatternCopy, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_buttonPatternDelete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPatternDelete.Enable( False )
		
		bSizer67.Add( self.m_buttonPatternDelete, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer67.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonCheckAll = wx.Button( self, wx.ID_ANY, u"Check All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer67.Add( self.m_buttonCheckAll, 0, wx.ALL, 5 )
		
		self.m_buttonUncheckAll = wx.Button( self, wx.ID_ANY, u"Uncheck All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer67.Add( self.m_buttonUncheckAll, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer66.Add( bSizer67, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		bSizer65.Add( bSizer66, 0, 0, 5 )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer65.Add( bSizer96, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline292 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer65.Add( self.m_staticline292, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		bSizer87 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer87.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_buttonLoadPatterns = wx.Button( self, wx.ID_ANY, u"Load Checked Patterns", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLoadPatterns.SetDefault() 
		self.m_buttonLoadPatterns.Enable( False )
		
		bSizer87.Add( self.m_buttonLoadPatterns, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxForceRefreshMarketsData = wx.CheckBox( self, wx.ID_ANY, u"Force refresh of market data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxForceRefreshMarketsData.Hide()
		
		bSizer87.Add( self.m_checkBoxForceRefreshMarketsData, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button75 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer87.Add( self.m_button75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer65.Add( bSizer87, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer65 )
		self.Layout()
		bSizer65.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkListPatterns.Bind( wx.EVT_LISTBOX, self.OnCheckListBoxPatterns )
		self.m_checkListPatterns.Bind( wx.EVT_CHECKLISTBOX, self.OnCheckListBoxTogglePatterns )
		self.m_buttonPatternNew.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternNew )
		self.m_buttonPatternEdit.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternEdit )
		self.m_buttonPatternCopy.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternCopy )
		self.m_buttonPatternDelete.Bind( wx.EVT_BUTTON, self.OnButtonClickPatternDelete )
		self.m_buttonCheckAll.Bind( wx.EVT_BUTTON, self.OnButtonClickCheckAll )
		self.m_buttonUncheckAll.Bind( wx.EVT_BUTTON, self.OnButtonClickUncheckAll )
		self.m_buttonLoadPatterns.Bind( wx.EVT_BUTTON, self.OnButtonClickLoad )
		self.m_button75.Bind( wx.EVT_BUTTON, self.OnButtonClickClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheckListBoxPatterns( self, event ):
		event.Skip()
	
	def OnCheckListBoxTogglePatterns( self, event ):
		event.Skip()
	
	def OnButtonClickPatternNew( self, event ):
		event.Skip()
	
	def OnButtonClickPatternEdit( self, event ):
		event.Skip()
	
	def OnButtonClickPatternCopy( self, event ):
		event.Skip()
	
	def OnButtonClickPatternDelete( self, event ):
		event.Skip()
	
	def OnButtonClickCheckAll( self, event ):
		event.Skip()
	
	def OnButtonClickUncheckAll( self, event ):
		event.Skip()
	
	def OnButtonClickLoad( self, event ):
		event.Skip()
	
	def OnButtonClickClose( self, event ):
		event.Skip()
	

###########################################################################
## Class PlaceBet
###########################################################################

class PlaceBet ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Place Bet", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextBetType = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextBetType.Wrap( -1 )
		self.m_staticTextBetType.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer35.Add( self.m_staticTextBetType, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer7.Add( bSizer35, 1, wx.EXPAND|wx.TOP|wx.LEFT, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Odds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer2.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlPrice, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Stake", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlSize = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrlSize, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		bSizer7.Add( fgSizer2, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Risk: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer21.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextRisk = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_LEFT )
		self.m_staticTextRisk.Wrap( -1 )
		bSizer21.Add( self.m_staticTextRisk, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Profit: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer21.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_staticTextProfit = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_LEFT )
		self.m_staticTextProfit.Wrap( -1 )
		bSizer21.Add( self.m_staticTextProfit, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		bSizer7.Add( bSizer21, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.m_staticline52 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline52, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_checkBoxKeepInPlay = wx.CheckBox( self, wx.ID_ANY, u"Keep In-Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_checkBoxKeepInPlay, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline521 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline521, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer88 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxFillOrKill = wx.CheckBox( self.m_panel25, wx.ID_ANY, u"Fill or Kill in", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer88.Add( self.m_checkBoxFillOrKill, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_spinCtrlFillOrKill = wx.SpinCtrl( self.m_panel25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 999, 0 )
		bSizer88.Add( self.m_spinCtrlFillOrKill, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText87 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"secs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )
		bSizer88.Add( self.m_staticText87, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_panel25.SetSizer( bSizer88 )
		self.m_panel25.Layout()
		bSizer88.Fit( self.m_panel25 )
		bSizer7.Add( self.m_panel25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline62 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline62, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonPlaceBet = wx.Button( self, wx.ID_ANY, u"Place Bet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPlaceBet.SetDefault() 
		bSizer12.Add( self.m_buttonPlaceBet, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button3, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrlPrice.Bind( wx.EVT_TEXT, self.OnTextPrice )
		self.m_textCtrlSize.Bind( wx.EVT_TEXT, self.OnTextSize )
		self.m_buttonPlaceBet.Bind( wx.EVT_BUTTON, self.OnButtonClickPlaceBet )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnButtonClickCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTextPrice( self, event ):
		event.Skip()
	
	def OnTextSize( self, event ):
		event.Skip()
	
	def OnButtonClickPlaceBet( self, event ):
		event.Skip()
	
	def OnButtonClickCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class LoginInfoRegistration
###########################################################################

class LoginInfoRegistration ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Betfair registration is missing", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer153 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer154 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_customControlBitmap = wx.StaticBitmap(self)
		infoIcon = wx.ArtProvider.GetIcon(wx.ART_INFORMATION)
		self.m_customControlBitmap.SetIcon(infoIcon)
		bSizer154.Add( self.m_customControlBitmap, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText113 = wx.StaticText( self, wx.ID_ANY, u"You are using the Betfair Verified Edition\nbut it seems you have not completed the\nprocess to self-authorize yourself which is\nrequired to use this edition of the application is\n\nPlease visit:\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )
		bSizer154.Add( self.m_staticText113, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer153.Add( bSizer154, 1, wx.EXPAND, 5 )
		
		self.m_hyperlinkBfppSite = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Bfplusplus Official Site", u"http://www.bfplusplus.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer153.Add( self.m_hyperlinkBfppSite, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline87 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer153.Add( self.m_staticline87, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText1131 = wx.StaticText( self, wx.ID_ANY, u"You may also wisth to visit the development page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1131.Wrap( -1 )
		bSizer153.Add( self.m_staticText1131, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlinkBfppSiteDev = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Bfplusplus Development Site", u"http://code.google.com/p/bfplusplus", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer153.Add( self.m_hyperlinkBfppSiteDev, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline871 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer153.Add( self.m_staticline871, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button53 = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer153.Add( self.m_button53, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer153 )
		self.Layout()
		bSizer153.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_hyperlinkBfppSite.Bind( wx.EVT_HYPERLINK, self.OnHyperLinkBfppSite )
		self.m_hyperlinkBfppSiteDev.Bind( wx.EVT_HYPERLINK, self.OnHyperLinkBfppSiteDev )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnHyperLinkBfppSite( self, event ):
		event.Skip()
	
	def OnHyperLinkBfppSiteDev( self, event ):
		event.Skip()
	

###########################################################################
## Class PrioritizeEvents
###########################################################################

class PrioritizeEvents ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Events Ordering", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer74 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer75 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Events", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		self.m_staticText59.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer75.Add( self.m_staticText59, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		m_listBoxEventsChoices = []
		self.m_listBoxEvents = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,250 ), m_listBoxEventsChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE|wx.LB_SORT )
		bSizer75.Add( self.m_listBoxEvents, 0, wx.ALL, 5 )
		
		bSizer74.Add( bSizer75, 1, wx.EXPAND, 5 )
		
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button35 = wx.Button( self, wx.ID_ANY, u"Add >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.m_button35, 0, wx.ALL, 5 )
		
		self.m_button351 = wx.Button( self, wx.ID_ANY, u"<< Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.m_button351, 0, wx.ALL, 5 )
		
		bSizer74.Add( bSizer78, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer79 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText591 = wx.StaticText( self, wx.ID_ANY, u"Prioritized Events", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )
		self.m_staticText591.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString ) )
		
		bSizer79.Add( self.m_staticText591, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		m_listBoxPrioChoices = []
		self.m_listBoxPrio = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,250 ), m_listBoxPrioChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		bSizer79.Add( self.m_listBoxPrio, 0, wx.ALL, 5 )
		
		bSizer74.Add( bSizer79, 1, wx.EXPAND, 5 )
		
		bSizer80 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button39 = wx.Button( self, wx.ID_ANY, u"Move Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button39, 0, wx.ALL, 5 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, u"Move Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button40, 0, wx.ALL, 5 )
		
		bSizer74.Add( bSizer80, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer71.Add( bSizer74, 1, wx.EXPAND, 5 )
		
		self.m_staticline33 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer71.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer7 = wx.StdDialogButtonSizer()
		self.m_sdbSizer7OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer7.AddButton( self.m_sdbSizer7OK )
		self.m_sdbSizer7Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer7.AddButton( self.m_sdbSizer7Cancel )
		m_sdbSizer7.Realize();
		bSizer71.Add( m_sdbSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		self.SetSizer( bSizer71 )
		self.Layout()
		bSizer71.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button35.Bind( wx.EVT_BUTTON, self.OnButtonClickAdd )
		self.m_button351.Bind( wx.EVT_BUTTON, self.OnButtonClickRemove )
		self.m_button39.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveUp )
		self.m_button40.Bind( wx.EVT_BUTTON, self.OnButtonClickMoveDown )
		self.m_sdbSizer7OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickAdd( self, event ):
		event.Skip()
	
	def OnButtonClickRemove( self, event ):
		event.Skip()
	
	def OnButtonClickMoveUp( self, event ):
		event.Skip()
	
	def OnButtonClickMoveDown( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class ProgressDialog
###########################################################################

class ProgressDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Loading", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_gaugeLoading = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		bSizer23.Add( self.m_gaugeLoading, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextLoading = wx.StaticText( self, wx.ID_ANY, u"Loading", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticTextLoading.Wrap( -1 )
		bSizer23.Add( self.m_staticTextLoading, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer25.Add( bSizer23, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class RunnerAction
###########################################################################

class RunnerAction ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Runner Prices", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer136 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer150 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer143 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextMarket = wx.StaticText( self.m_panel39, wx.ID_ANY, u"Market Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMarket.Wrap( -1 )
		bSizer143.Add( self.m_staticTextMarket, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextMarketName = wx.StaticText( self.m_panel39, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMarketName.Wrap( -1 )
		bSizer143.Add( self.m_staticTextMarketName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer150.Add( bSizer143, 0, wx.EXPAND, 5 )
		
		self.m_staticline73 = wx.StaticLine( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer150.Add( self.m_staticline73, 0, wx.EXPAND, 5 )
		
		bSizer137 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText97 = wx.StaticText( self.m_panel39, wx.ID_ANY, u"Selection:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )
		bSizer137.Add( self.m_staticText97, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choiceRunnersChoices = []
		self.m_choiceRunners = wx.Choice( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceRunnersChoices, 0 )
		self.m_choiceRunners.SetSelection( 0 )
		bSizer137.Add( self.m_choiceRunners, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer150.Add( bSizer137, 0, wx.EXPAND, 5 )
		
		self.m_staticline731 = wx.StaticLine( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer150.Add( self.m_staticline731, 0, wx.EXPAND|wx.BOTTOM, 5 )
		
		self.m_bitmapRunnerAction = wx.StaticBitmap( self.m_panel39, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 350,255 ), 0 )
		bSizer150.Add( self.m_bitmapRunnerAction, 0, 0, 5 )
		
		self.m_staticline77 = wx.StaticLine( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer150.Add( self.m_staticline77, 0, wx.EXPAND, 5 )
		
		bSizer144 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxInverseAxis = wx.CheckBox( self.m_panel39, wx.ID_ANY, u"Inverse Axis", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer144.Add( self.m_checkBoxInverseAxis, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline78 = wx.StaticLine( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer144.Add( self.m_staticline78, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer144.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline781 = wx.StaticLine( self.m_panel39, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer144.Add( self.m_staticline781, 0, wx.EXPAND, 5 )
		
		self.m_bpButton34 = wx.BitmapButton( self.m_panel39, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/arrow_refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer144.Add( self.m_bpButton34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText104 = wx.StaticText( self.m_panel39, wx.ID_ANY, u"Reload Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText104.Wrap( -1 )
		bSizer144.Add( self.m_staticText104, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer150.Add( bSizer144, 0, wx.EXPAND, 5 )
		
		self.m_panel39.SetSizer( bSizer150 )
		self.m_panel39.Layout()
		bSizer150.Fit( self.m_panel39 )
		bSizer136.Add( self.m_panel39, 1, wx.EXPAND, 5 )
		
		self.m_staticline75 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer136.Add( self.m_staticline75, 0, wx.EXPAND, 5 )
		
		self.m_panel40 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer140 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1431 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextMarket1 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Total Matched on the event:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMarket1.Wrap( -1 )
		bSizer1431.Add( self.m_staticTextMarket1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextTotalMatchedEvent = wx.StaticText( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextTotalMatchedEvent.Wrap( -1 )
		bSizer1431.Add( self.m_staticTextTotalMatchedEvent, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer140.Add( bSizer1431, 0, wx.EXPAND, 5 )
		
		bSizer14311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextMarket11 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Matched on the runner:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMarket11.Wrap( -1 )
		bSizer14311.Add( self.m_staticTextMarket11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextTotalMatchedRunner = wx.StaticText( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextTotalMatchedRunner.Wrap( -1 )
		bSizer14311.Add( self.m_staticTextTotalMatchedRunner, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer140.Add( bSizer14311, 0, wx.EXPAND, 5 )
		
		bSizer143111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextMarket111 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Last Price Matched:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMarket111.Wrap( -1 )
		bSizer143111.Add( self.m_staticTextMarket111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextLastPriceMatched = wx.StaticText( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextLastPriceMatched.Wrap( -1 )
		bSizer143111.Add( self.m_staticTextLastPriceMatched, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer140.Add( bSizer143111, 0, wx.EXPAND, 5 )
		
		self.m_gridPricing = wx.grid.Grid( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridPricing.CreateGrid( 0, 3 )
		self.m_gridPricing.EnableEditing( True )
		self.m_gridPricing.EnableGridLines( True )
		self.m_gridPricing.EnableDragGridSize( False )
		self.m_gridPricing.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridPricing.EnableDragColMove( False )
		self.m_gridPricing.EnableDragColSize( True )
		self.m_gridPricing.SetColLabelSize( 30 )
		self.m_gridPricing.SetColLabelValue( 0, u"To Back" )
		self.m_gridPricing.SetColLabelValue( 1, u"To Lay" )
		self.m_gridPricing.SetColLabelValue( 2, u"Traded" )
		self.m_gridPricing.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridPricing.EnableDragRowSize( True )
		self.m_gridPricing.SetRowLabelSize( 65 )
		self.m_gridPricing.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridPricing.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer140.Add( self.m_gridPricing, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel40.SetSizer( bSizer140 )
		self.m_panel40.Layout()
		bSizer140.Fit( self.m_panel40 )
		bSizer136.Add( self.m_panel40, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer136 )
		self.Layout()
		bSizer136.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_choiceRunners.Bind( wx.EVT_CHOICE, self.OnChoiceRunners )
		self.m_checkBoxInverseAxis.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxInverseAxis )
		self.m_bpButton34.Bind( wx.EVT_BUTTON, self.OnButtonClickReloadData )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnChoiceRunners( self, event ):
		event.Skip()
	
	def OnCheckBoxInverseAxis( self, event ):
		event.Skip()
	
	def OnButtonClickReloadData( self, event ):
		event.Skip()
	

###########################################################################
## Class TransientMessage
###########################################################################

class TransientMessage ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 375,75 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.FRAME_NO_TASKBAR|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer84 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextMessages = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticTextMessages.Wrap( 0 )
		bSizer84.Add( self.m_staticTextMessages, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText76.Wrap( -1 )
		self.m_staticText76.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer84.Add( self.m_staticText76, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_ENTER_WINDOW, self.OnEnterWindow )
		self.Bind( wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow )
		self.Bind( wx.EVT_LEFT_UP, self.OnLeftUpStaticText )
		self.Bind( wx.EVT_SET_FOCUS, self.OnSetFocus )
		self.m_staticTextMessages.Bind( wx.EVT_ENTER_WINDOW, self.OnEnterWindowStaticText )
		self.m_staticTextMessages.Bind( wx.EVT_LEAVE_WINDOW, self.OnLeaveWindowStaticText )
		self.m_staticTextMessages.Bind( wx.EVT_LEFT_UP, self.OnLeftUpStaticText )
		self.m_staticText76.Bind( wx.EVT_ENTER_WINDOW, self.OnEnterWindowStaticText )
		self.m_staticText76.Bind( wx.EVT_LEAVE_WINDOW, self.OnLeaveWindowStaticText )
		self.m_staticText76.Bind( wx.EVT_LEFT_UP, self.OnLeftUpStaticText )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnEnterWindow( self, event ):
		event.Skip()
	
	def OnLeaveWindow( self, event ):
		event.Skip()
	
	def OnLeftUpStaticText( self, event ):
		event.Skip()
	
	def OnSetFocus( self, event ):
		event.Skip()
	
	def OnEnterWindowStaticText( self, event ):
		event.Skip()
	
	def OnLeaveWindowStaticText( self, event ):
		event.Skip()
	
	
	
	
	

###########################################################################
## Class UpdateChecker
###########################################################################

class UpdateChecker ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bfplusplus Pre-start Update Checker", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer149 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText112 = wx.StaticText( self, wx.ID_ANY, u"Bfplusplus has to check once a week for possible compulsory updates to solve service affecting bugs or implement new needed API features", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText112.Wrap( 225 )
		bSizer149.Add( self.m_staticText112, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText1121111 = wx.StaticText( self, wx.ID_ANY, u"This ensures compliance with Betfair policies and that the application can remain free", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1121111.Wrap( 225 )
		bSizer149.Add( self.m_staticText1121111, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline85 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer149.Add( self.m_staticline85, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonDoCheck = wx.Button( self, wx.ID_ANY, u"Proceed with update check", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_buttonDoCheck, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonDoExit = wx.Button( self, wx.ID_ANY, u"Exit Bfplusplus", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_buttonDoExit, 0, wx.ALL, 5 )
		
		bSizer149.Add( bSizer152, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline851 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer149.Add( self.m_staticline851, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_gaugeUpdateChecking = wx.Gauge( self, wx.ID_ANY, 0, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gaugeUpdateChecking.SetValue( 20 ) 
		bSizer149.Add( self.m_gaugeUpdateChecking, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticTextUpdateTimer = wx.StaticText( self, wx.ID_ANY, u"20 secs remaining", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUpdateTimer.Wrap( -1 )
		bSizer149.Add( self.m_staticTextUpdateTimer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline83 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer149.Add( self.m_staticline83, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_textCtrlUpdateResult = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrlUpdateResult.SetMinSize( wx.Size( -1,150 ) )
		
		bSizer149.Add( self.m_textCtrlUpdateResult, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline84 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer149.Add( self.m_staticline84, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonOpenBrowser = wx.Button( self, wx.ID_ANY, u"Open browser to download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonOpenBrowser.Enable( False )
		
		bSizer151.Add( self.m_buttonOpenBrowser, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonReturn = wx.Button( self, wx.ID_ANY, u"Return to Bfplusplus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonReturn.Enable( False )
		
		bSizer151.Add( self.m_buttonReturn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer149.Add( bSizer151, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer149 )
		self.Layout()
		bSizer149.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonDoCheck.Bind( wx.EVT_BUTTON, self.OnButtonClickDoCheck )
		self.m_buttonDoExit.Bind( wx.EVT_BUTTON, self.OnButtonClickDoExit )
		self.m_buttonOpenBrowser.Bind( wx.EVT_BUTTON, self.OnButtonClickBrowser )
		self.m_buttonReturn.Bind( wx.EVT_BUTTON, self.OnButtonClickReturn )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickDoCheck( self, event ):
		event.Skip()
	
	def OnButtonClickDoExit( self, event ):
		event.Skip()
	
	def OnButtonClickBrowser( self, event ):
		event.Skip()
	
	def OnButtonClickReturn( self, event ):
		event.Skip()
	

###########################################################################
## Class UserSecurity
###########################################################################

class UserSecurity ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Username storage security Warning", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer146 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap35 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"icons/famfamfam-silk/exclamation32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_bitmap35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText109 = wx.StaticText( self, wx.ID_ANY, u"WARNING!\n\nIf you choose this option, your Betfair account could be compromised.\n\nIf anyone accesses your computer, then that person will have access\nto your account usernames, including if your computer is stolen\n\nDo you still want Bfplusplus to remember usernames?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )
		bSizer152.Add( self.m_staticText109, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer146.Add( bSizer152, 1, wx.EXPAND, 5 )
		
		self.m_staticline80 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer146.Add( self.m_staticline80, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer147 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button47 = wx.Button( self, wx.ID_ANY, u"No, I don't want", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button47.SetDefault() 
		bSizer147.Add( self.m_button47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Yes, proceed and save usernames", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer147.Add( self.m_button48, 0, wx.ALL, 5 )
		
		bSizer146.Add( bSizer147, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer146 )
		self.Layout()
		bSizer146.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button47.Bind( wx.EVT_BUTTON, self.OnButtonClickNo )
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnButtonClickYes )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickNo( self, event ):
		event.Skip()
	
	def OnButtonClickYes( self, event ):
		event.Skip()
	

