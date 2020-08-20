.. parsonsprob:: ch12ex6muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :noindent:
   :adaptive:

   The following method should return the number of times "5" is an element in the passed-in array -- so {1, 5, 7, 14, 5} will return 2 (Note that when the method is called the index will always start off as 0).  But the blocks have been mixed up and include <b>two extra blocks</b> that are not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static int numFiveOccurrence(int[] arr, int index)
   {
   =====
       if (index >= arr.length)
       {
   =====
       if (index <= arr.length) #distractor
       {
   =====
           return 0;
   =====
       } //end if
       else
       {
   =====
           if (arr[index] == 5)
           {
               return numFiveOccurrence(arr, index + 1) + 1;
           }
   =====
           return numFiveOccurrence(arr, index + 1);
   =====
           return numFiveOccurrence(arr, index); #distractor
   =====
       } //end else
   } //end method