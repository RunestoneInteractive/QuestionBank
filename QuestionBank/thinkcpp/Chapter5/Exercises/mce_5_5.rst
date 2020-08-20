.. mchoice:: mce_5_5
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
    :mean_clicks_to_correct: 1.5

    What is the output of the code below?
    
    .. code-block:: cpp
    
      int main() {
        bool x = 2 < 3;
        cout << x;
        cout << false;
        cout << ((1 + 4) * 4 > 24);
        cout << (23 == (32 + 2 - 11));
      }
    
    - 1001
    
      + Since the first and last statements are true and the middle two are false, this is the correct output.
    
    - truefalsefalsetrue
    
      - In C++, boolean values are outputted as 0 or 1.
    
    - 1false01
    
      - Since the second ``cout`` statement doesn't have quotes around the word "false", the value of 0 is outputted.
    
    - 0110
    
      - Remember that if a boolean expression is true, it has a value of 1.