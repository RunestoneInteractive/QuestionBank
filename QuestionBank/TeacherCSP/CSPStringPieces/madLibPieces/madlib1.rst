.. activecode:: madlib1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPStringPieces
   :subchapter: madLibPieces
   :topics: CSPStringPieces/madLibPieces
   :from_source: T
   :tour_1: "Line by line tour"; 2: StEx-line1; 3: StEx-line2; 4: StEx-line3; 5: StEx-line4; 6: StEx-line5; 9: StEx-line6; 10: StEx-line7; 11: StEx-line8; 12: StEx-line9; 13: StEx-line10; 16: StEx-line11; 17: StEx-line12; 18: StEx-line13; 19: StEx-line14; 20: StEx-line15;
   :tour_2: "Structural tour"; 2-6: StEx-line1-5; 9-13: StEx-line6-10; 16-20: StEx-line11-15;

   # initialize the variables
   firstName = "Pat"
   lastName = "Smith"
   gender = "girl"
   address = "65 Elm Street"
   verb = "eat"

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
   print (next3)
   print(ending)