.. mchoice:: mc9r
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Lists
   :subchapter: Listsandforloops2
   :topics: Lists/Listsandforloops2
   :from_source: None
   :answer_a: Error, i is an integer and does not understand the upper method.
   :answer_b: Error, upper is not a list method - it is a string method.
   :answer_c: ["APPLE", "ORANGE", "BANANA", "CHERRY"]
   :correct: c
   :feedback_a: i is used as an index into the list.
   :feedback_b: upper is used on a list element, not on the list.
   :feedback_c: Yes, the for loop processes each item of the list making an upper case string and reassigning it to the same location in the list.

   What is printed by the following statements?

   .. code-block:: python

     fruits = ["apple", "orange", "banana", "cherry"]
     for i in range(len(fruits)):
         fruits[i] = fruits[i].upper()
     print(fruits)