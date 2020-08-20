.. mchoice:: retention_1
       :author: Barbara  Ericson
       :difficulty: 4.0
       :basecourse: StudentCSP
       :chapter: CSPIntroDecisions
       :subchapter: Exercises
       :topics: CSPIntroDecisions/Exercises
       :from_source: F
       :answer_a: Normal
       :answer_b: Hypertensive Crisis
       :answer_c: High Blood Pressure A
       :answer_d: Prehypertension
       :answer_e: I don’t know
       :correct: c
       :feedback_a: Incorrect
       :feedback_b: Incorrect
       :feedback_c: This will print when check_systolic was 1 and check_diastolic was greater than 1 (but not 3).
       :feedback_d: This will print when check_systolic was 1 and check_diastolic was less than or equal to 1.
       :feedback_e: That is okay.
       :pct_on_first: 0.6627565982
       :total_students_attempting: 341
       :num_students_correct: 333.0
       :mean_clicks_to_correct: 1.4924924925

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