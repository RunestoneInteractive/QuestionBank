.. mchoice:: mc8u
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: TraversalandthewhileLoop
   :topics: Strings/TraversalandthewhileLoop
   :from_source: None
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :correct: a
   :feedback_a: Yes, idx goes through the odd numbers starting at 1.  o is at position 4 and 8.
   :feedback_b: o is at positions 4 and 8.  idx starts at 1, not 0.
   :feedback_c: There are 2 o characters but idx does not take on the correct index values.


   How many times is the letter o printed by the following statements?

   .. code-block:: python

      s = "python rocks"
      idx = 1
      while idx < len(s):
          print(s[idx])
          idx = idx + 2