.. parsonsprob:: pab_3
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program has the correct code to reverse the elements in an array, a,  but the code is mixed up.  Drag the blocks from the left into the correct order on the right. You will be told if any of the blocks are in the wrong order.</p>
   -----
   public static void reverse(int[] a)
   {
   =====
     int temp = 0;
     int half = a.length / 2;
     int max = a.length - 1;
   =====
     for (int i = 0; i < half; i++)
     {
   =====
        temp = a[i];
   =====
        a[i] = a[max - i];
   =====
        a[max - i] = temp;
   =====
     } // end for
   =====
   } // end method