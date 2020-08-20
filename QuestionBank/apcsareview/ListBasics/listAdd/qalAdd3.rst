.. mchoice:: qalAdd3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listAdd
   :topics: ListBasics/listAdd
   :from_source: T
   :answer_a: [5, 4, 3, 2]
   :answer_b: [5, 4, 1, 3]
   :answer_c: [2, 5, 4, 3]
   :answer_d: [5, 2, 4, 3]
   :correct: d
   :feedback_a: Remember that <code>add(obj)</code> adds the object to the end of the list.
   :feedback_b: This would be true if it was <code>add(obj, index)</code>, but it is <code>add(index, obj)</code>
   :feedback_c: This would be true if the first index was 1, but it is 0.
   :feedback_d: This adds the 2 to index 1, but first moves all other values past that index to the right.

   What will print when the following code executes?

   .. code-block:: java

      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(5);
      list1.add(4);
      list1.add(3);
      list1.add(1, 2);
      System.out.println(list1);