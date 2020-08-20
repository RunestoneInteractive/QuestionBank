.. mchoice:: question10_3_3
   :author: bmiller
   :difficulty: 2.4445294568
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: T
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: 23 is a value in the dictionary, not a key.
   :feedback_b: Yes, the in operator returns True if a key is in the dictionary, False otherwise.
   :practice: T
   :pct_on_first: 0.6388676358
   :total_students_attempting: 1307
   :num_students_correct: 1294.0
   :mean_clicks_to_correct: 1.3663060278

   What is printed by the following statements?
   
   .. sourcecode:: python
   
      mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
      print(23 in mydict)