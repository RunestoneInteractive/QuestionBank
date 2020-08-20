.. mchoice:: floating_point_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: Floating-point
   :topics: Chapter3/Floating-point
   :from_source: T
   :answer_a: e
   :answer_b: 3
   :answer_c: 2
   :answer_d: 3.0
   :answer_e: 2.71828
   :correct: c
   :feedback_a: This is the name of a variable. Only the value of a variable will print with cout.
   :feedback_b: Converting to an int always rounds down.
   :feedback_c: When we converted e to an int, e was rounded down to 2. When we converted e_nt to e_double, the decimal places from e were lost, and the value of e_double is 2.
   :feedback_d: Converting to an int always rounds down.
   :feedback_e: When we converted e to an int, e was rounded down to 2. When we converted e_nt to e_double, the decimal places from e were lost.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   In the lab, we measured a temperature of 7.99999999 degrees C, using
   an extremely precise measuring device.  Now we are writing a program
   to perform some calculations with our data.  Consider the following C++
   code.
   
   ::
   
       double e = 2.71828;
       int e_int = e;
       double e_double = eInt;
       cout << e_double;
   
   What is the value of ``e_double`` that is printed to the terminal?