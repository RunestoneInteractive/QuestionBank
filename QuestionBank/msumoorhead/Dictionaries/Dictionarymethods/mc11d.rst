.. mchoice:: mc11d
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: None
   :answer_a: cat
   :answer_b: dog
   :answer_c: elephant
   :answer_d: bear
   :correct: c
   :feedback_a: keylist is a list of all the keys which is then sorted.  cat would be at index 1.
   :feedback_b: keylist is a list of all the keys which is then sorted.  dog would be at index 2.
   :feedback_c: Yes, the list of keys is sorted and the item at index 3 is printed.
   :feedback_d: keylist is a list of all the keys which is then sorted.  bear would be at index 0.


   What is printed by the following statements?

   .. sourcecode:: python

     mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
     keylist = list(mydict.keys())
     keylist.sort()
     print(keylist[3])