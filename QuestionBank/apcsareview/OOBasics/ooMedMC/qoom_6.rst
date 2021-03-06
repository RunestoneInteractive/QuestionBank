.. mchoice:: qoom_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooMedMC
   :topics: OOBasics/ooMedMC
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: I and III only
   :answer_d: III only
   :answer_e: I, II, and III
   :correct: c
   :feedback_a: Both I and III are correct. I is correct because variable <code>b</code> has been declared to be an object of the class <code>Book</code> so you can invoke any public methods that are defined in the <code>Book</code> class or in parents of <code>Book</code>. II is not correct because you can't invoke methods in the <code>Dictionary</code> class directly on <code>b</code> since <code>b</code> is declared to be of type <code>Book</code> not type <code>Dictionary</code> and <code>Dictionary</code> is a subclass of <code>Book</code> not a parent class of <code>Book</code>. III is correct because you can cast <code>b</code> to type <code>Dictionary</code> and then invoke public methods in <code>Dictionary</code>.
   :feedback_b: You can't invoke methods in the <code>Dictionary</code> class directly on <code>b</code> since <code>b</code> is declared to be of type <code>Book</code> not type <code>Dictionary</code> and <code>Dictionary</code> is a subclass of <code>Book</code> not a parent class of <code>Book</code>. The compiler checks that the method exists on the declared class type, not the run-time type of the object.
   :feedback_c: I is correct because variable <code>b</code> has been declared to be an object of the class <code>Book</code> so you can invoke any public methods that are defined in the <code>Book</code> class or in parents of <code>Book</code>. II is not correct because you can't invoke methods in the <code>Dictionary</code> class directly on <code>b</code> since <code>b</code> is declared to be of type <code>Book</code> not type <code>Dictionary</code> and <code>Dictionary</code> is a subclass of <code>Book</code> not a parent class of <code>Book</code>. III is correct because you can cast <code>b</code> to type <code>Dictionary</code> and then invoke public methods in <code>Dictionary</code>.
   :feedback_d: I is also correct.
   :feedback_e: You can't invoke methods in the <code>Dictionary</code> class directly on <code>b</code> since <code>b</code> is declared to be of type <code>Book</code> not type <code>Dictionary</code> and <code>Dictionary</code> is a subclass of <code>Book</code> not a parent class of <code>Book</code>. The compiler checks that the method exists on the declared class, not the run-time class.

   Given the following class declarations and code, what is the result when the code is run?

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
         public String getDefinition(String word)
         {
            // implementation not shown
         }

         // constructors, fields, and methods not shown
      }

      Assume that the following declaration appears in a client class.

      Book b = new Dictionary();

      Which of the following statements would compile without error?
      I.  b.getISBN();
      II. b.getDefinition("wonderful");
      III. ((Dictionary) b).getDefinition("wonderful");