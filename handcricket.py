from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown 
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.textinput import TextInput
import pickle
import os
import random
r1=None
teamu=None
teamc=None
o=None
name='Guest'
class SM(ScreenManager):
    pass
class NameScreen(Screen):
    def submit(self,nam):
        global name,dis
        name=nam
        self.manager.current='main'
class MainScreen(Screen):
   def dis(self,*args):
       if name=='Enter Your Name':
           self.l1289.text='Welcome Guest'
       else:
         self.l1289.text='Welcome '+str(name)
class OverScreen(Screen):
    def submit(self,o1):
        global o
        try:
         o=int(o1)
         self.manager.current='team'
        except:
            self.l1.text='Enter Integer Value Only'
class TossScreen(Screen):
    def ch(self,r12):
        global r1
        r1=r12
        self.manager.current='mainp'
    def submit(self,toss1):
        l=['H','T']
        try:
         self.ids.ma.clear_widgets()
        except:
            pass
        self.c111=toss1
        self.toss12=toss1
        if self.c111 in l or self.c111.capitalize() in l:
            self.toss()
        else:
            self.ids.ma.add_widget(Label(text='enter H or T only'))
    def toss(self,*args):
        l=['H','T']
        r=random.choice(l)
        global r1
        if r==self.c111 or r==self.c111.capitalize():
            self.ids.ma.add_widget(Label(text='You won the Toss choose'))
            self.bat.opacity=1
            self.bowl.opacity=1
            self.bat.disable=False
            self.bowl.disable=False
        elif self.toss12 in l or self.toss12.capitalize() in l:
            self.ids.ma.add_widget(Label(text='You Loss the Toss'))
            l1=['bat','bowl']
            r1=random.choice(l1)
            self.ids.ma.add_widget(Label(text='Opponent choose to '+r1))
            if r1=='bat':
                r1='bowl'
                self.manager.current='mainp'
            elif r1=='bowl':
                r1='bat'
                self.manager.current='mainp'
class LuckTScreen(Screen):
    def test(self,*args):
        try:
          self.n=int(self.t1.text)
          a1=str(self.n)
          a=len(a1)
          self.g=random.randint(0,10**a)
          if a>=2:
            if self.g>self.n:
                self.d=self.g-self.n
                b=(self.d)/(10**(a-2))
                self.l=100-b
            else:
                self.d=self.n-self.g
                b=(self.d)/(10**(a-2))
                self.l=100-b
          else:
            if self.g>self.n:
                self.d=self.g-self.n
                self.l=(10-self.d)*10
            else:
                self.d=self.n-self.g
                self.l=(10-self.d)*10
          self.output()
        except:
             self.l1.text='enter number only'
   
    def output(self):
        self.l1.text='Your Number ='+str(self.n)
        self.l22.text='Random Number Taken was '+str(self.g)
        self.l3.text='Difference ='+str(self.d)
        self.l4.text='Luck percentage ='+str(self.l)
class LeaderScreen(Screen):
     def Leader(self,*args):
        with open('games.pickle', 'rb') as f:
             c3= pickle.load(f)
        self.ids.grid1.clear_widgets()
        self.ids.grid1.add_widget(Label(text='Name'))
        self.ids.grid1.add_widget(Label(text='Wins'))
        self.ids.grid1.add_widget(Label(text='Loss'))
        self.ids.grid1.add_widget(Label(text='Draws'))
        self.ids.grid1.add_widget(Label(text='Total Played'))
        for x in c3:
             self.ids.grid1.add_widget(Label(text=str(x)))
             self.ids.grid1.add_widget(Label(text=str(c3[x][0])))
             self.ids.grid1.add_widget(Label(text=str(c3[x][1])))
             self.ids.grid1.add_widget(Label(text=str(c3[x][2])))
             self.ids.grid1.add_widget(Label(text=str(c3[x][3])))
     def ini(self):
        self.ids.grid1.clear_widgets()
class EditScreen(Screen):
    pass
class ChooseScreen(Screen):
    pass
