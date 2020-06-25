import wx
import wx.media

class myFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None,title='Music Player')
		panel=wx.Panel(self)
		

		mySizer=wx.BoxSizer(wx.VERTICAL)

		self.mc=wx.media.MediaCtrl(panel)
		mySizer.Add(self.mc,0,wx.ALL | wx.EXPAND,5)

		playButton=wx.Button(panel,label='Play')
		mySizer.Add(playButton,0,wx.ALL | wx.CENTER,5)
		playButton.Bind(wx.EVT_BUTTON,self.onPlay)

		loadButton=wx.Button(panel,label='Load')
		mySizer.Add(loadButton,0,wx.ALL | wx.CENTER,5)
		loadButton.Bind(wx.EVT_BUTTON,self.onLoadFile)

		pauseButton=wx.Button(panel,label='Pause')
		mySizer.Add(pauseButton,0,wx.ALL | wx.CENTER,5)
		pauseButton.Bind(wx.EVT_BUTTON,self.onPause)

		stopButton=wx.Button(panel,label='Stop')
		mySizer.Add(stopButton,0,wx.ALL | wx.CENTER,5)
		stopButton.Bind(wx.EVT_BUTTON,self.onStop)

		panel.SetSizer(mySizer)
		self.Show()

	def onLoadFile(self,event):
		wildcard="*.mp3;*wav"
		style=wx.FD_OPEN
		fileDialog=wx.FileDialog(self,"Choose a file",wildcard=wildcard,style=style)
		if fileDialog.ShowModal()==wx.ID_OK:
			path=fileDialog.GetPath()
			self.mc.Load(path)

		fileDialog.Destroy()

	def onPlay(self,event):
		self.mc.Play()

	def onPause(self,event):
		self.mc.Pause()

	def onStop(self,event):
		self.mc.Stop()

if __name__ == '__main__':
	app = wx.App()
	frame = myFrame()
	app.MainLoop() 