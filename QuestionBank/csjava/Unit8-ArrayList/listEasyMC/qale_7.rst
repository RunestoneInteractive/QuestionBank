.. mchoice:: qale_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listEasyMC
   :topics: Unit8-ArrayList/listEasyMC
   :from_source: T
   :practice: T
   :answer_a: nums.add(2, 0);
   :answer_b: nums.add(2, 1);
   :answer_c: nums.add(0, 2);
   :answer_d: nums.add(1, 2);
   :answer_e: nums.add(2, 2);
   :correct: d
   :feedback_a: This would add 0 at index 2.  Remember that the method is <code>add(index, obj)</code>.
   :feedback_b: This would add 1 at index 2.  Remember that the method is <code>add(index, obj)</code>
   :feedback_c: This would add 2 at index 0 which would result in <code>[2, 1, 3, 4]</code>
   :feedback_d: This would add 2 at index 1 which would result in <code>[1, 2, 3, 4]</code>
   :feedback_e: This would add 2 at index 2 which would result in <code>[1, 3, 2, 4]</code>

   Which of the following is the correct way to add 2 between the 1 and 3 in the following list ``nums = [1, 3, 4]``?