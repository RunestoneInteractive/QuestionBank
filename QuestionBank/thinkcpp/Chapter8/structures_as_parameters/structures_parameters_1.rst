.. mchoice:: structures_parameters_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: structures_as_parameters
   :topics: Chapter8/structures_as_parameters
   :from_source: T
   :practice: T
   :answer_a: (-2.0, -7.0)
   :answer_b: (2.0, 7.0)
   :answer_c: (-7.0, -2.0)
   :answer_d: (7.0, 2.0)
   :correct: c
   :feedback_a: Take a close look at the printOppositeCoordinate function.
   :feedback_b: Take a close look at the printOppositeCoordinate function.
   :feedback_c: Yes, this is the correct output.
   :feedback_d: Take a close look at the printOppositeCoordinate function.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   What will print?
   
   .. code-block:: cpp
   
      struct Coordinate {
        double x, y;
      };
   
      void printOppositeCoordinate (Point p) {
        cout << "(" << -p.y << ", " << -p.x << ")" << endl;
      }
   
      int main() {
        Coordinate coord = { 2.0, 7.0 };
        printOppositeCoordinate (coord);
      }