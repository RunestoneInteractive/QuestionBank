.. mchoice:: point_objects_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: point_objects
   :topics: Chapter8/point_objects
   :from_source: T
   :practice: T
   :answer_a: blank.x = 3.0;
   :answer_b: Point.x = 3.0;
   :answer_c: nice.x = 3.0;
   :answer_d: nice.x = 3.0
   :correct: c
   :feedback_a: This declaration would not work for the specific code block below.
   :feedback_b: The specific name of the structure should be used, not its type.
   :feedback_c: Yes, we can access and modify the instance variables using the dot operator.
   :feedback_d: The semi-colon is missing at the end.
   :pct_on_first: 1.0
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.0

   Which of the following would be the correct way to initialize the instance variables
   of the ``Point`` object?
   
   .. code-block:: cpp
   
      struct Point () {
        double x, y;
      };
   
      int main() {
        Point nice;
      }