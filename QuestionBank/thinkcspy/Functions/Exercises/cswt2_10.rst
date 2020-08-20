.. mchoice:: cswt2_10
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :answer_a: COP Change: 1.38
   :answer_b: 76.41 Change: 1.38
   :answer_c: 76.41 Change: 1.84%
   :answer_d: COP Change: 1.84%
   :correct: a
   :random: 
   :pct_on_first: 0.9126213592
   :total_students_attempting: 103
   :num_students_correct: 103.0
   :mean_clicks_to_correct: 1.145631068

   10. What does the following code print? (The string holds stock market information for ConocoPhillips).::
   
      s = "COP, 76.41, 1.38, 1.84%, 4501203, 75.03"
      data_list = s.split(',')
      print(data_list[0], "Change:", data_list[2])