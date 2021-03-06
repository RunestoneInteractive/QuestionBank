.. mchoice:: songMethods
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-3-methods-no-params
   :topics: Unit2-Using-Objects/topic-2-3-methods-no-params
   :from_source: F
   :practice: T
   :answer_a: I like to eat eat eat.
   :answer_b: I like to eat eat eat fruit.
   :answer_c: I like to apples and bananas eat.
   :answer_d: I like to eat eat eat apples and bananas!
   :answer_e: Nothing, it does not compile.
   :correct: d
   :feedback_a: Try tracing through the print method and see what happens when it calls the other methods.
   :feedback_b: There is a fruit() method but it does not print out the word fruit.
   :feedback_c: The order things are printed out depends on the order in which they are called from the print method.
   :feedback_d: Yes, the print method calls the eat method 3 times and then the fruit method to print this.
   :feedback_e: Try the code in an active code window to see that it does work.

   What does the following code print out?

   .. code-block:: java

      public class Song
      {
        public void print()
        {
            System.out.print("I like to ");
            eat();
            eat();
            eat();
            fruit();
        }

        public void fruit()
        {
            System.out.println("apples and bananas!");
        }

        public void eat()
        {
           System.out.print("eat ");
        }

        public static void main(String[] args)
        {
           Song s = new Song();
           s.print();
        }
    }