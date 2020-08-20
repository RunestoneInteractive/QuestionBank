.. mchoice:: qpret_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit1-Getting-Started
    :subchapter: ptest1
    :topics: Unit1-Getting-Started/ptest1
    :from_source: T
    :answer_a: var1=1, var2=1
    :answer_b: var1=3, var2=-1
    :answer_c: var1=0, var2=2
    :answer_d: var1=2, var2=0
    :answer_e: The loop won't finish executing because of a division by zero.
    :correct: d
    :feedback_a: This would be true if the body of the while loop only executed one time, but it executes twice.
    :feedback_b: This would be true if the body of the while loop executed 3 times, but it exectues twice.
    :feedback_c: This would be true if the body of the while loop never executed. This would have happened if the while check was if var1 != 0 instead of var2 != 0.
    :feedback_d: The loop starts with var1=0 and var2=2. The while checks that var2 isn't 0 (2!=0) and that var1 / var2 is greater than or equal to zero (0/2=0) so this is equal to zero and the body of the while loop will execute. The variable var1 has 1 added to it for a new value of 1. The variable var2 has 1 subtracted from it for a value of 1. At this point var1=1 and var2=1. The while condition is checked again. Since var2 isn't 0 (1!=0) and var1/var2 (1/1=1) is >= 0 so the body of the loop will execute again. The variable var1 has 1 added to it for a new value of 2. The variable var2 has 1 subtracted from it for a value of 0. At this point var1=2 and var2=0. The while condition is checked again. Since var2 is zero the while loop stops and the value of var1 is 2 and var2 is 0.
    :feedback_e: The operation 0 / 2 won't cause a division by zero. The result is just zero.
    :pct_on_first: 0.3014430786
    :total_students_attempting: 5613
    :num_students_correct: 2123.0
    :mean_clicks_to_correct: 1.4333490344

    Given the following code segment, what are the values of ``var1`` and ``var2`` after the while loop finishes?
    
    .. code-block:: java
    
        int var1 = 0;
        int var2 = 2;
    
        while ((var2 != 0) && ((var1 / var2) >= 0))
        {
           var1 = var1 + 1;
           var2 = var2 - 1;
        }