.. activecode:: code3_3_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :stdin: true


   Run the following code twice for each boolean value for isHeads (true and false).    Notice the program always prints "after conditional" since that statement is not nested inside the if or else blocks.

   ~~~~
   import java.util.Scanner;
   public class HeadsOrTails
   {
      public static void main(String[] args)
      {
        Scanner scan = new Scanner(System.in);

        boolean isHeads = scan.nextBoolean();
        if (isHeads)
        {
            System.out.println("Let's go to the game");
        }
        else
        {
            System.out.println("Let's watch a movie");
        }
        System.out.println("after conditional");
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
       public void testMain() throws IOException
       {
           boolean passed = getResults("true", "true", "main()");
           assertTrue(passed);

       }

    }