.. mchoice:: mc8f1
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: Length
   :topics: Strings/Length
   :from_source: None
   :answer_a: c
   :answer_b: k
   :answer_c: s
   :answer_d: Error, negative indices are illegal.
   :correct: a
   :feedback_a: Yes, 3 characters from the end.
   :feedback_b: Count backward 3 characters.
   :feedback_c: When expressed with a negative index the last character s is at index -1.
   :feedback_d: Python does use negative indices to count backward from the end.


   What is printed by the following statements?

   .. code-block:: python

      s = "python rocks"
      print(s[-3])