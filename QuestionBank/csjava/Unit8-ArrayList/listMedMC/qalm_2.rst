.. mchoice:: qalm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listMedMC
   :topics: Unit8-ArrayList/listMedMC
   :from_source: T
   :practice: T
   :answer_a: [0, 4, 2, 5, 3]
   :answer_b: [3, 5, 2, 4, 0, 0, 0]
   :answer_c: [0, 0, 0, 4, 2, 5, 3]
   :answer_d: [4, 2, 5, 3]
   :answer_e: [0, 0, 4, 2, 5, 0, 3]
   :correct: d
   :feedback_a: This code will loop through the array list and if the current value at the current index (k) is 0 it will remove it.  When you remove a value from an array list it moves all values to the right of that one to the the left. It only increments the index when it doesn't find a zero so it work work correctly.
   :feedback_b: This shows all zeros at the end and this code removes 0's so this can't be right.
   :feedback_c: This shows all zeros at the beginning and this code removes zeros so this can't be right.
   :feedback_d: This shows all zeros removed.  Since k is only incremented if a value wasn't removed this will work correctly.
   :feedback_e: This shows the original values, but this code does remove some zeros so this can't be right.

   Given the following code and assume that ``nums`` initially contains [0, 0, 4, 2, 5, 0, 3], what will ``nums`` contain as a result of executing numQuest?

   .. code-block:: java

      private List<Integer> nums;

      // precondition: nums.size() > 0;
      // nums contains Integer objects
      public void numQuest()
      {
        int k = 0;
        Integer zero = new Integer(0);
        while (k < nums.size())
        {
         if (nums.get(k).equals(zero))
           nums.remove(k);
         else
            k++;
        }
      }