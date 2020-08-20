.. mchoice:: pre_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPrinTeasers
   :subchapter: pretest
   :topics: CSPrinTeasers/pretest
   :from_source: T
   :answer_a: Normal
   :answer_b: Hypertensive Crisis
   :answer_c: High Blood Pressure A
   :answer_d: Prehypertension
   :answer_e: I don’t know
   :correct: c
   :feedback_a: This will only print when both check_systolic and check_diastolic return 0 which is when check_systolic is passed a number less than 120 and check_diastolic is passed a number less than 80.
   :feedback_b: This will only print when either check_systolic or check_diastolic return 3 which is when check_systolic is passed a number greater or equal to 180 and check_diastolic is passed a number greater than or equal to 110.
   :feedback_c: This will print when check_systolic was 1 and check_diastolic was greater than 1 (but not 3).
   :feedback_d: This will print when check_systolic was 1 and check_diastolic was less than or equal to 1.
   :feedback_e: That is okay.  We do not expect you to know this.

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