.. mchoice:: qtnt1_12
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: II and III
   :answer_e: I and II
   :correct: c
   :feedback_a: Because List is an abstract class you can not create a new object of the type List.
   :feedback_b: The type parameter in a generic ArrayList must be a class type, not a primitive type. int is a primitive type.
   :feedback_c: Since an ArrayList is a List (implements the List interface), we can declare an ArrayList object as a List object.  This is called upcasting since we are casting it to the parent type.
   :feedback_d: III is correct, but II will cause a compile time error since we cannot use a primitive (int) as the type parameter in a generic ArrayList.
   :feedback_e: Both of these solutions will cause an error.
   :pct_on_first: 0.2358490566
   :total_students_attempting: 318
   :num_students_correct: 317.0
   :mean_clicks_to_correct: 2.476340694

   Which of these declarations will *not* cause an error?
   
   .. code-block:: java
   
      I ArrayList<String> stringList = new List<String>();
      II List<int> intList = new ArrayList<int>();
      III List<String> stringList = new ArrayList<String>();