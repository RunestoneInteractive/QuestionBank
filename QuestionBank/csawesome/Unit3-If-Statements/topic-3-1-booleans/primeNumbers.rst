.. activecode:: primeNumbers
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-1-booleans
   :topics: Unit3-If-Statements/topic-3-1-booleans
   :from_source: F
   :language: java

   public class PrimeNumbers
   {
      public static void main(String[] args)
      {
        int number = 5;
        System.out.println("Is " + number + " divisible by 1 to " + number + "?");
        System.out.println(number % 1 == 0);
        System.out.println(number % 2 == 0);
        System.out.println(number % 3 == 0);
        System.out.println(number % 4 == 0);
        System.out.println(number % 5 == 0);
      }
   }