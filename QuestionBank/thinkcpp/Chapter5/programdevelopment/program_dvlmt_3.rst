.. mchoice:: program_dvlmt_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: programdevelopment
   :topics: Chapter5/programdevelopment
   :from_source: T
   :answer_a: scaffolding - allows the function to compile and return something
   :answer_b: placekeeping - allows the function to compile and return something
   :answer_c: scaffolding - used to test values of temporary variables, later removed
   :answer_d: placekeeping - used to test values of temporary variables, later removed
   :correct: c
   :feedback_a: This is not the correct definition of scaffolding.
   :feedback_b: This is the correct definition of placekeeping but is not the correct answer.
   :feedback_c: Printing out the values allows you to observe whether the function is working or not.
   :feedback_d: This is not the correct definition of placekeeping.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   The print statements in the distance function will be removed after testing. What is this called, and what is its purpose?
   
   ::
   
       #include <iostream>
       using namespace std;
   
       double distance (double x1, double y1, double x2, double y2) {
         double dx = x2 - x1;
         double dy = y2 - y1;
         cout << "dx is " << dx << endl;
         cout << "dy is " << dy << endl;
         return 0.0;
       }