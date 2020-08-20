.. mchoice:: mce_7_9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: Exercises
    :topics: Chapter7/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
     int main() {
       string quote = "Life is like a box of chocolates. You never know what you’re gonna get.";
       int i = 0;
       int count = 0;
       while (i < quote.length()) {
         if (quote[i] == 'e') {
           count++;
         }
         i++;
       }
       cout << count;
     }
    
    - 0
    
      - Are there any occurences of the letter 'e' in ``quote``?
    
    - 6
    
      - Count the number of 'e's in ``quote``.
    
    - 7
    
      + There are 7 occurences of the letter 'e' in ``quote``.
    
    - 12
    
      - Count the number of 'e's in ``quote``.