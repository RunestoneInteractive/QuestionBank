.. parsonsprob:: m2-student-top-grades
   :author: Kathryn Cunningham
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 21
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 42.5

   Solve my really cool parsons problem...if you can.
   -----
   def first_student(data):
   =====
   adesDict = {}
   =====
   adesDict = [] #distractor
   =====
   r student in data:
   =====
    	total = student['grades’]
   =====
    	average = total / 5
   =====
    	average = total % 5
   =====
        gradesDict[student['name’]] = average
   ===== 
   adesList = sorted(marksDict.items(), key = lambda tup:tup[1], reverse = True)
   =====
   adesList = sorted(marksDict.items(), key = lambda tup:tup[0], reverse = True)
   =====
   p = gradesList[0]
   =====
   turn top[0]