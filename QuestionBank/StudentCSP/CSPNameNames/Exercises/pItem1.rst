.. parsonsprob:: pItem1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.5501618123
   :total_students_attempting: 309
   :num_students_correct: 307.0
   :mean_clicks_to_correct: 1.9413680782

   Put the mixed up code in order to define an Item class.  Item objects have a name and a price.  Define the __init__ method first and then the __str__ method.  
   -----
   class Item:
   =====
   def class Item: #paired
   =====
       def __init__(self, price, name):
   =====
       def __init__(price, name): #paired
   =====
           self.price = price
           self.name = name
   =====
       def __str__(self):
   =====
       def str(self): #paired
   =====
           return self.name + " " + str(self.price)
   =====
           return self.name + " " + self.price #paired