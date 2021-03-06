.. mchoice:: qListRem1
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :answer_a: [1, 2, 3, 4, 5]
   :answer_b: [1, 2, 4, 5, 6]
   :answer_c: [1, 2, 5, 4, 6]
   :answer_d: [1, 5, 2, 4, 6]
   :correct: c
   :feedback_a: The <code>set</code> will replace the item at index 2 so this can not be right.
   :feedback_b: The <code>add</code> with an index of 2 and a value of 5 adds the 5 at index 2 not 3. Remember that the first index is 0.
   :feedback_c: The <code>set</code> will change the item at index 2 to 4.  The add of 5 at index 2 will move everything else to the right and insert 5.  The last <code>add</code> will be at the end of the list.
   :feedback_d: The <code>add</code> with an index of 2 and a value of 5 adds the 5 at index 2 not 1. Remember that the first index is 0.

   What will print when the following code executes?

   .. code-block:: java

      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(1);
      list1.add(2);
      list1.add(3);
      list1.set(2, 4);
      list1.add(2, 5);
      list1.add(6);
      System.out.println(list1);