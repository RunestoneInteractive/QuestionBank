.. parsonsprob:: ch12ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rParsonsPractice
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :noindent: 
   :adaptive: 
   :pct_on_first: 0.5399568035
   :total_students_attempting: 463
   :num_students_correct: 440.0
   :mean_clicks_to_correct: 2.1477272727

   The following method should add up all of the elements in the passed-in array -- so {1,2,3,12} should return 18 (Note when the method is called, the index will always start off as 0).  But the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int sumElements(int[] arr, int index)
   {
   =====
       if (index >= arr.length)
       {
           return 0;
       } //end if
   =====
       if (index >= arr.length) #distractor
       {
           return 1;
       } //end if
   =====
       else
       {
   =====
           return sumElements(arr, index + 1) + arr[index];
   =====
           return sumElements(arr, index) + arr[index]; #distractor
   =====
       } //end else
   } //end method