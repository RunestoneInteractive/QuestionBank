.. activecode:: madlib_function
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPStringPieces
   :subchapter: strProcParam
   :topics: CSPStringPieces/strProcParam
   :from_source: T
   :tour_1: "Structural tour"; 1: Stf1-line1; 4: Stf1-line2; 5: Stf1-line3; 6: Stf1-line4; 7: Stf1-line5; 8: Stf1-line6; 11-15: Stf1-line7-11; 18: Stf1-line13;

   def witchStory (firstName, lastName, gender, address, verb):

       # create the story
       start = "Once there was a " + gender + " named " + firstName + "."
       next1 = "A good " + gender + " living at " + address + "."
       next2 = "One day, a wicked witch came to the " + lastName + " house."
       next3 = "The wicked witch was planning to " + verb + " " + firstName + "!"
       ending = "But " + firstName + " was smart and avoided the wicked witch."

       # print the story
       print(start)
       print(next1)
       print(next2)
       print(next3)
       print(ending)

   # call the procedure
   witchStory("Abe", "Brown", "boy", "1313 Maple Lane", "trick")