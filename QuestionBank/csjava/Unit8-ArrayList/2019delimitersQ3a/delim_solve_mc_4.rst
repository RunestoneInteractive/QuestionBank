.. mchoice:: delim_solve_mc_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: 2019delimitersQ3a
   :topics: Unit8-ArrayList/2019delimitersQ3a
   :from_source: T
   :answer_a: if (token == openDel && token == closeDel)
   :answer_b: if (token == openDel || token == closeDel)
   :answer_c: if (token.equals(openDel) && token.equals(closeDel))
   :answer_d: if (token.equals(openDel) || token.equals(closeDel))
   :correct: d
   :feedback_a: You should use .equals with strings and || for or
   :feedback_b: You should use .equals with strings
   :feedback_c: You should use || for or not &&
   :feedback_d: This returns true when openDel or closeDel have the same characters as token
   :optional:

   Which code correctly checks if token is equal to (has the same characters as) openDel or closeDel?