.. mchoice:: question19_3_3
   :author: bmiller
   :difficulty: 1.8161209068
   :basecourse: fopp
   :chapter: Classes
   :subchapter: TestingClasses
   :topics: Classes/TestingClasses
   :from_source: T
   :practice: T
   :answer_a: return value test
   :answer_b: side effect test
   :correct: a
   :feedback_a: You want to check if maxabs returns the correct value for some input.
   :feedback_b: The function has no side effects; even though it takes a list L as a parameter, it doesn't alter its contents.
   :pct_on_first: 0.7959697733
   :total_students_attempting: 397
   :num_students_correct: 394.0
   :mean_clicks_to_correct: 1.2106598985

   To test the function maxabs, which kind of test case should you write?
   
   .. sourcecode:: python
   
      def maxabs(L):
         """L should be a list of numbers (ints or floats). The return value should be the maximum absolute value of the numbers in L."""
         return max(L, key=abs)