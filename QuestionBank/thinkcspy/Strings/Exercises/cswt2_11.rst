.. mchoice:: cswt2_11
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :answer_a: "2.52"
   :answer_b: "2.48"
   :answer_c: "3.62"
   :answer_d: "Feb"
   :correct: a
   :random: 
   :pct_on_first: 0.4141414141
   :total_students_attempting: 99
   :num_students_correct: 96.0
   :mean_clicks_to_correct: 2.125

   11. Assume the first two lines below represent data stored in a file named "avg_precipitation.csv". What is the value of x after executing the following code?::
   
      City,State,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
      Springfield,MO,2.48,2.52,3.62,4.33,5.12,4.84,3.66,3.54,4.61,3.58,4.21,3.03
      
      f = open("avg_precipitation.csv", 'r')
      lines = f.readlines()
      f.close()
      data = lines[1].strip().split(',')
      x = data[3]