.. parsonsprob:: ch17RandStr1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: MixedFreeResponse
   :subchapter: RandomStringChooserParsonsB
   :topics: MixedFreeResponse/RandomStringChooserParsonsB
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The code below will copy the strings from the array to a list in the constructor using a general for loop.  In ``getNext`` it will return "NONE" if the length of the list is 0.  Otherwise it till calculate a random index in the list and remove and return the string at that index. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
       public RandomLetterChooser (String str)
       {
   =====
           super(getSingleLetters(str));
   =====
           super(str); #paired
   =====
       } // end constructor