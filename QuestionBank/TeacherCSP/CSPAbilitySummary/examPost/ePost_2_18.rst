.. mchoice:: ePost_2_18
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPAbilitySummary
   :subchapter: examPost
   :topics: CSPAbilitySummary/examPost
   :from_source: T
   :answer_a: Normal
   :answer_b: Hypertensive Crisis
   :answer_c: High Blood Pressure B
   :answer_d: Prehypertension
   :answer_e: High Blood Pressure A
   :correct: e
   :feedback_a: This would be true if check_systolic returned 0 and check_diastolic returned 0.
   :feedback_b: This would be true if check_systolic returned 3 or check_diastolic returned 3.
   :feedback_c: This would be true if check_systolic returned 2 and check_diastolic returned something other than 3.
   :feedback_d: This would be true if check_systolic returned 1 and check_diastolic returned 1.
   :feedback_e: The function check_systolic(135) returns 1 and the function check_diastolic(100) returns 2 so this will print "High Blood Pressure A"

   What is the output from the program below?

   ::

      def check_systolic(num1):
          if num1 < 120:
              return 0
          elif num1 < 140:
              return 1
          elif num1 < 180:
              return 2
          else:
              return 3

      def check_diastolic(num2):
          if num2 < 80:
              return 0
          elif num2 < 90:
              return 1
          elif num2 < 110:
              return 2
          else:
              return 3

      syst = 135
      dias = 100
      if check_systolic(syst) == 0 and check_diastolic(dias) == 0:
          print ("Normal")
      elif check_systolic(syst) == 3 or check_diastolic(dias) == 3:
          print ("Hypertensive Crisis")
      elif check_systolic(syst) == 1:
          if check_diastolic(dias) > 1:
              print ("High Blood Pressure A")
          else:
              print ("Prehypertension")
      else:
          print ("High Blood Pressure B")