.. mchoice:: qloopList_1
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :answer_a: [0, 4, 2, 5, 3]
   :answer_b: [3, 5, 2, 4, 0, 0, 0, 0]
   :answer_c: [0, 0, 0, 0, 4, 2, 5, 3]
   :answer_d: [4, 2, 5, 3]
   :correct: a
   :feedback_a: Incrementing the index each time through the loop will miss when there are two zeros in a row.
   :feedback_b: This would be true if the code moved the zeros to the end, but that is not what it does.
   :feedback_c: This would be true if the code moved the zeros to the font, but that is not what it does.
   :feedback_d: This would be correct if <code>k</code> was only incremented when an item was not removed from the list.

   Assume that ``nums`` has been created as an ``ArrayList`` object and it initially contains the following ``Integer`` values [0, 0, 4, 2, 5, 0, 3, 0]. What will ``nums`` contain as a result of executing ``numQuest``?

   .. code-block:: java

      ArrayList<Integer> list1 = new ArrayList<Integer>();
      private ArrayList<Integer> nums;

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
            k++;
         }
      }