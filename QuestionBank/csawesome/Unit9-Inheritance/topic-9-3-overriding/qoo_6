.. mchoice:: qoo_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-3-overriding
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :practice: T
   :answer_a: public void getFood()
   :answer_b: public String getFood(int quantity)
   :answer_c: public String getFood()
   :correct: b
   :feedback_a: You can not just change the return type to overload a method.
   :feedback_b: For overloading you must change the parameter list (number, type, or order of parameters).
   :feedback_c: How is this different from the current declaration for <code>getFood</code>?
   :pct_on_first: 0.5726141079
   :total_students_attempting: 1928
   :num_students_correct: 1920.0
   :mean_clicks_to_correct: 1.5708333333

    Which of the following declarations in ``Person`` would correctly *overload* the ``getFood`` method in ``Person``?
   
    .. code-block:: java
   
      public class Person
      {
         private String name = null;
   
         public Person(String theName)
         {
            name = theName;
         }
   
         public String getFood()
         {
            return "Hamburger";
         }
      }
   
      public class Student extends Person
      {
         private int id;
         private static int nextId = 0;
   
         public Student(String theName)
         {
           super(theName);
           id = nextId;
           nextId++;
         }
   
         public int getId() {return id;}
         public void setId (int theId)
         {
            this.id = theId;
         }
      }