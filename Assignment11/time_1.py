import datetime

class Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s

    def add (self,other):
        totalSecs1=0
        totalSecs2=0
        totalSecs1 += (self.hour*3600+ + self.minute * 60 + self.second)
        totalSecs2 += (other.hour*3600+ + other.minute * 60 + other.second)
        totalSecs3=totalSecs1+totalSecs2
        totalSecs3, sec = divmod(totalSecs3, 60)
        hr, min = divmod(totalSecs3, 60)
        print("The result obtained for Adding Time in Python: ")
        print ("%d:%02d:%02d" % (hr, min, sec))
    
    def sub(self,other):
        totalSecs1=0
        totalSecs2=0
        totalSecs1 += (self.hour*3600+ + self.minute * 60 + self.second)
        totalSecs2 += (other.hour*3600+ + other.minute * 60 + other.second)
        totalSecs3=abs(totalSecs1-totalSecs2)
        totalSecs3, sec = divmod(totalSecs3, 60)
        hr, min = divmod(totalSecs3, 60)
        print("The result obtained for Subtracting Time in Python: ")
        print ("%d:%02d:%02d" % (hr, min, sec))
        
    def timetoSecs(self):
        totalSecs=0
        totalSecs += (self.hour*3600+ + self.minute * 60 + self.second)
        print("The result obtained for Convert Time to Seconds in Python: ")
        print (totalSecs,"seconds")
        
    def secstoTime(self):
        totalSecs=self.second
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        print("The result obtained for Converting Seconds to Time in Python: ")
        print ("%d:%02d:%02d" % (hr, min, sec))
        
    def GMTtoIran(self):
        self.hour+=2
        self.minute+=30
        totalSecs=0
        totalSecs += (self.hour*3600+ + self.minute * 60 + self.second)
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        print("The result obtained for Converting GMT to IRAN in Python: ")
        print ("%d:%02d:%02d" % (hr, min, sec))
         
    
        
zaman1 = Time(4, 30, 30)
zaman2 = Time(2, 35, 30)
## for add , sub

zaman3=Time(0,0,2780)
## for converting seconds to hour,minute, seconds

zaman4=Time(7,33,35)
## for converting gmt to iranian's hour

zaman1.add(zaman2)
zaman1.sub(zaman2)
zaman1.timetoSecs()
zaman2.timetoSecs()
zaman3.secstoTime()
zaman4.GMTtoIran()

