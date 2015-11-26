# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Karkínos - Sistema de Ayuda a la Decisión para la evaluación del riesgo de cáncer genético", pos = wx.DefaultPosition, size = wx.Size( 950,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 950,500 ), wx.Size( 950,550 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Historias Clínicas" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 250,530 ) ) 
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_SORT )
		sbSizer1.Add( self.m_listBox1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Evaluar historia clínica", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer1.Add( self.m_button1, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		fgSizer1.Add( sbSizer1, 1, 0, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Diagnóstico" ), wx.VERTICAL )
		
		sbSizer2.SetMinSize( wx.Size( 680,520 ) ) 
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_indice = wx.StaticText( self, wx.ID_ANY, u"Caso índice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_indice.Wrap( -1 )
		self.label_indice.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		self.label_indice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.label_indice, 0, wx.ALL, 5 )
		
		self.text_indice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.text_indice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.text_indice.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer3.Add( self.text_indice, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_informativo = wx.StaticText( self, wx.ID_ANY, u"Informativo - No Informativo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_informativo.Wrap( -1 )
		self.label_informativo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		self.label_informativo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.label_informativo, 0, wx.ALL, 5 )
		
		self.text_informativo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.text_informativo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.text_informativo.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.text_informativo.SetMinSize( wx.Size( -1,90 ) )
		
		bSizer3.Add( self.text_informativo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_asociados = wx.StaticText( self, wx.ID_ANY, u"Casos asociados", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_asociados.Wrap( -1 )
		self.label_asociados.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		self.label_asociados.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.label_asociados, 0, wx.ALL, 5 )
		
		self.text_asociados = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.text_asociados.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.text_asociados.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.text_asociados.SetMinSize( wx.Size( -1,90 ) )
		
		bSizer3.Add( self.text_asociados, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_diagnostico = wx.StaticText( self, wx.ID_ANY, u"Diagnóstico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_diagnostico.Wrap( -1 )
		self.label_diagnostico.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		self.label_diagnostico.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.label_diagnostico, 0, wx.ALL, 5 )
		
		self.text_diagnostico = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.text_diagnostico.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.text_diagnostico.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.text_diagnostico.SetMinSize( wx.Size( -1,120 ) )
		
		bSizer3.Add( self.text_diagnostico, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_evaluation = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_evaluation.Wrap( -1 )
		self.label_evaluation.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 91, False, wx.EmptyString ) )
		self.label_evaluation.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.label_evaluation, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer1.Add( sbSizer2, 1, 0, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_listBox1.Bind( wx.EVT_LISTBOX, self.m_listBox1OnListBox )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		pass
	

	# Virtual event handlers, overide them in your derived class
	def m_listBox1OnListBox( self, event ):
		event.Skip()
	
	def m_button1OnButtonClick( self, event ):
		event.Skip()
	
	

app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()

	