class TeamsScreen(Screen):
    def team(self,*args):
        a=open('teams.pickle','rb')
        b=pickle.load(a)
        c=int(len(b)/4)+1
        self.ids.ma.cols=c
        try:
         self.ids.ma.clear_widgets()
        except:
            pass
        for b1 in b:
          self.ids.ma.add_widget(Label(text=str(b1)))
    def submit(self,team1):
        global dis
        self.ids.ma.clear_widgets()
        a=open('teams.pickle','rb')
        b=pickle.load(a)
        if team1.capitalize()in b.keys() or team1 in b.keys():
          global teamu,teamc
          teamu=team1
          while True:
             teamc=random.choice(list(b.keys()))
             if teamc!=team1:
                 break
          self.ids.ma.add_widget(Label(text='Opponent Team='+teamu))
          self.manager.current='toss'
        else:
            self.ids.ma.add_widget(Label(text='enter a vaild team name'))
    def change1(self):
        self.manager.current='toss'
class CrickScreen(Screen):
    def ini(self):
        global r1,teamu,teamc,name,o
        self.a=open('teams.pickle','rb')
        self.b=pickle.load(self.a)
        self.k1=0
        self.k2=0
        self.o1=0
        self.o2=0
        self.r2=0
        self.r1=0
        self.i1=0
        self.l21=self.b[teamc]
        self.l2=self.b[teamu.capitalize()]
        self.ids['l117'].text=''
        self.ids['l118'].text=''
        self.ids['l115'].text=''
        self.ids['l116'].text=''
        self.ids['l114'].text=''
    def frist(self):
        self.ids['l117'].text='Wickets = '+str(self.k1)
        self.ids['l118'].text="Over="+str(self.o1/6)+" Balls ="+str(self.o1%6)
        self.ids['l115'].text='Runs = '+str(self.r1)
        self.ids['l116'].text="Batman's Name = "+str(self.l2[0])
        self.ids['l114'].text="Bowler's Name ="+str(self.l21[random.randint(0,10)])
    def second(self):
        self.ids['l117'].text='Wickets = '+str(self.k2)
        self.ids['l118'].text="Over="+str(self.o2/6)+" Balls ="+str(self.o2%6)
        self.ids['l115'].text='Runs = '+str(self.r2)
        self.ids['l116'].text="Batman's Name = "+str(self.l21[0])
        self.ids['l114'].text="Bowler's Name ="+str(self.l2[random.randint(0,10)])
    def submit(self,c23):
        self.ids['l119'].text=" "  
        try:
           c23=int(c23)
           if c23 not in range(7):
               self.ids['l119'].text="Enter Number Between 0 to 6 only"
               return 0
        except:
           self.ids['l119'].text="Enter Number Only"
           return 0
        if self.i1==0:
          if r1=='bat':
           if self.r1==0 and self.k1==0:
             self.frist()
             self.l=self.l2[0]
             self.l1=self.l21[random.randint(0,10)]
             self.batting(c23)
           else:
            self.batting(c23)
          elif r1=='bowl':
            if self.r2==0 and self.k2==0:
             self.second()
             self.l1=self.l21[0]
             self.l=self.l2[random.randint(0,10)]
             self.bowling(c23)
            else: 
             self.bowling(c23)
        elif self.i1==1:
            if r1=='bat':
                if self.r2==0 and self.k2==0:
                  self.l=self.l2[0]
                  self.l1=self.l21[random.randint(0,10)]
                  self.second()
                  self.bowling(c23)
                else:
                 self.bowling(c23)
            elif r1=='bowl':
              if self.r1==0 and self.k1==0:
                self.l1=self.l2[0]
                self.l=self.l21[random.randint(0,10)]
                self.frist()
                self.batting(c23)
              else:
                  self.batting(c23) 
    def batting(self,c23):
        if self.i1==0:
          if self.k1<10 and self.o1<(o*6):
            if c23 in range(7):
                 c13=random.randint(0,6)
                 if(c23==c13):
                     self.k1+=1
                     self.o1+=1
                     self.ids['l119'].text="Opsss You Are Out"
                     self.l=self.l2[self.k1]
                     self.ids['l116'].text="Batman's Name = "+str(self.l)
                     self.ids['l117'].text='Wickets = '+str(self.k1)
                     self.ids['l118'].text="Over="+str(int(self.o1/6))+" Balls ="+str(self.o1%6)
                 elif (c23==0 or c13==0):
                     self.ids['l119'].text="No Ball"
                     if c23==0:
                      self.r1+=c13
                      self.ids['l115'].text="Runs = "+str(self.r1)
                     else:
                       self.r1+=c23
                       self.ids['l115'].text="Runs = "+str(self.r1)
                 else:
                     self.r1+=c23
                     self.o1+=1
                     self.ids['l115'].text="Runs = "+str(self.r1)
                     self.ids['l118'].text="Over= "+str(int(self.o1/6))+" Balls ="+str(self.o1%6)
                 if self.k1>=10 or self.o1>=(o*6):
                    self.i1=1
                    self.ids['l119'].text="End of 1 innings"
                    return 0
                 if self.o1%6==0 and self.o1!=0:
                    self.ids['l114'].text="Bowler's Name ="+str(self.l21[random.randint(0,10)])
        else:
          if self.k1<10 and self.o1<(o*6):  
            if c23 in range(7):
                 c13=random.randint(0,6)
                 if(c23==c13):
                     self.k1+=1
                     self.o1+=1
                     self.ids['l119'].text="Opsss You Are Out"
                     self.ids['l117'].text='Wickets = '+str(self.k1)
                     self.l=self.l2[self.k1]
                     self.ids['l118'].text="Over= "+str(int(self.o1/6))+" Balls ="+str(self.o1%6)
                 elif (c23==0 or c13==0):
                     self.ids['l119'].text="No Ball"
                     if c23==0:
                      self.r1+=c13
                      self.ids['l115'].text="Runs = "+str(self.r1)
                      
                     else:
                       self.r1+=c23
                       self.ids['l115'].text="Runs = "+str(self.r1)
                 else:
                     self.r1+=c23
                     self.o1+=1
                     self.ids['l115'].text="Runs = "+str(self.r1)
                     self.ids['l118'].text="Over= "+str(int(self.o1/6))+" Balls ="+str(self.o1%6)
                 if self.r2<self.r1:
                    self.manager.current='winner'
                 if self.o1%6==0:
                    self.ids['l114'].text="Bowler's Name ="+str(self.l21[random.randint(0,10)]) 
          else:
              if self.r1==self.r2:
                  self.manager.current='draw'
              else:
                self.manager.current='loose'
    def bowling(self,c23):
        if self.i1==0:
           if self.k2<10 and self.o2<(o*6):
            if c23 in range(7):
                 c13=random.randint(0,6)
                 if(c23==c13):
                     self.k2+=1
                     self.o2+=1
                     self.ids['l119'].text="Woow He is Out"
                     self.l1=self.l21[self.k2]
                     self.ids['l116'].text="Batman's Name = "+str(self.l1)
                     self.ids['l117'].text='Wickets = '+str(self.k2)
                     self.ids['l118'].text="Over="+str(int(self.o2/6))+" Balls ="+str(self.o2%6)
                 elif (c23==0 or c13==0):
                     self.ids['l119'].text="No Ball"
                     if c23==0:
                      self.r2+=c13
                      self.ids['l115'].text="Runs = "+str(self.r2)
                     else:
                       self.r2+=c23
                       self.ids['l115'].text="Runs = "+str(self.r2)
                 else:
                     self.r2+=c13
                     self.o2+=1
                     self.ids['l115'].text="Runs = "+str(self.r2)
                     self.ids['l118'].text="Over="+str(int(self.o2/6))+" Balls ="+str(self.o2%6)
                 if self.k2>=10 or self.o2>=(o*6):
                  self.ids['l119'].text="End of 1 innings"   
                  self.i1=1
                  return 0
                 if self.o2%6==0 and self.o2!=0:
                    self.ids['l114'].text="Bowler's Name ="+str(self.l2[random.randint(0,10)])
                 
        else:
           if self.k2<10 and self.o2<(o*6):  
            if c23 in range(7):
                 c13=random.randint(0,6)
                 if(c23==c13):
                     self.k2+=1
                     self.o2+=1
                     self.ids['l119'].text="Woww He is Out"
                     self.ids['l117'].text='Wickets = '+str(self.k2)
                     self.l=self.l2[self.k2]
                     self.ids['l118'].text="Over="+str(int(self.o2/6))+" Balls ="+str(self.o2%6)
                 elif (c23==0 or c13==0):
                     self.ids['l114'].text="No Ball"
                     if c23==0:
                      self.r2+=c13
                      self.ids['l115'].text="Runs = "+str(self.r1)
                     else:
                       self.r2+=c23
                       self.ids['l115'].text="Runs = "+str(self.r1)
                 else:
                     self.r2+=c13
                     self.o2+=1
                     self.ids['l115'].text="Runs = "+str(self.r2)
                     self.ids['l118'].text="Over="+str(int(self.o2/6))+" Balls ="+str(self.o2%6)
                 if self.o2%6==0:
                    self.ids['l114'].text="Bowler's Name ="+str(self.l2[random.randint(0,10)])   
            if self.r2>self.r1:
                self.manager.current='loose'
           else:
              if self.r1==self.r2:
                  self.manager.current='draw'
              else:
                 self.manager.current='winner'
