.. mchoice:: question10_3_4
   :author: bmiller
   :difficulty: 2.5478927203
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: T
   :answer_a: 18
   :answer_b: 43
   :answer_c: 0
   :answer_d: 61
   :correct: b
   :feedback_a: Add the values that have keys longer than 3 characters, not those with exactly 3 characters.
   :feedback_b: Yes, the for statement iterates over the keys. It adds the values of the keys that have length greater than 3.
   :feedback_c: This is the accumulator pattern. Total starts at 0 but then changes as the iteration proceeds.
   :feedback_d: Not all the values are added together. The if statement only chooses some of them.
   :practice: T
   :pct_on_first: 0.6130268199
   :total_students_attempting: 1305
   :num_students_correct: 1288.0
   :mean_clicks_to_correct: 1.5473602484

   What is printed by the following statements?
   
   .. sourcecode:: python
   
      total = 0
      mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
      for akey in mydict:
         if len(akey) > 3:
            total = total + mydict[akey]
      print(total)