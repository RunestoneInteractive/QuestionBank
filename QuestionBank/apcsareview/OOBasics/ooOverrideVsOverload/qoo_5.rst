.. mchoice:: qoo_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooOverrideVsOverload
   :topics: OOBasics/ooOverrideVsOverload
   :from_source: T
   :answer_a: public void getFood()
   :answer_b: public String getFood(int quantity)
   :answer_c: public String getFood()
   :correct: c
   :feedback_a: The return type must match the parent method return type.
   :feedback_b: The parameter lists must match (must have the same types in the same order).
   :feedback_c: The return type and parameter lists must match.

    Which of the following declarations in ``Student`` would correctly *override* the ``getFood`` method in ``Person``?

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