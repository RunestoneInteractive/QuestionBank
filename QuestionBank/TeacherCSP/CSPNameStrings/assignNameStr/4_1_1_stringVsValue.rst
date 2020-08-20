.. mchoice:: 4_1_1_stringVsValue
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameStrings
   :subchapter: assignNameStr
   :topics: CSPNameStrings/assignNameStr
   :from_source: T
   :answer_a: The address is street
   :answer_b: The address is 125 Main Street
   :answer_c: It won't execute
   :correct: a
   :feedback_a: Since street is in double quotes it will print the string street rather than the value of the variable street.
   :feedback_b: This would be true if it was print("The address is " + street)
   :feedback_c: While this isn't printing what we probably want it to, it will print something.


   Given the following code segment, what will be printed?

   ::

     street = "125 Main Street"
     print("The address is " + "street")