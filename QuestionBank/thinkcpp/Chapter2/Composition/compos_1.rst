.. mchoice:: compos_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Composition
   :topics: Chapter2/Composition
   :from_source: T
   :answer_a: Change line 5 to pets = dogs + cats;
   :answer_b: Change line 5 to int pets = dogs + cats;
   :answer_c: Change line 5 to pets == dogs + cats;
   :answer_d: Change line 5 to int pets == dogs + cats;
   :answer_e: No change, the code runs fine as is.
   :correct: a
   :feedback_a: Assignment statements operate such that the evaluated expression on the right is assigned to the variable on the left.
   :feedback_b: pets has already been declared as an int.
   :feedback_c: The == operator checks if the left side EQUALS the right side.  It is not the correct operator here.
   :feedback_d: pets has already been declared as an int.  Also, the == operator is not the proper choice here.
   :feedback_e: Assignment statements assign the value on the right to the variable on the left.
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.3333333333

   What must be changed in order for this code block to work?
   
   .. code-block::
       :linenos:
   
       int main () {
         int dogs = 3;
         int cats = 6;
         int pets;
         dogs + cats = pets;
         cout << "I have " << pets << " pets!";
         return 0;
       }