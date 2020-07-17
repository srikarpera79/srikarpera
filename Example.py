import wx

class Calci(wx.Frame):
    
    str=''
    counter = 0
    temp=float(0)
    tp=float(0)

    flag = 0
    
    def __init__(self,parent,title):
        super().__init__(parent=None,title='CALCI',size=(200,160))

        p=wx.Panel(self)
        p1=wx.Panel(p)
        p2=wx.Panel(p)
        
        bsizer=wx.BoxSizer(wx.VERTICAL)
        bs = wx.BoxSizer(wx.VERTICAL)

        self.t=wx.TextCtrl(p1)
        bs.Add(self.t,0,wx.EXPAND)

        self.b1=wx.Button(p2,label='AC')
        self.b2=wx.Button(p2,label='C')
        self.b3=wx.Button(p2,label='%')
        self.b4=wx.Button(p2,label='/')
        self.b5=wx.Button(p2,label='7')
        self.b6=wx.Button(p2,label='8')
        self.b7=wx.Button(p2,label='9')
        self.b8=wx.Button(p2,label='*')
        self.b9=wx.Button(p2,label='4')
        self.b10=wx.Button(p2,label='5')
        self.b11=wx.Button(p2,label='6')
        self.b12=wx.Button(p2,label='-')
        self.b13=wx.Button(p2,label='1')
        self.b14=wx.Button(p2,label='2')
        self.b15=wx.Button(p2,label='3')
        self.b16=wx.Button(p2,label='+')
        self.b17=wx.Button(p2,label='0')
        self.b18=wx.Button(p2,label='+/-')
        self.b19=wx.Button(p2,label='.')
        self.b20=wx.Button(p2,label='=')

        gs=wx.GridSizer(5,4,1,1)
        gs.Add(self.b1,0,wx.EXPAND,4)
        gs.Add(self.b2,0,wx.EXPAND,4)
        gs.Add(self.b3,0,wx.EXPAND,4)
        gs.Add(self.b4,0,wx.EXPAND,4)
        gs.Add(self.b5,0,wx.EXPAND,4)
        gs.Add(self.b6,0,wx.EXPAND,4)
        gs.Add(self.b7,0,wx.EXPAND,4)
        gs.Add(self.b8,0,wx.EXPAND,4)
        gs.Add(self.b9,0,wx.EXPAND,4)
        gs.Add(self.b10,0,wx.EXPAND,4)
        gs.Add(self.b11,0,wx.EXPAND,4)
        gs.Add(self.b12,0,wx.EXPAND,4)
        gs.Add(self.b13,0,wx.EXPAND,4)
        gs.Add(self.b14,0,wx.EXPAND,4)
        gs.Add(self.b15,0,wx.EXPAND,4)
        gs.Add(self.b16,0,wx.EXPAND,4)
        gs.Add(self.b17,0,wx.EXPAND,4)
        gs.Add(self.b18,0,wx.EXPAND,4)
        gs.Add(self.b19,0,wx.EXPAND,4)
        gs.Add(self.b20,0,wx.EXPAND,4)

        self.b1.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b2.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b3.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b4.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b5.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b6.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b7.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b8.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b9.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b10.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b11.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b12.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b13.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b14.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b15.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b16.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b17.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b18.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b19.Bind(wx.EVT_BUTTON,self.OnClicked)
        self.b20.Bind(wx.EVT_BUTTON,self.OnClicked)

        p1.SetSizer(bs)
        p2.SetSizer(gs)

        bsizer.Add(p1,0,wx.EXPAND)
        bsizer.Add(p2,0,wx.EXPAND)

        p.SetSizer(bsizer)

        self.Center()
        self.Show()


    def OnClicked(self, event):
        
       
        if event.GetEventObject()==self.b5:
            
            Calci.counter+=1
            Calci.str = Calci.str+('7')
            self.t.SetValue(Calci.str)


        if event.GetEventObject()==self.b6:
            Calci.counter+=1
            Calci.str=Calci.str+('8')
            self.t.SetValue(Calci.str)


        if event.GetEventObject()==self.b7:
            Calci.counter+=1
            Calci.str=Calci.str+('9')
            self.t.SetValue(Calci.str)

        if event.GetEventObject()==self.b9:

            Calci.counter+=1
            Calci.str=Calci.str+('4')
            self.t.SetValue(Calci.str)
            
        if event.GetEventObject()==self.b10:
            Calci.counter+=1
            Calci.str=Calci.str+('5')
            self.t.SetValue(Calci.str)
            
        if event.GetEventObject()==self.b11:
            Calci.counter+=1
            Calci.str=Calci.str+('6')
            self.t.SetValue(Calci.str)

            
        if event.GetEventObject()==self.b13:
            Calci.counter+=1
            Calci.str=Calci.str+('1')
            self.t.SetValue(Calci.str)
            
            
        if event.GetEventObject()==self.b14:
            Calci.counter+=1
            Calci.str=Calci.str+('2')
            self.t.SetValue(Calci.str)
            
        if event.GetEventObject()==self.b15:
            Calci.counter+=1
            Calci.str=Calci.str+('3')
            self.t.SetValue(Calci.str)
            
        if event.GetEventObject()==self.b17:
            Calci.counter+=1
            Calci.str=Calci.str+('0')
            self.t.SetValue(Calci.str)
            
        if event.GetEventObject()==self.b1:
            #Calci.flag = False
            Calci.counter=0
            Calci.str=''
            Calci.temp = 0.0
            self.t.SetValue(Calci.str)

        if event.GetEventObject()==self.b2:
            
            #Calci.flag = False
            Calci.counter=0
            Calci.temp=0.0
            Calci.str=''
            self.t.SetValue(str(Calci.temp))

        if event.GetEventObject()==self.b4:
            tp=float(Calci.str)
            Calci.temp = Calci.temp / tp
            Calci.str=''

            Calci.flag=4
        
        if event.GetEventObject()==self.b8:
            tp = float(Calci.str)
            Calci.temp = Calci.temp * tp
            Calci.str=''
            Calci.flag=3
            
        if event.GetEventObject()==self.b12:
            tp=float(Calci.str)
            Calci.temp = Calci.str
            Calci.str=''
            Calci.temp = Calci.temp - tp
            Calci.str=''
            Calci.flag=2
        if event.GetEventObject()==self.b16:
            tp=float(Calci.str)

            Calci.temp = Calci.temp + tp
            Calci.str=''
            Calci.flag=1
           
            self.t.SetValue(str(Calci.temp))

        if event.GetEventObject()==self.b18:
            
            self.t.SetValue(str(Calci.temp))

        if event.GetEventObject()==self.b19:
             
            Calci.str=Calci.str+('.') 
            self.t.SetValue(Calci.str)
            #Calci.flag= True
            
            #self.t.SetValue(str(Calci.temp))
            #Calci.temp=0


        if event.GetEventObject()==self.b20:
            self.t.SetValue(str(Calci.temp))
            Calci.str=''
            Calci.temp=''
            """ if Calci.flag == 1:
                Calci.temp=int(Calci.str) +Calci.temp
            if Calci.flag == 2:
                Calci.temp=int(Calci.str) -Calci.temp
            if Calci.flag == 3:
                Calci.temp=int(Calci.str) *Calci.temp
            if Calci.flag == 4:
                Calci.temp=int(Calci.str) / Calci.temp
            """
             
            
            




if __name__ == '__main__':
    app=wx.App()
    name =Calci(parent = None,title = 'Calci')
    app.MainLoop()


        






        