.. mchoice:: question10_2_1
   :author: bmiller
   :difficulty: 1.8550932568
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Dictionaryoperations
   :topics: Dictionaries/Dictionaryoperations
   :from_source: T
   :answer_a: 12
   :answer_b: 0
   :answer_c: 18
   :answer_d: Error, there is no entry with mouse as the key.
   :correct: c
   :feedback_a: 12 is associated with the key cat.
   :feedback_b: The key mouse will be associated with the sum of the two values.
   :feedback_c: Yes, add the value for cat and the value for dog (12 + 6) and create a new entry for mouse.
   :feedback_d: Since the new key is introduced on the left hand side of the assignment statement, a new key-value pair is added to the dictionary.
   :practice: T
   :pct_on_first: 0.7862266858
   :total_students_attempting: 1394
   :num_students_correct: 1381.0
   :mean_clicks_to_correct: 1.283852281

   What is printed by the following statements?
   
   .. sourcecode:: python
   
     mydict = {"cat":12, "dog":6, "elephant":23}
     mydict["mouse"] = mydict["cat"] + mydict["dog"]
     print(mydict["mouse"])