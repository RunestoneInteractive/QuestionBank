.. parsonsprob:: ch7ex1muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: ArrayParsonsPractice
   :topics: Unit7-Arrays/ArrayParsonsPractice
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program segment should double each element in the array then print out the new value -- so (1,2,3,4,5) should become (2,4,6,8,10).  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   int[] arr = {1, 2, 3, 4, 5};
   =====
   for (int i = 0; i < arr.length; i++) {
   =====
       arr[i] = arr[i] * 2;
   =====
       System.out.println(arr[i]);
   =====
   }