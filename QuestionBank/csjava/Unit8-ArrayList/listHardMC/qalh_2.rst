.. mchoice:: qalh_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listHardMC
   :topics: Unit8-ArrayList/listHardMC
   :from_source: T
   :practice: T
   :answer_a: [0, 0, 4, 2, 5, 0, 3, 0]
   :answer_b: [3, 5, 2, 4, 0, 0, 0, 0]
   :answer_c: [0, 0, 0, 0, 4, 2, 5, 3]
   :answer_d: [4, 2, 5, 3]
   :answer_e: [0, 4, 2, 5, 3]
   :correct: e
   :feedback_a: This shows the original values but this code does remove some zeros so this can't be right.
   :feedback_b: This shows all zeros at the end, but this code removes 0's so this can't be right.
   :feedback_c: This shows all zeros at the beginning, but this code removes zeros so this can't be right.
   :feedback_d: This shows all zeros removed. This would be correct if k was only incremented if a value wasn't removed.
   :feedback_e: This code will loop through the array list and if the current value at the current index (k) is 0, it will remove it. When you remove a value from an array list, it moves all values to the right of that down one. So the first 0 will be deleted but the second one will not since k is incremented even if you remove something. You should only increment k if you didn't remove something and then you would remove all 0's from the list.

   Assume that nums has been created as an ArrayList object and initially contains the following Integer values: [0, 0, 4, 2, 5, 0, 3, 0]. What will nums contain as a result of executing the following method numQuest?

   .. code-block:: java

     private List<Integer> nums;

     //precondition: nums.size() > 0
     //nums contains Integer objects
     public void numQuest() {
        int k = 0;
        Integer zero = new Integer(0);
        while (k < nums.size()) {
           if (nums.get(k).equals(zero))
              nums.remove(k);
           k++;
        }
     }