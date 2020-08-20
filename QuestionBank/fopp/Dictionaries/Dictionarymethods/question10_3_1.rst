.. mchoice:: question10_3_1
   :author: bmiller
   :difficulty: 1.6490566038
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: T
   :answer_a: 2
   :answer_b: 0.5
   :answer_c: bear
   :answer_d: Error, divide is not a valid operation on dictionaries.
   :correct: a
   :feedback_a: get returns the value associated with a given key so this divides 12 by 6.
   :feedback_b: 12 is divided by 6, not the other way around.
   :feedback_c: Take another look at the example for get above.  get returns the value associated with a given key.
   :feedback_d: The integer division operator is being used on the values returned from the get method, not on the dictionary.
   :pct_on_first: 0.8377358491
   :total_students_attempting: 1325
   :num_students_correct: 1306.0
   :mean_clicks_to_correct: 1.251914242

   What is printed by the following statements?
   
   .. sourcecode:: python
   
     mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
     answer = mydict.get("cat")//mydict.get("dog")
     print(answer)