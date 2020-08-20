.. parsonsprob:: ch7ex5muc
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
   :pct_on_first: 0.3144876325
   :total_students_attempting: 1698
   :num_students_correct: 1554.0
   :mean_clicks_to_correct: 3.3101673102

   The following program segment is a method that should return the average given an array of integers (the parameter).  But, the blocks have been mixed up and include <b>one extra block</b> that is not needed in a correct solution.  Drag the blocks from the left and put them in the correct order with the correct indentation on the right.  Click the <i>Check Me</i> button to check your solution. </p>
   -----
   public static double findAverage(int[] arr) {
   =====
       double sum = 0;
   =====
       int sum = 0; #distractor
   =====
       for (int i = 0; i < arr.length; i++) {
   =====
           sum += arr[i];
   =====
       } //end for loop
   =====
       return (sum / arr.length);
   =====
   } //end findAverage method