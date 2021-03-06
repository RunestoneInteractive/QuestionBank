.. mchoice:: qListRem3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-4-arraylist-algorithms
   :topics: Unit8-ArrayList/topic-8-4-arraylist-algorithms
   :from_source: T
   :answer_a: [1, 2, 3, 4, 5]
   :answer_b: [1, 2, 4, 5, 6]
   :answer_c: [1, 2, 5, 4, 6]
   :answer_d: [1, 5, 2, 4, 6]
   :correct: d
   :feedback_a: The <code>set</code> will replace the 3 at index 2 so this isn't correct.
   :feedback_b: The <code>add</code> with an index of 1 and a value of 5 adds the 5 at index 1 not 3. Remember that the first index is 0.
   :feedback_c: The <code>set</code> will change the item at index 2 to 4.  The <code>add</code> of 5 at index 1 will move everything else to the right and insert 5.  The last <code>add</code> will be at the end of the list.
   :feedback_d: <code>add</code> without an index adds at the end, <code>set</code> will replace the item at that index, <code>add</code> with an index will move all current values at that index or beyond to the right.

   What will print when the following code executes?

   .. code-block:: java

      List<Integer> numList = new ArrayList<Integer>();
      numList.add(new Integer(1));
      numList.add(new Integer(2));
      numList.add(new Integer(3));
      numList.set(2,new Integer(4));
      numList.add(1, new Integer(5));
      numList.add(new Integer(6));
      System.out.println(numList);