.. mchoice:: mc11h
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: None
   :answer_a: 18
   :answer_b: 43
   :answer_c: 0
   :answer_d: 61
   :correct: b
   :feedback_a: Add the values that have keys greater than 3, not equal to 3.
   :feedback_b: Yes, the for statement iterates over the keys.  It adds the values of the keys that have length greater than 3.
   :feedback_c: This is the accumulator pattern.  total starts at 0 but then changes as the iteration proceeds.
   :feedback_d: Not all the values are added together.  The if statement only chooses some of them.


   What is printed by the following statements?

   .. sourcecode:: python

      total = 0
      mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
      for akey in mydict:
         if len(akey) > 3:
            total = total + mydict[akey]
      print(total)