import wx
import wx.media

# Box in which all widgets are placed
class myFrame(wx.Frame):
	def __init__(self,parent=None,id=-1):
		wx.Frame.__init__(self,parent,id,'Music Player')
		self.panel=wx.Panel(self)
		

		mySizer=wx.BoxSizer(wx.VERTICAL)

		self.mc=wx.media.MediaCtrl(self.panel)
		mySizer.Add(self.mc,0,wx.ALL | wx.EXPAND,5)

		self.slider=wx.Slider(self.panel,-1,0,0,0,size=wx.Size(300,-1))
		self.Bind(wx.EVT_SLIDER,self.onSeek,self.slider)

		self.timer=wx.Timer(self)
		self.Bind(wx.EVT_TIMER,self.onTimer,self.timer)

		playButton=wx.Button(self.panel,-1,label='Play')
		mySizer.Add(playButton,0,wx.ALL | wx.CENTER,5)
		self.Bind(wx.EVT_BUTTON,self.onPlay,playButton)

		loadButton=wx.Button(self.panel,-1,label='Load')
		mySizer.Add(loadButton,0,wx.ALL | wx.CENTER,5)
		self.Bind(wx.EVT_BUTTON,self.onLoadFile,loadButton)

		pauseButton=wx.Button(self.panel,-1,label='Pause')
		mySizer.Add(pauseButton,0,wx.ALL | wx.CENTER,5)
		self.Bind(wx.EVT_BUTTON,self.onPause,pauseButton)

		stopButton=wx.Button(self.panel,-1,label='Stop')
		mySizer.Add(stopButton,0,wx.ALL | wx.CENTER,5)
		stopButton.Bind(wx.EVT_BUTTON,self.onStop,stopButton)

		self.panel.SetSizer(mySizer)
		self.Show()
	# function to load file
	def onLoadFile(self,event):
		wildcard="*.mp3;*wav"
		style=wx.FD_OPEN
		fileDialog=wx.FileDialog(self,"Choose a file",wildcard=wildcard,style=style)
		if fileDialog.ShowModal()==wx.ID_OK:
			path=fileDialog.GetPath()
			self.mc.Load(path)

		fileDialog.Destroy()
   # function to play
	def onPlay(self,event):
		self.mc.Play()
		self.timer.Start(100)
		self.slider.SetRange(0,self.mc.Length())
	# function to pause
	def onPause(self,event):
		self.mc.Pause()
    # function to stop
	def onStop(self,event):
		self.mc.Stop()
    # functions for slider
	def onTimer(self,event):
		updateslider=self.mc.Tell()
		self.slider.SetValue(updateslider)

	def onSeek(self,event):
		dragslider=self.slider.GetValue()
		self.mc.Seek(dragslider)

if __name__ == '__main__':
	app = wx.App()
	frame = myFrame()
	app.MainLoop() 