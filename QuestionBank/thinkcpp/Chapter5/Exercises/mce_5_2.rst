.. mchoice:: mce_5_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter5
    :subchapter: Exercises
    :topics: Chapter5/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.0

    What would be returned by ``secretFunction`` if the input was 14?
    
    .. code-block:: cpp
    
      int secretFunction (int input) {
        if (input % 2 == 0) {
          return 3 * input - 2;
        }
        else {
          if (input % 7 == 0) {
            return input;
          }
          return 2 * input + 9;
        }
        return input + 4;
      }
    
    - 14
    
      - Although 14 is divisible by 7, take another look at the conditionals.
    
    - 18
    
      - The flow of code would never reach the last return statement.
    
    - 37
    
      - Take a closer look at the conditional statements.
    
    - 40
    
      + Since 14 is divisible by 2, the function returns two less than three times 14.