.. mchoice:: question10_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: T
   :answer_a: True
   :answer_b: False
   :correct: a
   :feedback_a: Yes, dog is a key in the dictionary.
   :feedback_b: The in operator returns True if a key is in the dictionary, False otherwise.
   :practice: T
   :pct_on_first: 0.8983957219
   :total_students_attempting: 1309
   :num_students_correct: 1295.0
   :mean_clicks_to_correct: 1.0942084942

   What is printed by the following statements?
   
   .. sourcecode:: python
   
     mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
     print("dog" in mydict)