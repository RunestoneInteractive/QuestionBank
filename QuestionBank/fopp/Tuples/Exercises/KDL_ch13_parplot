.. activecode:: KDL_ch13_parplot
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Tuples
   :subchapter: Exercises
   :topics: Tuples/Exercises
   :from_source: F
   :language: python

   Parametric plotting time.

   ~~~~
   def create_t(start,stop,step):
       r=int((stop-start)//step)
       t=start
       tlist=[start]
       for _ in range(r):
           t=t+step
           tlist+=[t]
       return tlist
   def circle(r,tlist):
       import math
       x=[]
       y=[]
       for t in tlist:
           x+=[r*math.cos(t)]
           y+=[r*math.sin(t)]
       return x,y
   def cool_thing(a,b,tlist):
       import math
       x=[]
       y=[]
       for t in tlist:
           x+=[-a*math.cos(t)+b*math.cos(-a/10*t)]
           y+=[-a*math.sin(t)-b*math.sin(-a/10*t)]
       return x,y
   def slinky_circle(a,b,c,tlist):
       import math
       x=[]
       y=[]
       for t in tlist:
           x+=[(b+a*math.sin(c*t))*math.cos(t)]
           y+=[(b+a*math.sin(c*t))*math.sin(t)]
       return x,y
   import turtle
   wn=turtle.Screen()
   wn.setworldcoordinates(-10,-10,10,10)
   def plot_line(xlist,ylist):
       ted=turtle.Turtle()
       ted.tracer(100,25)
       ted.up()
       ted.goto(xlist[0],ylist[0])
       ted.down()
       for i,x in enumerate(xlist):
           ted.goto(x,ylist[i])
       ted.update()
   #plot_line(*circle(3,create_t(0,2.1*3.14,0.1)))
   #plot_line(*cool_thing(3.5,6.5,create_t(0,40*3.2,0.01)))
   #plot_line(*slinky_circle(2,8,20,create_t(0,2*3.2,0.01)))

   ====