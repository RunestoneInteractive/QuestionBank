.. parsonsprob:: 9_largest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day1
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day1
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.3794796269
   :total_students_attempting: 2037
   :num_students_correct: 1839.0
   :mean_clicks_to_correct: 3.9592169657

   The following has the correct code to find the largest value in a 2D array. Drag the blocks from the left into the correct order on the right and indent them as well. Check your solution by clicking on the <i>Check Me</i> button.  You will be told if any of the blocks are in the wrong order or have the wrong indention.
   -----
   public static int getLargest(int[][] arr)  {
   =====
    int largest = arr[0][0];
    int current = 0;
    for (int r = 0; r < arr.length; r++)  {
    =====
      for (int c = 0; c < arr[0].length; c++)  {
    =====
        current = arr[r][c];
        if (current > largest)  {
    =====
          largest = current;
    =====
        } // end if
    =====
      } // end column loop
    =====
    } // end row loop
    return largest;
   =====
   } // end method