.. parsonsprob:: NumberCubeB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: numberCubeB
   :topics: Unit6-Arrays/numberCubeB
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.3006134969
   :total_students_attempting: 1141
   :num_students_correct: 1009.0
   :mean_clicks_to_correct: 3.2467789891

   The method getLongestRun below contains the correct code for one solution to this problem, but it is mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
   -----
   public static int getLongestRun(int[] values)
   {
       int currentLen = 0;
       int maxLen = 0;
       int maxStart = -1;
   =====
       for (int i = 0; i < values.length-1; i++)
       {
   =====
           if (values[i] == values[i+1])
           {
   =====
               currentLen++;
               if (currentLen > maxLen)
               {
                   maxLen = currentLen;
                   maxStart = i - currentLen + 1;
               }
   =====
           } else {
               currentLen = 0;
           }
   =====
       } // end for
       return maxStart;
   =====
   } // end method