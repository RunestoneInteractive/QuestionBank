.. mchoice:: mce_5_6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter5
    :subchapter: Exercises
    :topics: Chapter5/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 1.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 1.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
      int main() {
        bool w = !(2 * 3 == 6 || 4 - 3 > 8);
        bool x = true || 4 > 6;
        bool y = 3 != 6 - 3 && 23 >= 23;
        bool z = (4 + 9 < 15 && 3 != 4) || 2 + 5 == 7;
        cout << w << x << y << z;
      }
    
    - 0101
    
      + Since the expressions are false, true, false, and true, the output is 0101.
    
    - 1101
    
      - Remember the NOT operator (!) inverts the value of a boolean.
    
    - 0100
    
      - Take a closer look at the order of operations.
    
    - 0110
    
      - Take a closer look at the expressions.