class WinnerScreen(Screen):
    def ini(self):
        global name
        a=open('games.pickle','rb')
        b=pickle.load(a)
        c=open('games.pickle','wb')
        if name in b:
            b[name][0]+=1
            b[name][3]+=1
        else:
              b[name]=[1,0,0,1]
        pickle.dump(b,c)
        c.close()
        a.close()
        os.remove('games.pickle')
        os.rename('games1.pickle','games.pickle')
class LooseScreen(Screen):
    def ini(self):
        global name
        a=open('games.pickle','rb')
        b=pickle.load(a)
        c=open('games.pickle','wb')
        if name in b:
            b[name][1]+=1
            b[name][3]+=1
        else:
              b[name]=[0,1,0,1]
        pickle.dump(b,c)
        c.close()
        a.close()
        os.remove('games.pickle')
        os.rename('games1.pickle','games.pickle')
class DrawScreen(Screen):
    def ini(self):
        global name
        a=open('games.pickle','rb')
        b=pickle.load(a)
        c=open('games.pickle','wb')
        if name in b:
            b[name][2]+=1
            b[name][3]+=1
        else:
              b[name]=[0,0,1,1]
        pickle.dump(b,c)
        c.close()
        a.close()
        os.remove('games.pickle')
        os.rename('games1.pickle','games.pickle')
