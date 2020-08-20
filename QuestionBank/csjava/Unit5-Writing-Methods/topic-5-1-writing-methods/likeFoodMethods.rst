.. mchoice:: likeFoodMethods
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit5-Writing-Methods
   :subchapter: topic-5-1-writing-methods
   :topics: Unit5-Writing-Methods/topic-5-1-writing-methods
   :from_source: F
   :practice: T
   :answer_a: I like to eat eat eat.
   :answer_b: I like to eat eat eat fruit.
   :answer_c: I like to apples and bananas eat.
   :answer_d: I like to eat eat eat apples and bananas!
   :correct: d
   :feedback_a: Try tracing through the print method and see what happens when it calls the other methods.
   :feedback_b: There is a fruit() method but it does not print out the word fruit.
   :feedback_c: The order things are printed out depends on the order in which they are called from the print method.
   :feedback_d: Yes, the print method calls the consume method 3 times and then the fruit method to print this.

   What does the following code print out?

   .. code-block:: java

      public class LikeFood
      {

        public static void fruit()
        {
            System.out.println("apples and bananas!");
        }

        public static void consume()
        {
           System.out.print("eat ");
        }

        public static void main(String[] args)
        {
            System.out.print("I like to ");
            consume();
            consume();
            consume();
            fruit();
        }
    }