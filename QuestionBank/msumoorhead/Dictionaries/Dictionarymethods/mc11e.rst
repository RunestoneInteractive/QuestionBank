.. mchoice:: mc11e
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: None
   :answer_a: 2
   :answer_b: 0.5
   :answer_c: bear
   :answer_d: Error, divide is not a valid operation on dictionaries.
   :correct: a
   :feedback_a: get returns the value associated with a given key so this divides 12 by 6.
   :feedback_b: 12 is divided by 6, not the other way around.
   :feedback_c: Take another look at the example for get above.  get returns the value associated with a given key.
   :feedback_d: The integer division operator is being used on the values returned from the get method, not on the dictionary.


   What is printed by the following statements?

   .. sourcecode:: python

     mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
     answer = mydict.get("cat") // mydict.get("dog")
     print(answer)