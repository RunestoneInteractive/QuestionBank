.. mchoice:: qpret_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit1-Getting-Started
    :subchapter: ptest1
    :topics: Unit1-Getting-Started/ptest1
    :from_source: T
    :answer_a: 0 1 2 0 1 2 0 1
    :answer_b: 0 2 1 0 2 1 0 2
    :answer_c: 0 2 1 0 2 1 0 2 1
    :answer_d: 2 1 0 2 1 0 2 1
    :answer_e: 0 2 1 0 2 1 0
    :correct: b
    :feedback_a: The second time through the loop the value of num is 2 and 2 % 3 is 2 not 1.
    :feedback_b: The while loop will iterate 8 times. The value of num each time through the loop is: 0, 2, 4, 6, 8, 10, 12, and 14. The corresponding remainder operator of 3 is: 0, 2, 1, 0, 2, 1, 0, 2, which is print to the console.
    :feedback_c: The loop will iterate 8 times not 9. When the value of num exceeds 14, num will no longer be evaluated against the conditional statements. The remainder operator of 3 will be evaluated on the num values of 0, 2, 4, 6, 8, 10, 12 and 14.
    :feedback_d: The value of num the first time through the loop is 0 so the first remainder is 0 not 2. This would be true if the value of num was 2 to start.
    :feedback_e: This would be true if the loop stopped when the value of num was less than 14 but it is less than or equal to 14.
    :pct_on_first: 0.3520271477
    :total_students_attempting: 5599
    :num_students_correct: 2353.0
    :mean_clicks_to_correct: 1.3438164046

    Given the following code segment, what is printed when it executes?
    
    .. code-block:: java
    
        public static void test()
        {
           int num = 0;
           while(num <= 14)
           {
    
              if(num % 3 == 1)
              {
                 System.out.print("1 ");
              }
    
              else if (num % 3 == 2)
              {
                 System.out.print("2 ");
              }
    
              else
              {
                 System.out.print("0 ");
              }
    
              num += 2;
           }
       }