class EditTScreen(Screen):
    def select(self,team):
        global team1
        c=self.c[team]
        team1=team
        self.dropdown.select(team)
        self.dropdown1=DropDown() 
        for i in c:
             btn = Button(text=i,size_hint_y=None,)
             btn.bind(on_release = lambda btn:self.select1(btn.text))
             self.dropdown1.add_widget(btn)
        mainbutton = Button(text ='Select Player', size_hint =(None,None),pos_hint={'x':.3,'y':0.7}) 
        mainbutton.bind(on_release=self.dropdown1.open) 
        self.dropdown1.bind(on_select=lambda instance,x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)
    def select1(self,player):
        global team1,player1
        player1=player
        self.l1.text=' '
        self.dropdown1.select(player)
        self.change=TextInput(text='Enter Name to what you want for '+player,size_hint=(1,.06),pos_hint={'x':0,'y':.56},multiline=False)
        self.add_widget(self.change)
        btn=Button(text ='Submit', size_hint =(None,None),pos_hint={'x':.5,'y':0.3})
        btn.bind(on_release=lambda x:self.ch())
        self.add_widget(btn)
    def ch(self):
        global team1,player1
        b=open('teams1.pickle','wb')
        player2=self.change.text
        k=self.c[team1]
        for x  in range(len(k)):
            if k[x]==player1:
                k[x]=player2
                self.c[team1]=k
        pickle.dump(self.c,b)
        self.a.close()
        b.close()
        os.remove('teams.pickle')
        os.rename('teams1.pickle','teams.pickle')
        self.l1.text='Changed '+player1+' to '+player2+' Succesfully'
        self.ini()
    def ini(self):
        self.a=open('teams.pickle','rb')
        self.c=pickle.load(self.a)
        self.dropdown=DropDown() 
        for i in self.c:
             btn = Button(text=i,size_hint_y=None,)
             btn.bind(on_release = lambda btn:self.select(btn.text))
             self.dropdown.add_widget(btn)
        mainbutton = Button(text ='Select Team', size_hint =(None,None),pos_hint={'x':0,'y':0.7}) 
        mainbutton.bind(on_release=self.dropdown.open) 
        self.dropdown.bind(on_select=lambda instance,x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)
    def safe(self,t):
        try:
         self.a.close()
        except:
            pass
        self.manager.current=t
