.. parsonsprob:: midtermStudentClassDict
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive:
   :numbered: left

   Fix the code to return a dictionary of the class names, like "Freshman" or "Senior" and the number of people in each class.  The input is a list of dictionaries where each dictionary represents a single student.  
   -----
   def classSizes(data):
   =====
       classDict = dict()
   =====
       for studentDict in data:
   =====
           theClass = studentDict['Class']
   =====
           classDict[theClass] = classDict.get(theClass,0) + 1
   =====
          classDict[theClass] = classDict[theClass]  + 1 #distractor
   =====
        return classDict

config values (conf.py):

- parsons_div_class - custom CSS class of the component's outermost div