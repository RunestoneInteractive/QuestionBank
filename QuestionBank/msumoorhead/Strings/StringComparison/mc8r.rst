.. mchoice:: mc8r
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: StringComparison
   :topics: Strings/StringComparison
   :from_source: None
   :answer_a: True
   :answer_b: False
   :answer_c: They are the same word
   :correct: b
   :feedback_a: d is greater than D according to the ord function (68 versus 100).
   :feedback_b: Yes, upper case is less than lower case according to the ordinal values of the characters.
   :feedback_c: Python is case sensitive meaning that upper case and lower case characters are different.

   Evaluate the following comparison:

   .. code-block:: python

      "dog" < "Dog"