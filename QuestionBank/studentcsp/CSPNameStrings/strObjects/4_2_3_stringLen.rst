.. mchoice:: 4_2_3_stringLen
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPNameStrings
   :subchapter: strObjects
   :topics: CSPNameStrings/strObjects
   :from_source: T
   :practice: T
   :answer_a: 13
   :answer_b: 15
   :answer_c: 10
   :correct: b
   :feedback_a: Don't forget to include the spaces in the count.
   :feedback_b: The len function returns the number of elements in the string including spaces.
   :feedback_c: This would be true if the len function only returned the number of alphabetic characters, but it includes all including spaces.


   Given the following code segment, what will be printed?

   ::

     street = "125 Main Street"
     print(len(street))