.. mchoice:: qalAdd1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listAdd
   :topics: ListBasics/listAdd
   :from_source: T
   :answer_a: [1, 2, 3, 4, 5]
   :answer_b: [1, 4, 2, 3, 5]
   :answer_c: [1, 2, 4, 3, 5]
   :answer_d: [1, 2, 4, 5]
   :correct: c
   :feedback_a: This would be true if all the <code>add</code> method calls were <code>add(value)</code>, but at least one is not.
   :feedback_b: This would be true if it was <code>add(1, new Integer(4))</code>
   :feedback_c: The <code>add(2, new Integer(4))</code> will put the 4 at index 2, but first move the 3 to index 3.
   :feedback_d: This would be true if the <code>add(2, new Integer(4))</code> replaced what was at index 2, but it actually moves the value currently at index 2 to index 3.

   What will print when the following code executes?

   .. code-block:: java

      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(new Integer(1));
      list1.add(new Integer(2));
      list1.add(new Integer(3));
      list1.add(2, new Integer(4));
      list1.add(new Integer(5));
      System.out.println(list1);