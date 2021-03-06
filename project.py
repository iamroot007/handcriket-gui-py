import random
import pickle
import subprocess
from os import system, name
import msvcrt
class Luck:
    def __init__(self):
        self.n=0
        self.g=0
        self.l=0
        self.d=0
    def enter(self):
        while True:
            try:
              self.n=int(raw_input("enter any number:"))
              break
            except :
                print"enter the number only:"
    def test(self):
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
    def output(self):
        print"your number=",self.n
        print"random chossen number=",self.g
        print"Difference b\w number=",self.d
        print"Luck percentage[%]=",self.l
class cricket:
    def __init__(self):
        self.runs=0
        self.balls=0
        self.us=0
        self.cs=0
        self.ban=""
        self.bn=""
    def batting(self,o,l,l1,t1,t2):
        k=0
        o1=o*6
        i=0
        if self.cs==0:
          self.bn=random.choice(l1)
          self.batn=l[0]  
          while i<o1:
            if i!=0 and i%6==0:
                self.bn=random.choice(l1)
            print"Batman's Name =",self.batn
            print t1,"batting score=",self.us
            print"overs=",i/6,"balls",i%6
            print"wickets=",k
            print"Bowler's Name=",self.bn
            if k==10:
                break
            try:
               g=random.randint(0,6) 
               g=int(raw_input("enter the runs:"))
            except:
                 print"wrong"
            h=random.randint(0,6)
            if g==h:
                k+=1
                i+=1
                print self.batn ,"is out"
                self.batn=l[k]
            elif g not in range(7):
                print"Not proper range"
            elif g==0 or h==0:
                print"NO ball"
                if g==0:
                   self.us+=h
                elif h==0:
                    self.us+=g        
            else:
                i+=1
                self.us+=g
            cls()    
          print"END OF 1st Innings"
        else:
            self.bn=random.choice(l1)
            self.batn=l[0]
            while i<o1:
             if self.us>self.cs:
                print t1,"wins the macth"
                break   
             print"Batman's Name =",self.batn
             print t1," batting score=",self.us
             print t2," batting score=",self.cs
             print"wickets=",k
             print"overs=",i/6,"balls",i%6
             print"Bowler's Name=",self.bn
             print"required runs",(self.cs-self.us)+1
             if i!=0 and i%6==0:
                self.bn=random.choice(l)
             if k==10:
                print t2,"wins the macth" 
                break
             g=int(raw_input("enter the runs:"))
             h=random.randint(0,6)
             if g==h:
                k+=1
                i+=1
                print self.batn ,"is out"
                self.batn=l[k]
             elif g not in range(7):
                print"Not proper range"
             elif g==0 or h==0:
                print"No ball" 
                if g==0:
                   self.us+=h
                elif h==0:
                    self.us+=g
             else:
                i+=1
                self.us+=g
             cls()
            if self.cs>self.us:
                print t2,"wins the macth"
            print"END OF 2st Innings"
    def bowling(self,o,l,l1,t1,t2):
        k=0
        o1=o*6
        i=0
        if self.us==0:
          self.bn=random.choice(l1)
          self.batn=l[0]  
          while i<o1:
            if i!=0 and i%6==0:
                self.bn=random.choice(l1)
            print"Batman's Name =",self.batn
            print"wickets=",k
            print t2,"batting score=",self.cs
            print"overs=",i/6,"balls",i%6
            print"Bowler's Name=",self.bn
            if k==10:
                print t1,"wins the macth"
                break
            g=int(raw_input("enter the runs:"))
            h=random.randint(0,6)
            if g==h:
                k+=1
                i+=1
                print self.batn ,"is out"
                self.batn=l[k]
            elif g not in range(7):
                print"Not proper range"
            elif g==0 or h==0:
                print"No ball"
                if g==0:
                   self.cs+=h
                elif h==0:
                    self.cs+=g
            else:
                i+=1
                self.cs+=h
            cls()
          print"END OF 1st Innings"
        else:
          self.bn=random.choice(l1)
          self.batn=l[0]  
          while i<o1:
             if self.us<self.cs:
                print t2,"wins the macth"
                break 
             print"Batman's Name =",self.batn
             print"overs=",i/6,"balls",i%6
             print"wickets=",k
             print"Bowler's Name=",self.bn
             print t1,"batting score=",self.us
             print t2," batting score=",self.cs
             print"required runs=",(self.us-self.cs)+1
             if i!=0 and i%6==0:
                self.bn=random.choice(l)
             if k==10:
                break
             g=int(raw_input("enter the runs:"))
             h=random.randint(0,6)
             if g==h:
                k+=1
                i+=1
                print self.batn ,"is out"
                self.batn=l[k]
             elif g not in range(7):
                print"Not proper range"
             elif g==0 or h==0:
                print"NO ball" 
                if g==0:
                   self.cs+=h
                elif h==0:
                    self.cs+=g
             else:
                i+=1
                self.cs+=h
             cls()   
          if self.cs<self.us:
                print t1,"wins the macth"
          print"END OF 2nd Innings"
    
    def winner(self):
            if self.us>self.cs:
               return  True
            else:
                return False

