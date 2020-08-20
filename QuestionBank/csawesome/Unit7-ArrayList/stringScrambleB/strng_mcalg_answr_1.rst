.. mchoice:: strng_mcalg_answr_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: stringScrambleB
   :topics: Unit7-ArrayList/stringScrambleB
   :from_source: T
   :answer_a: (index != wordList.current())
   :answer_b: (int index = wordList.size() - 1; index >= 0; index--)
   :answer_c: (index < wordList.size())
   :answer_d: (wordList(index) != wordList.size())
   :correct: c
   :feedback_a: the .current() command does not exist
   :feedback_b: this form of range control does not work with while loops
   :feedback_c: Correct!
   :feedback_d: this does not accurately update the list as you iterate through wordList
   :pct_on_first: 1.0
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.0

   There are many ways to use loops to solve this problem. If we were to use a while loop, what conditional could we write to make sure the loop does not go out of bounds? (Assume an integer index has already been initialized).