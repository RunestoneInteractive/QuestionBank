.. mchoice:: cswt01_q24a
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :answer_a: Prints the sum of all the even integers between 2 and 10 (including 10)
   :answer_b: Prints the sum of all the integers between 2 and 10 (including 10)
   :answer_c: Prints the sum of all the integers between 2 and 11 (including 11)
   :answer_d: Prints the sum of all the even integers between 2 and 12 (including 12)
   :correct: a
   :random: 
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.5

   24. What does the following code do?::
   
      def sum_nums(n):
          for i in range(2, n, 2):
              total += i
          return total
   
      def main():
          x = sum_nums(12)
          print(x)
   
      main()