.. mchoice:: question10_3_3
   :author: bmiller
   :difficulty: 2.4434250765
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
   :pct_on_first: 0.6391437309
   :total_students_attempting: 1308
   :num_students_correct: 1295.0
   :mean_clicks_to_correct: 1.366023166

   What is printed by the following statements?
   
   .. sourcecode:: python
   
      mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
      print(23 in mydict)