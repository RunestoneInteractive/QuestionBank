.. mchoice:: qsm_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: Data Set 2 contains one string which should return true and one that should return false.
   :answer_b: All strings in Data Set 2 have the same number of characters.
   :answer_c: The strings in Data Set 2 are all lowercase
   :answer_d: Data Set 2 contains fewer values than Data Set 1.
   :answer_e: There are no advantages.
   :correct: a
   :feedback_a: All of the strings in Data Set 1 should return true, so the false condition is never tested.
   :feedback_b: Variety is always good in testing, so this is not an advantage.
   :feedback_c: It would be better to include both upper and lower case for testing, so this is not an advantage.
   :feedback_d: More test conditions is usually better, so this is not an advantage.
   :feedback_e: All the values in Data Set 1 are true, so the false condition is not tested.
   :pct_on_first: 0.3810858144
   :total_students_attempting: 2855
   :num_students_correct: 2815.0
   :mean_clicks_to_correct: 2.8373001776

   There is a method called checkString that determines whether a string is the same forwards and backwards. The following data set inputs can be used for testing the method. What advantage does Data Set 2 have over Data Set 1?
   
   .. code-block:: java
   
      Data Set 1    Data Set 2
      aba               bcb
      abba              bcd
      aBa