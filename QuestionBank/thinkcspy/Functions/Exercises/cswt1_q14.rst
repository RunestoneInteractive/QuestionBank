.. mchoice:: cswt1_q14
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :answer_a: 3 6 9
   :answer_b: 8 16 29
   :answer_c: 11 22 38
   :answer_d: Impossible to tell without running the program
   :correct: a
   :random: 
   :pct_on_first: 0.1739130435
   :total_students_attempting: 23
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 1.9565217391

   What does the following code print?::
   
      def function1(a, b, c) :
          a = a + 5
          b = b + 10
          c = c + 20
   
      def main() :
          a = 3
          b = 6
          c = 9
          function1(a, b, c)
          print(a, b, c)
   
      main()