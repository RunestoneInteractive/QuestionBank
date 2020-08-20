.. parsonsprob:: NumberCubeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: numberCubeA
   :topics: Unit7-Arrays/numberCubeA
   :from_source: T
   :numbered: left
   :adaptive:

   The method getCubeTosses below contains the correct code for one solution to this problem, but it is mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
   -----
   public static int[] getCubeTosses(NumberCube cube,
                                     int numTosses)
   {
   =====
       int[] cubeTosses = new int[numTosses];
   =====
       for (int i = 0; i < numTosses; i++)
       {
   =====
           cubeTosses[i] = cube.toss();
   =====
       } // end for
   =====
       return cubeTosses;
   =====
   } // end method