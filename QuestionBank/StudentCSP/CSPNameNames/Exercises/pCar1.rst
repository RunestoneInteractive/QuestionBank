.. parsonsprob:: pCar1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.6480836237
   :total_students_attempting: 287
   :num_students_correct: 281.0
   :mean_clicks_to_correct: 1.8896797153

   Put the code below in order to define a Car class.  A car has a make and model.  Define a constructor (__init__), a method to return the attributes as a string (__str__), and a method, forward, that takes an integer, theSpeed, and returns "speed: " followed by the value of theSpeed.
   -----
   class Car:
   =====
       def __init__(self, make, model):
   =====
       def init(self, make, model): #paired
   =====
           self.make = make
           self.model = model
   =====
       def __str__(self):
   =====
           return("make: " + self.make + " model: " + self.model)
   =====
           return(make:  + self.make + " model: " + self.model) #paired
   =====
           
       def forward(self, theSpeed):
   =====
       def forward(theSpeed, self): #paired
   =====
           return("forward: " + str(theSpeed))
   =====
           return("forward: " + theSpeed) #paired