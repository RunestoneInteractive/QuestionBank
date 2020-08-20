.. parsonsprob:: ch7ex2muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: ArrayParsonsPractice
   :topics: ArrayBasics/ArrayParsonsPractice
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following program segment should fill an array with elements that count up from 0 to 50 by 5 (0, 5, 10, 15, 20...).  But the blocks have been mixed up.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   int[] arr = new int[11];
   =====
   for (int i = 0; i < 11; i++) {
   =====
       arr[i] = i * 5;
   =====
       System.out.println(arr[i]);
   =====
   }