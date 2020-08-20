.. mchoice:: qalm_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listMedMC
   :topics: ListBasics/listMedMC
   :from_source: T
   :answer_a: [e, d, b]
   :answer_b: [e, d, b, b]
   :answer_c: [e, d, a, b, b]
   :answer_d: [e, d, a, b]
   :correct: b
   :feedback_a: This would be true if you couldn't add a duplicate object to a list, but you can.
   :feedback_b: The list is [a], [a, b], [c, a, b], [c, d, b], [e, d, b], and then [e, d, b, b]
   :feedback_c: This would be true it <code>list1.set(1,"d");</code> was <code>list1.add(1,"d");</code>
   :feedback_d: This would be true it <code>list1.set(1,"d");</code> was <code>list1.add(1,"d");</code> and if lists didn't allow duplicate objects.

   What is printed as a result of executing the following code segment?

   .. code-block:: java

     List<String> list1 = new ArrayList<String>();
     list1.add("a");
     list1.add("b");
     list1.add(0,"c");
     list1.set(1, "d");
     list1.set(0, "e");
     list1.add("b");
     System.out.println(list1);

     What is printed as a result of executing the following code segment?