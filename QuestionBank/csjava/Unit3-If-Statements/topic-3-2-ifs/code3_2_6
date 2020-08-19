.. activecode:: code3_2_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :stdin: true

   The code below doesn't work as expected. It has 2 errors.
   Run the program with input true, then change the input to false and run again.
   Even when the input is false, the program still prints both messages.
   Fix it to only print both "Wear a coat" and "Wear gloves" when isCold is true.
   Nothing should print when isCold is false.

   ~~~~
   import java.util.Scanner;
   public class TestCold
   {
      public static void main(String[] args)
      {
        Scanner scan = new Scanner(System.in);

        System.out.println("Is it cold?");
        boolean isCold = scan.nextBoolean();

        if (isCold);
            System.out.println("Wear a coat");
            System.out.println("Wear gloves");

      }
   }
   ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {

        @Test
        public void testsemicolon()
        {
            String code = getCode();
            int num = countOccurences(code, "isCold);");
            boolean passed = num == 0;

            getResults("0", "" + num, "if (isCold);  get rid of semicolon", passed);
            assertTrue(passed);
        }

        @Test
        public void testCountCurlies()
        {
            String code = getCode();
            int num = countOccurences(code, "{");
            boolean passed = num >= 3;

            getResults("3", "" + num, "Number of {", passed);
            assertTrue(passed);
        }
    }