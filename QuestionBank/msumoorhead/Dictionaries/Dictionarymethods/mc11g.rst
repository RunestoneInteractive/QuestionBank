.. mchoice:: mc11g
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: None
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: 23 is a value in the dictionary, not a key.
   :feedback_b: Yes, the in operator returns True if a key is in the dictionary, False otherwise.

   What is printed by the following statements?

   .. sourcecode:: python

      mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
      print(23 in mydict)