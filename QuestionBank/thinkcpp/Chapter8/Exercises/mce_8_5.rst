.. mchoice:: mce_8_5
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
    
      int calculateDensity (Cube c) {
        return c.mass / c.volume;
      }
    
      int main() {
        Cube c = { 2, 8, 4 };
        int density = calculateDensity (c);
        cout << density;
      }
    
    - 0
    
      + Because of integer division, ``density`` is 0 and thus the output is 0.
    
    - 2
    
      - Density is mass divided by volume.
    
    - 0.5
    
      - Take a closer look at what kind of division we are doing.
    
    - 1
    
      - Integer division truncates the extra digits.