.. mchoice:: qoo_13
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/topic-9-6-polymorphism
   :from_source: T
   :practice: T
   :answer_a: b.getISBN();
   :answer_b: b.getDefintion();
   :answer_c: ((Dictionary) b).getDefinition();
   :correct: b
   :feedback_a: The b object is actually a Dictionary object which inherits the getISBN method from Book.
   :feedback_b: At compile time the declared type is Book and the Book class does not have or inherit a getDefintion method.
   :feedback_c: Casting to Dictionary means that the compiler will check the Dictionary class for the getDefinition method.

   Given the following class definitions and a declaration of Book b = new Dictionary which of the following will cause a compile-time error?

   .. code-block:: java

      public class Book
      {
         public String getISBN()
         {
            // implementation not shown
         }

         // constructors, fields, and other methods not shown
      }

      public class Dictionary extends Book
      {
         public String getDefinition()
         {
            // implementation not shown
         }
      }