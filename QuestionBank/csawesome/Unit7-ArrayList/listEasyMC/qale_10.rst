.. mchoice:: qale_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listEasyMC
   :topics: Unit7-ArrayList/listEasyMC
   :from_source: T
   :practice: T
   :answer_a: ["Sarah", "Destini", "Layla", "Sharrie"]
   :answer_b: ["Sarah", "Destini", "Anaya", "Layla", "Sharrie"]
   :answer_c: ["Sarah", "Layla", "Sharrie"]
   :answer_d: ["Destini", "Layla", "Sharrie", "Sarah"]
   :correct: a
   :feedback_a: The list is first ["Anaya", "Layla", "Sharrie"] and then ["Destini, "Layla", "Sharrie"] and finally ["Sarah", "Destini, "Layla", "Sharrie"]
   :feedback_b: The set replaces the value at index 0.
   :feedback_c: This would be true if the second add was a set.
   :feedback_d: This would be true if the last add didn't have an index of 0.
   :pct_on_first: 0.5140495868
   :total_students_attempting: 1815
   :num_students_correct: 1768.0
   :mean_clicks_to_correct: 1.9298642534

   What will print when the following code executes?
   
   .. code-block:: java
   
      List<String> list1 = new ArrayList<String>();
      list1.add("Anaya");
      list1.add("Layla");
      list1.add("Sharrie");
      list1.set(0, "Destini");
      list1.add(0, "Sarah");
      System.out.println(list1);