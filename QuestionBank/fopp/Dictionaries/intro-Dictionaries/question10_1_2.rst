.. mchoice:: question10_1_2
   :author: bmiller
   :difficulty: 1.4157303371
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: intro-Dictionaries
   :topics: Dictionaries/intro-Dictionaries
   :from_source: T
   :answer_a: 12
   :answer_b: 6
   :answer_c: 23
   :answer_d: Error, you cannot use the index operator with a dictionary.
   :correct: b
   :feedback_a: 12 is associated with the key cat.
   :feedback_b: Yes, 6 is associated with the key dog.
   :feedback_c: 23 is associated with the key elephant.
   :feedback_d: The [ ] operator, when used with a dictionary, will look up a value based on its key.
   :practice: T
   :pct_on_first: 0.8960674157
   :total_students_attempting: 1424
   :num_students_correct: 1410.0
   :mean_clicks_to_correct: 1.1411347518

   What is printed by the following statements?
   
   .. sourcecode:: python
   
     mydict = {"cat":12, "dog":6, "elephant":23}
     print(mydict["dog"])