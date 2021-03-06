.. mchoice:: qtnt2_16
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: Vroom vroom! Let's go!
   :answer_b: Vroom vroom!
   :answer_c: Let's go!
   :answer_d: Let's go! Vroom vroom!
   :answer_e: This would result in a compile-time error.
   :correct: a
   :feedback_a: The method drive has been overwritten in the Minivan class. Since obj is of type Minivan, the compiler will use the overwritten method. The overwritten method uses super() to call to the method of the parent class, so "Vroom vroom! " is printed. Then, the overwritten method prints out "Let's go! ".
   :feedback_b: Although the overwritten method has a call to the method in the parent class, there is another line of code that must be printed. The drive method has been overwritten for the Minivan class.
   :feedback_c: This would be the case if the overwritten method did not make a call to the class in the parent class. Because the method has a call to the parent class before it does anything else, "Vroom vroom! " is printed.
   :feedback_d: This would be the case if the parent method had been called after "Let's go! " had been printed.
   :feedback_e: This code correctly compiles, so there are no errors present. The Minivan class can make a call to a method in the Car class using super, because the Minivan class extends the Car class.


   Consider the classes ``Car`` and ``Minivan``, shown below. If ``obj`` has been instantiated later in the class as a ``Minivan``, what is printed as a result of ``obj.drive()``?

   .. code-block:: java

      public class Car
      {
         public void drive()
         {
            System.out.print("Vroom vroom! ");
         }
      }

      public class Minivan extends Car
      {
         public void drive()
         {
            super.drive();
            System.out.print(" Let's go! ");
         }
      }