.. mchoice:: mc8m
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: StringMethods
   :topics: Strings/StringMethods
   :from_source: None
   :answer_a: 0
   :answer_b: 2
   :answer_c: 3
   :correct: c
   :feedback_a: There are definitely o and p characters.
   :feedback_b: There are 2 o characters but what about p?
   :feedback_c: Yes, add the number of o characters and the number of p characters.


   What is printed by the following statements?

   .. code-block:: python

      s = "python rocks"
      print(s.count("o") + s.count("p"))