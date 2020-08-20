.. mchoice:: 4_4_2_Story2_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameStrings
   :subchapter: madlib
   :topics: CSPNameStrings/madlib
   :from_source: T
   :answer_a: Yes
   :answer_b: No
   :correct: a
   :feedback_a: The only thing that is different is when the lines are printed, but the lines are the same.
   :feedback_b: Did you try it?  Copy the code into the program area above and run it.

   Would the following code print the same story as shown above?

   ::

     firstName = "Sofia"
     lastName = "Diaz"
     gender = "girl"
     address = "1600 Pennsylvania Avenue"
     verb = "burp at"
     start = "Once there was a " + gender + " named " + firstName + "."
     print(start)
     next1 = "A good " + gender + " living at " + address + "."
     print(next1)
     next2 = "One day, a wicked witch came to the " + lastName + " house."
     print(next2)
     next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
     print(next3)
     ending = "But " + firstName + " was smart and avoided the wicked witch."
     print(ending)