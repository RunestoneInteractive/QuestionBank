.. mchoice:: question15_4_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter15
   :subchapter: File_output
   :topics: Chapter15/File_output
   :from_source: T
   :answer_a: Create two "for" loops instead of an if-statement so that the statement loops through both conditions once.
   :answer_b: Create a "while" loop instead of an if-statement so that the statement loops through both conditions separately until the body of the loop is reached.
   :answer_c: Create two "if" statements, one that check whether in_file.good() is false, and another that checks whether out_file.good() is false, instead of putting them together in one "if" statement.
   :correct: c
   :feedback_a: Try again!
   :feedback_b: Try again!
   :feedback_c: Correct!

   The code from the previous problem checks whether the files open or not. It doesn't specify which one, if any, doesn't open. How could you specify which file does not open?