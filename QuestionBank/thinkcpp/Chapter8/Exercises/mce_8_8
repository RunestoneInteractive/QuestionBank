.. mchoice:: mce_8_8
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
    :mean_clicks_to_correct: 2.0

    What is the output of the code below?
    
    .. code-block:: cpp
    
      void foo (int& x, int y) {
        x = x + 4;
        y = 2 * x + 3 * y;
      }
    
      void bar (int x, int y) {
        y = 2 * x;
        x = x - 1;
        foo (x, x);
      }
    
      void func (int &x, int& y) {
        x = x + 3;
        bar (y, x);
      }
    
      int main() {
        int x = 4;
        int y = 7;
        func (y, x);
        cout << x << ", " << y;
      }
    
    - 4, 7
    
      - Take a closer look at ``func`` and its parameters. Are they passed by value, passed by reference, or both?
    
    - 4, 10
    
      + Since ``bar`` doesn't pass either parameter by reference, neither ``bar`` nor ``foo`` affect the values of ``x`` and ``y``.
    
    - 7, 7
    
      - Check the order of the arguments passed into ``func``.
    
    - 35, 8
    
      - Take a closer look at the three functions. Are they all passed by reference?