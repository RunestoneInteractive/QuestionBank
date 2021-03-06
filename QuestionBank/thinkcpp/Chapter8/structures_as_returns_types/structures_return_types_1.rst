.. mchoice:: structures_return_types_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: structures_as_returns_types
   :topics: Chapter8/structures_as_returns_types
   :from_source: T
   :practice: T
   :answer_a: addTwo, printPoint, findCenter
   :answer_b: printPoint, findCenter
   :answer_c: addTwo, findCenter
   :answer_d: Point, Rectangle
   :correct: c
   :feedback_a: Look at the return type, found before the function name in its definition.
   :feedback_b: Look at the return type, found before the function name in its definition.
   :feedback_c: Correct!
   :feedback_d: These are structures, not functions.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Which functions will return a structure?
   
   .. code-block:: cpp
   
      struct Point {
        double x, y;
      };
   
      struct Rectangle {
        Point corner;
        double width, height;
      };
   
      Rectangle addTwo (Point& p) {
        double x = p.x + 2;
        double y = p.y + 2;
        Point result = {x, y};
        return result;
      }
   
      void printPoint (Point p) {
        cout << "(" << p.x << ", " << p.y << ")" << endl;
      }
   
      Point findCenter (Rectangle& box) {
        double x = box.corner.x + box.width/2;
        double y = box.corner.y + box.height/2;
        Point result = {x, y};
        return result;
      }
   
      int main() {
        Rectangle box = { {0.0, 0.0}, 100, 200 };
        Point center = findCenter (box);
        cout << addTwo (center) << endl;
        printPoint (center);
      }