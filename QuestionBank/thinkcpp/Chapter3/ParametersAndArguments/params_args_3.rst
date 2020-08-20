.. fillintheblank:: params_args_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ParametersAndArguments
   :topics: Chapter3/ParametersAndArguments
   :from_source: F
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   ::
   
       #include <iostream>
       using namespace std;
   
       void printTwice (char phil) {
         cout << phil << phil << endl;
       }
   
       int main () {
         double argument = 3.14;
         printTwice (argument);
         return 0;
       }
   
   What will be printed to the terminal?  If nothing will print,
   or if the compiler will throw an error, type "error".
   
   - :error: The type provided does not match the expected parameter type!
     :3.143.14: If you look closely, you'll notice that the type of the argument is not the same as the type of the parameter.
     :.*: Try again!