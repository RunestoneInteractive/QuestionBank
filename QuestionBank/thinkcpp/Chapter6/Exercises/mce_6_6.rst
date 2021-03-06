.. mchoice:: mce_6_6
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
    :mean_clicks_to_correct: 4.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
     int main() {
       int x = 1;
       while (x < 6) {
         cout << x << "\t" << pow (x, 5) / pow (x, 3) << endl;
         x++;
       }
     }
    
    - The first six perfect fifths.
    
      - Take a closer look at the while loop and what ``x`` was initialized to.
    
    - The first six perfect squares.
    
      - Take a closer look at the while loop and what ``x`` was initialized to.
    
    - The first five perfect squares.
    
      + Dividing ``x`` to the power of 5 by ``x`` to the power of 3 effectively results in perfect squares.
    
    - The first five perfect cubes.
    
      - Take a closer look at the mathematical expression inside the while loop.