.. activecode:: firstsplit
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPStringPieces
   :subchapter: split
   :topics: CSPStringPieces/split
   :from_source: T
   :tour_1: "Line by line tour"; 2: StP1-line1; 5: StP1-line2; 8: StP1-line3; 9: StP1-line4; 10: StP1-line5;

   # create the input
   input = "Pat,Smith,girl,65 Elm Street,eat"

   # split on the comma
   pieces = input.split(",")

   # print the values
   print(pieces)
   print("First name is:")
   print(pieces[0])