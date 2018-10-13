import wx

class WxFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(800,400))
        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE) #??? Find out what this does (Text editor maybe)
        self.Show(True)
        
        #Individual options
        file_menu = wx.Menu()
        menu_exit = file_menu.Append(wx.ID_EXIT,'&Exit','Close Program')

        #Menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu,'&File') #Is the ampersand required?
        self.SetMenuBar(menu_bar)

        #Events
        self.Bind(wx.EVT_MENUw,self.onExit,menu_exit)

        #Displays contents of each button
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)  #Create button orientation
        self.buttons = [] #Build list and add buttons
        for i in range(0, 6):
            self.buttons.append(wx.Button(self,-1,"Button&{}".format(str(i))))
            self.sizer2.Add(self.buttons[i],1,wx.EXPAND) #Adds buttons to bottom horizontally

        #TODO Find out what these options do
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.EXPAND)

        #TODO Find out what these options do
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    def onExit(self,e):
        self.Close(True)

app = wx.App(False)
frame = WxFrame(None,'Hello World')
app.MainLoop()