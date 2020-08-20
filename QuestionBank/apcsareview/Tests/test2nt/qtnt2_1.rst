.. mchoice:: qtnt2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II only
   :answer_e: II and III only
   :correct: e
   :feedback_a: A Fish is NOT a type of Goldfish. The Fish class does not inherit from the Goldfish class, so a Fish cannot be instantiated as a Goldfish object.
   :feedback_b: II is correct, but III is correct as well. A Goldfish IS-A type of Fish, and a Fish IS-A type of Animal.
   :feedback_c: III is correct, but II is correct as well. A Goldfish IS-A type of Fish, and a Fish IS-A type of Animal.
   :feedback_d: II is correct, but a Fish is NOT a type of Goldfish. A Fish cannot be instantiated as a Goldfish object, because the Fish class does not inherit from the Goldfish class.
   :feedback_e: A Goldfish IS-A type of Fish, and a Fish IS-A type of Animal. The Goldfish class inherits from the Fish class, and the Fish class inherits from the Animal class.

   Consider the ``Animal``, ``Fish``, and ``Goldfish`` classes shown below.  Which of the following object declarations will compile without error?

   .. code-block:: java

     public class Animal
     {
         /* no constructors or other methods have been declared */
     }

     public class Fish extends Animal
     {
         /* no constructors or other methods have been declared */
     }

     public class Goldfish extends Fish
     {
         /* no constructors or other methods have been declared */
     }

     I. Goldfish glub = new Fish();

     II. Animal glub = new Fish();

     III. Fish glub = new Goldfish();