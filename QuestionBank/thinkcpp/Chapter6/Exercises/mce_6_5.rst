.. mchoice:: mce_6_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter6
    :subchapter: Exercises
    :topics: Chapter6/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
     int main() {
       int n = 10;
       cout << "Da ";
       cout << "na ";
       while (n != 3) {
         cout << "na ";
       }
       cout << "Batman!";
     }
    
    - Batman!
    
      - Take a closer look at the while loop.
    
    - Da Batman!
    
      - Take a closer look at the while loop.
    
    - Da na na na na na na na na Batman!
    
      - Take a closer look at the while loop.
    
    - The end condition is never met, so it will result in an infinite loop.
    
      + Since we never change the value of ``n``, 10 will never equal 3 so the code will run forever.