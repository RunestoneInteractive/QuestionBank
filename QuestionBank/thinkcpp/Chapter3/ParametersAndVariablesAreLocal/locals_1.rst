.. mchoice:: locals_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ParametersAndVariablesAreLocal
   :topics: Chapter3/ParametersAndVariablesAreLocal
   :from_source: T
   :answer_a: 1 local variable, 1 parameter
   :answer_b: 0 local variables, 1 parameter
   :answer_c: 2 local variables, 0 parameters
   :answer_d: 2 local variables, 1 parameter
   :correct: c
   :feedback_a: A parameter would be located within the parentheses next to the function's name.
   :feedback_b: A parameter would be located within the parentheses next to the function's name.
   :feedback_c: Correct!
   :feedback_d: A parameter would be located within the parentheses next to the function's name.
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.5

   How many local variables and parameters does ``main`` have?
   
   ::
   
       void printHelloName (string name) {
         cout << "Hello " << name << "!";
       }
   
       int main () {
         string name1 = "Phil";
         printHelloName(name1);
         string name2 = "Joe";
         printHelloName(name2);
         return 0;
       }