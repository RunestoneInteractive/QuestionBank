.. mchoice:: mce_6_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter6
    :subchapter: Exercises
    :topics: Chapter6/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.0
    :total_students_attempting: 2
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
      int main() {
        int n = 10;
        // cout << "Da ";
        cout << "na ";
        while (n != 3) {
          cout << "na ";
          n--;
        }
        cout << "Batman!";
      }
    
    - na na na na na na na na Batman!
    
      + The code prints out eight "na"s before printing out "Batman!"
    
    - na na na na na na na Batman!
    
      - Look over the code carefully. There are output statements before the while loop.
    
    - Da na na na na na na na na Batman!
    
      - Will "Da" ever be printed?
    
    - The end condition is never met, so it will result in an infinite loop.
    
      - Since we repeatedly decrement ``n`` inside the while loop, it will eventually be equal to 3 and the while loop will terminate.