class DelScreen(Screen):
    def ini(self):
        self.a=open('teams.pickle','rb')
        self.c=pickle.load(self.a)
        self.dropdown=DropDown() 
        for i in self.c:
             btn = Button(text=i,size_hint_y=None,)
             btn.bind(on_release = lambda btn:self.det(btn.text))
             self.dropdown.add_widget(btn)
        mainbutton = Button(text ='Select Team', size_hint =(None,None),pos_hint={'x':0,'y':0.7}) 
        mainbutton.bind(on_release=self.dropdown.open) 
        self.dropdown.bind(on_select=lambda instance,x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)
    def det(self,team):
        self.l1.text=' '
        self.dropdown.select(team)
        btn=Button(text ='Submit', size_hint =(None,None),pos_hint={'x':.5,'y':0.5})
        btn.bind(on_release=lambda x:self.det1(team))
        self.add_widget(btn)
    def det1(self,team):
        del self.c[team]
        b=open('teams1.pickle','wb')
        pickle.dump(self.c,b)
        self.a.close()
        b.close()
        os.remove('teams.pickle')
        os.rename('teams1.pickle','teams.pickle')
        self.l1.text='Deleted Team '+team+' Successfully'
        self.ini()
    def safe(self,t):
        try:
         self.a.close()
        except:
            pass
        self.manager.current=t
class AddScreen(Screen):
    def ini(self):
        self.l=TextInput(text='Enter Team Name',size_hint=(1,.06),pos_hint={'x':0,'y':.56},multiline=False)
        self.btn=Button(text ='Submit', size_hint =(None,None),pos_hint={'x':.5,'y':0.3})
        self.btn.bind(on_release=lambda x:self.addt())
        self.add_widget(self.l)
        self.add_widget(self.btn)
    def addt(self):
        global c
        c=0
        self.l1.text=' '
        self.team=self.l.text
        self.t=[]*10
        self.l.text='Enter name of player '+str(c+1)
        self.remove_widget(self.btn)
        self.btn1=Button(text ='Submit', size_hint =(None,None),pos_hint={'x':.5,'y':0.3})
        self.btn1.bind(on_release=lambda x:self.addt1())
        self.add_widget(self.btn1)
        c+=1
    def addt1(self):
        global c
        if c==0:
            self.t.append(self.l.text)
            c+=1
        elif c<10:
          self.t.append(self.l.text)  
          self.l.text='Enter name of player '+str(c+1)
          c+=1
        else:
            a=open('teams.pickle','rb')
            b=open('teams1.pickle','wb')
            c=pickle.load(a)
            c[self.team]=self.t
            pickle.dump(c,b)
            a.close()
            b.close()
            os.remove('teams.pickle')
            os.rename('teams1.pickle','teams.pickle')
            self.l1.text='Added Team '+self.team+' Succesfully'
            self.ini()
r=Builder.load_file("crick.kv")
class crickApp(App):
    def build(self):
        return r
crickApp().run()
