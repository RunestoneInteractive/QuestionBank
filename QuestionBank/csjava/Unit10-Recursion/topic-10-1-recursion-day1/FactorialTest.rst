.. activecode:: FactorialTest
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :language: java

   Run the code below to test the factorial method. What's the factorial of 6? Add another test to print out the factorial of 6. What's the factorial of 1? Add another test to print out the factorial of 1.
   ~~~~
   public class FactorialTest
   {

       public static int factorial(int n)
       {
           if (n == 0)
               return 1;
           else
               return n * factorial(n-1);
       }

       public static void main(String[] args)
       {
           System.out.println("factorial of 3 is: " + factorial(3));
           System.out.println("factorial of 4 is: " +factorial(4));
           System.out.println("factorial of 5 is: " +factorial(5));
       }
   }