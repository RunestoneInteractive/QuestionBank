.. parsonsprob:: ch7ex2muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: ArrayParsonsPractice
   :topics: Unit6-Arrays/ArrayParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.8407608696
   :total_students_attempting: 1840
   :num_students_correct: 1764.0
   :mean_clicks_to_correct: 1.2188208617

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