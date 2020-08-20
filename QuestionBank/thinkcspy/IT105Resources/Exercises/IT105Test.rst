.. parsonsprob:: IT105Test
   :author: Tom Babbitt
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: IT105Resources
   :subchapter: Exercises
   :topics: IT105Resources/Exercises
   :from_source: F
   :maxdist: 2
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   You are tasked to write a function called ``findMax(aList)`` that iterates through a list and returns the maximum value.
   
   Ensure that the code is in the correct order.
   -----
   def findMax(aList):
   =====
      if len(aList) == 0:
         return None
   =====
      currentMax = aList[0]
   =====
      for item in aList:
   =====
      for item in currentMax:   #distractor  
   =====
         if item &gt; currentMax:
   =====
            currentMax = item
   =====
            currentMax = currentMax + 1 #distractor
   =====
      return currentMax