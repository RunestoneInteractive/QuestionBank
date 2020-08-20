.. parsonsprob:: NumberCubeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: numberCubeA
   :topics: Unit6-Arrays/numberCubeA
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.427773344
   :total_students_attempting: 1253
   :num_students_correct: 1131.0
   :mean_clicks_to_correct: 2.7409372237

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