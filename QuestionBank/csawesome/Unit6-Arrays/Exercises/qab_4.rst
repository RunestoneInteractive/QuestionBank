.. mchoice:: qab_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: Exercises
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: All values in positions <i>m+1</i> through <i>myStuff.length-1</i> are greater than or equal to <i>n</i>.
   :answer_b: All values in position 0 through <i>m</i> are less than <i>n</i>.
   :answer_c: All values in position <i>m+1</i> through <i>myStuff.length-1</i> are less than <i>n</i>.
   :answer_d: The smallest value is at position <i>m</i>.
   :correct: a
   :feedback_a: Mystery steps backwards through the array until the first value less than the passed num (<i>n</i>) is found and then it returns the index where this value is found.
   :feedback_b: This would be true if mystery looped forward through the array and returned when it found a value greater than the passed num (<i>n</i>).
   :feedback_c: This would be true if it returned when it found a value at the current index that was greater than num (<i>n</i>).
   :feedback_d: It returns the first time the condition is met so nothing is known about the values which are unchecked.
   :pct_on_first: 0.3727144866
   :total_students_attempting: 2133
   :num_students_correct: 2075.0
   :mean_clicks_to_correct: 2.4607228916

   Given the following array instance variable and method, which of the following best describes the contents of ``myStuff`` after (``int m = mystery(n);``) has been executed?
   
   .. code-block:: java
   
     // private field in the class
     private int[ ] myStuff;
   
     //precondition: myStuff contains
     //  integers in no particular order
     public int mystery(int num)
     {
        for (int k = myStuff.length - 1; k >= 0; k--)
        {
            if (myStuff[k] < num)
            {
               return k;
            }
        }
        return -1;
      }