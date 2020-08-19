.. activecode:: code3_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :stdin: 16

   Run the following code to see what it prints out when the variable age is set to the value 18.
   Change the input value to 18 and then run it again to see the result of the print
   statement in the else part.
   Can you change the if-statement to indicate that you can get a license at age 16 instead of 18?
   Use 2 test cases for the value of age to test your code to see the results of both print statements.
   ~~~~

   import java.util.Scanner;
   public class DriversTest
   {
      public static void main(String[] args)
      {
        Scanner scan = new Scanner(System.in);
        int age = scan.nextInt();
        if (age >= 18)
        {
            System.out.println("You can get a driver's license in most states!");
        }
        else
        {
            System.out.println("Sorry, you need to be older to get a driver's license.");
        }
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
       @Test
       public void testCodeContains() throws IOException
       {
           String target = "age >= 16";
           boolean passed = checkCodeContains("check age >= 16", target);
           assertTrue(passed);
       }
    }