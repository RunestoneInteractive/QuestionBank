.. mchoice:: qvm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: vMedMC
   :topics: VariableBasics/vMedMC
   :from_source: T
   :answer_a: 2147483647
   :answer_b: 0
   :answer_c: There will be a compile time error
   :answer_d: -2147483648
   :answer_e: There will be a run time error
   :correct: d
   :feedback_a: This would be true if it was printing just the maximum integer value.
   :feedback_b: This might make sense, but adding one to the maximum integer value gives the minimum integer value.
   :feedback_c: It will compile, but what will it do when you run it?
   :feedback_d: Adding one to the maximum integer value gives the minimum integer value due to overflow.
   :feedback_e: This makes sense, but it is not what happens.

   What will be printed by ``System.out.println(Integer.MAX_VALUE + 1);``?