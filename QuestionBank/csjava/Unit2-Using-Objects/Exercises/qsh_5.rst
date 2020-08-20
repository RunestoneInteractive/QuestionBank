.. mchoice:: qsh_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: F
   :practice: T
   :answer_a: unknown value
   :answer_b: 0
   :answer_c: compile error
   :answer_d: runtime error
   :correct: b
   :feedback_a: ints get initialized to 0 by default if not explicitly initialized.
   :feedback_b: ints get initialized to 0 by default if not explicitly initialized.
   :feedback_c: This code will compile.
   :feedback_d: someVar has a value assigned by default.

   Assume that SomeClass and MainClass are properly defined in separate files. What is the output of main()?

   .. code-block:: java

    class SomeClass
    {
        int someVar;
    }

    public class MainClass
    {
        public static void main(String[] args)
        {
            SomeClass x = new SomeClass();
            System.out.println(x.someVar);
        }
    }