.. mchoice:: output_vars_1
   :author: bmiller
   :difficulty: 3
   :basecourse: thinkcpp
   :topics: Chapter2/Outputtingvariables
   :from_source: T
   :answer_a: a
   :answer_b: b
   :answer_c: z
   :answer_d: 8
   :answer_e: Nothing! There will be a compile error!
   :correct: a
   :feedback_a: The string, not the variable, a will be printed.
   :feedback_b: b will not be printed.
   :feedback_c: The cout statement prints a, not the value of the variable a.
   :feedback_d: z is the value of a and will not be printed
   :feedback_e: There is no type mismatch, so there will not be a compile error.

   What prints when the following code is run?

   ::

       int main () {
         char a;
         char b;
         a = 'z';
         b = '8';
         cout << "a";
       }