def LeaderBoard(c3):
    print"Name","\t","wins","\t","loss","\t","macth played"
    for a in c3:
         z11=c3[a][0]
         z13=c3[a][1]
         print"---------------------------------------------------"
         print a,"\t",z11,"\t",z13-z11,"\t",z13
while True:
     print"WELCOME TO GAME OF NUMBER CRICKET"
     print"It's a computer version of Hand Cricker"
     print"""1.play
2.edit
3.Leaderboard
4.exit"""
     a=int(raw_input("enter your choice:"))
     if a==1:
       a111=raw_input("enter your Name:")  
       while True:   
        a11=raw_input("Want to test your luck[e to exit luck tester]:")
        a1=a11.capitalize()
        if a1=="Y"or a1=="Yes":
           l12=Luck()
           l12.enter()
           l12.test()
           l12.output()
        if a1=="E":
            break
       e=raw_input("Want instructions of the game [Y,Yes]:")
       w1=e.capitalize()
       if w1 =="Y"or w1=="Yes":
           print"""1.you have to enter run from 1-6
2.if your run macthes with comp. run then your are out and vice versa
3.0 means no ball and your are given runs given by computer"""
       b=open("teams.txt","a+")
       c2=open("games.txt","a+")
       c4=open("games1.txt","a+")
       c3=pickle.load(c2)
       if a111 in c3:
        z11=c3[a111][0]
        z13=c3[a111][1]
       c=pickle.load(b)
       c1=c.keys()
       print "teams are "
       for z in c1:
           print z
       while True:
                d1=raw_input("enter your team name:")
                d=d1.capitalize()
                if d in c1:
                    break
                else:
                    print d,"Team doesn't exist"
       l11=c[d]        
       while True:
            f=random.choice(c1)
            if d!=f:
                l12=c[f]
                break
       print"Macth is b\w ",d,"and",f
       o=int(raw_input("enter no. of overs:"))
       m=" "
       while m not in["H","T"]:
           m1=raw_input("HEAD or TAIL [H,T]:")
           m=m1.capitalize()
       p=["H","T"]
       n=random.choice(p)
       if m==n:
            print d,"won the toss"
            r=" "
            while r not in ['Bat','Bowl']:
             r1=raw_input("enter your choice Batting or bowling[bat or bowl]:")
             r=r1.capitalize()
            if r=="Bat":
                c1=cricket()
                c1.batting(o,l11,l12,d,f)
                c1.bowling(o,l12,l11,d,f)
                if a111 in c3:
                   z1=c1.winner()
                   if z1 is True:
                    z11+=1 
                   z13+=1
                else:
                  z1=c1.winner()  
                  if z1 is True:
                    z11=1 
                  z13=1
                z14=[z11,z13]  
                c3[a111]=z14
                LeaderBoard(c3)
                pickle.dump(c3,c4)
                c2.close()
                os.remove("games.txt")
                c4.close()
                os.rename("games1.txt","games.txt")
            elif r=="Bowl":
                c1=cricket()
                c1.bowling(o,l12,l11,d,f)
                c1.batting(o,l11,l12,d,f)
                if a111 in c3:
                   z1=c1.winner()
                   if z1 is True:
                    z11+=1 
                   z13+=1
                else:
                  z1=c1.winner()  
                  if z1 is True:
                    z13=1
                    z14=[z11,z13]  
                    z11=1 
                c3[a111]=z14
                LeaderBoard(c3)
                pickle.dump(c3,c4)
                c2.close()
                c4.close()
                os.remove("games.txt")
                os.rename("games1.txt","games.txt")
       else:
            print f,"won the toss"
            r1=["batting","bowling"]
            r=random.choice(r1)
            print f,"choose to ",r
            if r=="batting":
                c1=cricket()
                c1.bowling(o,l12,l11,d,f)
                c1.batting(o,l11,l12,d,f)
                if a111 in c3:
                   z1=c1.winner()
                   if z1 is True:
                    z11+=1 
                   z13+=1
                else:
                  z1=c1.winner()  
                  if z1 is True:
                    z11=1 
                  z13=1
                z14=[z11,z13]  
                c3[a111]=z14
                LeaderBoard(c3)
                pickle.dump(c3,c4)
                c2.close()
                os.remove("games.txt")
                c4.close()
                os.rename("games1.txt","games.txt")
            elif r=="bowling":
                     c1=cricket()
                     c1.batting(o,l11,l12,d,f)
                     c1.bowling(o,l12,l11,d,f)
                     if a111 in c3:
                        z1=c1.winner()
                        if z1 is True:
                         z11+=1 
                         z13+=1
                     else:
                      z1=c1.winner()   
                      if z1 is True:
                       z11=1 
                      z13=1
                     z14=[z11,z13]  
                     c3[a111]=z14
                     LeaderBoard(c3)
                     pickle.dump(c3,c4)
                     c2.close()
                     os.remove("games.txt")
                     c4.close()
                     os.rename("games1.txt","games.txt")
     elif a==2:
       while True:
           b=open("teams.txt","a+")
           f1=open("teams1.txt","a+")
           c=pickle.load(b)
           b.close()
           print"""1.add teams
2.edit team player Name
3.remove team
4.exit"""
           d=int(raw_input("enter your choice:"))
           if d==1:
               e=raw_input("enter team Name:")
               while True:
                n=int(raw_input("enter no. of players:"))
                if n<11 or n>15:
                   print"min. no. of players =",11,"and max.players=",15
                else:
                    break
               l=[]*n
               for f in range(n):
                   g=raw_input("enter the name of player:")
                   l.append(g)
               c[e]=l
               i=pickle.dump(c,f1)
               os.remove("teams.txt")
               f1.close()
               os.rename("teams1.txt","teams.txt")
               print"successfully added"
           elif d==2:
               e=raw_input("enter team name:")
               f=c[e]
               for x in f:
                   print x
               h=raw_input("enter orginal name of player:")
               for g in range(len(f)):
                   if f[g]==h:
                       h1=raw_input("enter new name of player:")
                       f[g]=h1
                       c[e]=f
                       pickle.dump(c,f1)
                       os.remove("teams.txt")
                       f1.close()
                       os.rename("teams1.txt","teams.txt")
                       print"succesfully added"
                
                       
           elif d==3:
               e=raw_input("enter team Name:")
               del c[e]
               pickle.dump(c,f1)
               os.remove("teams.txt")
               f1.close()
               os.rename("teams1.txt","teams.txt")
               print"Deleted successfully"
           elif d==4:
               break
           else:
               print"wrong choice"
     elif a==3:
         a=open("games.txt","r")
         c3=pickle.load(a)
         LeaderBoard(c3)
     elif a==4:
        break
     else:
        print"wrong choice"


                   
   
               
                  
        
