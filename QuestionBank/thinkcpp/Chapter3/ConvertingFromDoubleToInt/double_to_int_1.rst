.. mchoice:: double_to_int_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ConvertingFromDoubleToInt
   :topics: Chapter3/ConvertingFromDoubleToInt
   :from_source: T
   :answer_a: temp
   :answer_b: 8
   :answer_c: 7
   :answer_d: 8.0
   :answer_e: 7.0
   :correct: c
   :feedback_a: This is the name of a variable. Only the value of a variable will print with cout.
   :feedback_b: Remember that converting to an integer always rounds down.
   :feedback_c: Correct!
   :feedback_d: This is not an integer data type, and it's not the right number.
   :feedback_e: This is not an integer data type.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   In the lab, we measured a temperature of 7.99999999 degrees C, using
   an extremely precise measuring device.  Now we are writing a program
   to perform some calculations with our data.  Consider the following C++
   code.
   
   ::
   
       int main () {
         double temp = 7.99999999;
         int roundedTemp = int (temp);
         cout << roundedTemp;
       }
   
   What is the value of roundedTemp?