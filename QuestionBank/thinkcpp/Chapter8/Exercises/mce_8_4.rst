.. mchoice:: mce_8_4
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
    
      struct Cube {
        int edgeLength;
        int volume;
        int mass;
      };
    
      int main() {
        Cube c;
        c.edgeLength = 4;
        c.volume = 64;
        c.mass = 128;
        cout << c.edgeLength << ", " << c.volume << "," << c.mass << ", ";
        int density = c.mass / c.volume;
        cout << density;
      }
    
    - 4, 2, 64, 128
    
      - Check the ordering of the output statements.
    
    - 4, 64, 128, 2
    
      - Take a closer look at the output statements.
    
    - 4, 64,128, 2
    
      + The code outputs all instance variables and the density in the proper order.
    
    - edgeLength, volume, mass, density
    
      - Dot notation accesses the values of the instance variables, not the names.