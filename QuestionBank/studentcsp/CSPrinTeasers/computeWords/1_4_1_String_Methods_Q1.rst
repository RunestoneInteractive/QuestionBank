.. mchoice:: 1_4_1_String_Methods_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPrinTeasers
   :subchapter: computeWords
   :topics: CSPrinTeasers/computeWords
   :from_source: T
   :answer_a: Hi There
   :answer_b: HiThere
   :answer_c: Hi There Hi There
   :answer_d: HiThereHiThere
   :answer_e: HiThere2
   :correct: d
   :feedback_a: When you add strings together you copy the second string right after the first, without any added space
   :feedback_b: Remember that * 2 repeats two copies of the same string
   :feedback_c: Adding strings together and repeating them doesn't add spaces between the strings
   :feedback_d: Strings are added together without adding any space and they are repeated without adding a space
   :feedback_e: The * 2 repeats the string two times

   What would the following code print?

   ::

      first = "Hi"
      next = "There"
      print ((first + next) * 2)