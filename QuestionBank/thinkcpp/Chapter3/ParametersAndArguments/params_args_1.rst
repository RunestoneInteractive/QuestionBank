.. fillintheblank:: params_args_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ParametersAndArguments
   :topics: Chapter3/ParametersAndArguments
   :from_source: T
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 3.0

   ::
   
       #include <iostream>
       using namespace std;
   
       void printTwice (char phil) {
         cout << phil << phil << endl;
       }
   
       int main () {
         string argument = "s";
         printTwice (argument);
         return 0;
       }
   
   What will be printed to the terminal?  If nothing will print,
   or if the compiler will throw an error, type "error".
   
   - :error: The type provided does not match the expected parameter type!
     :ss: The type provided does not match the expected parameter type!
     :.*: Try again!