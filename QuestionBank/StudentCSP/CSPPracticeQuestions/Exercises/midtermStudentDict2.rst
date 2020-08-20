.. parsonsprob:: midtermStudentDict2
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 37
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 9.9166666667

   Fix the mixed up code to return a list of dictionary objects where each dictionary object represents one line from the data file.  The first line of the data file is the field names.  Use these as the keys for the dictionary.  The data is in a csv file.  
   -----
   def getData(file):
   =====
       students = []
       inFile = open(file,"r")
   =====
       lineList = inFile.readlines()
   =====
       line = lineList[0]
   ===== 
       # get the list of keys to use
       keyList = line.split(",")
   =====
       for index in range(1,len(lineList)):
   =====
           line = lineList[index]
           studentDict = dict() 
           valueList = line.split(",") 
   =====
           for index in range(len(valueList)): 
   =====
               key = keyList[index]
               studentDict[key] = valueList[index]
               students.append(studentDict)
   =====
        inFile.close()
   turn students
   
   fig values (conf.py):
   
   arsons_div_class - custom CSS class of the component's outermost div