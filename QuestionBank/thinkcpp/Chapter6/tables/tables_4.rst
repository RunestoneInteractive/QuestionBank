.. mchoice:: tables_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: tables
   :topics: Chapter6/tables
   :from_source: T
   :practice: T
   :answer_a: Change ``pow(x,2)`` to ``pow(3,x)`` and change ``x = x + 1`` to ``x = x + 2``.
   :answer_b: Change ``pow(x,2)`` to ``pow(x,3)``.
   :answer_c: Change ``pow(x,2)`` to ``pow(x,3)`` and change ``x = x + 1`` to ``x = x + 2``.
   :answer_d: Change ``x < 11`` to ``x < 6`` and change ``pow(x,2)`` to ``pow(x,3)``.
   :correct: c
   :feedback_a: Check the order of the ``pow`` function!
   :feedback_b: This will print out the first ten perfect cubes.
   :feedback_c: Changing both the ``pow`` function and the increment in this way gives us the right answer.
   :feedback_d: This will print out the first five perfect cubes, but not the first five odd perfect cubes.
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   How can we modify the code below to print out a table of the first five odd numbers and their perfect cubes?
   
   .. code-block:: cpp
   
     int main() {
       int x = 1;
       while (x < 11) {
         cout << x << "\t" << pow(x, 2) << endl;
         x = x + 1;
       }
     }