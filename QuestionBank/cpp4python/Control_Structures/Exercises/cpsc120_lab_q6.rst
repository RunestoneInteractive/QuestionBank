.. parsonsprob:: cpsc120_lab_q6
   :author: Matthew Zuniga
   :difficulty: 2.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   Another type of for loop would be the <b>ranged based for-loop.</b><br>
   Use the range based for-loop to add up all EVEN and ODD numbers from 1 to 100 in their respective variables called evenSum and oddSum. <br>
   You will need to populate the vector nums first.
   
   -----
   int evenSum = 0;
   int oddSum = 0;
   vector &#60;int&#62; nums;
   =====
   for(int i = 0; i < 100; i++) {
    nums.push_back(i);
   }
   =====
   for(int num : nums) {
   =====
    if(num % 2 == 0) {
     evenSum += num;
    }
   =====
    else {
     oddSum += num;
    }
   =====
   #distractorfor(int nums : num) {
   =====