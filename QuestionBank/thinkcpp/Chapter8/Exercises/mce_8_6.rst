.. mchoice:: mce_8_6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: Exercises
    :topics: Chapter8/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 3.0

    What is the value of ``s.coffeeCupFull`` when the code is done running?
    
    .. code-block:: cpp
    
      struct Student {
        string name;
        bool isSleepy;
        bool coffeeCupFull;
      };
    
      void pourCoffee (Student s) {
        s.coffeeCupFull = true;
      }
    
      int main() {
        Student s = { "Thor Odinson", true, false };
        if (s.isSleepy) {
          pourCoffee (s);
        }
      }
    
    - true
    
      - C++ outputs boolean values as either a 0 or 1.
    
    - false
    
      - C++ outputs boolean values as either a 0 or 1.
    
    - 1
    
      - Take a closer look at the function definition of ``pourCoffee``.
    
    - 0
    
      + Since we pass a ``Student`` object by value to ``pourCoffee``, the function makes a copy of the object and does not modify the original.