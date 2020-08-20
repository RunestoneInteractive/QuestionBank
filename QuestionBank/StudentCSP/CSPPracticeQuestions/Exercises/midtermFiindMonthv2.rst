.. parsonsprob:: midtermFiindMonthv2
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.231292517
   :total_students_attempting: 147
   :num_students_correct: 133.0
   :mean_clicks_to_correct: 8.1578947368

   Put the mixed up code below in order to loop through a list of dictionaries of student data and create a dictionary of the birth month and the count of the number of students with that birth month.  The birthdate is in the format Month/Day/Year.  Return the month with the most student births.
   -----
   def findMonth(a):
   =====
       monthDict = {}
   =====
       for studentDict in a:
   =====
           date = studentDict['DOB']
   =====
           valList = date.split("/")
   =====
           theMonth = valList[0]
   =====
           theMonth = valList[1] #distractor
   =====
           monthDict[theMonth] = monthDict.get(theMonth,0) + 1
   =====
       monthList = sorted(monthDict.items(), key = lambda tup: tup[1], reverse = True)
   =====
       monthList = sorted(monthDict.items(), key = lambda tup: tup[1]) #distractor
   =====
       first = monthList[0]
   =====
       return int(first[0])
   =====
       return int(first[1]) #distractor
   
   fig values (conf.py):
   
   arsons_div_class - custom CSS class of the component's outermost div