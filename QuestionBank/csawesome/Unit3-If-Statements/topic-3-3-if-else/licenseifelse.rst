.. activecode:: licenseifelse
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.0675675676
   :total_students_attempting: 222
   :num_students_correct: 199.0
   :mean_clicks_to_correct: 2.7537688442

   Run the following code to see what it prints out when the variable age is set to the value 16. Change the variable age's value to 15 and then run it again to see the result of the print statement in the else part.
   Can you change the if-statement to indicate that you can get a license at age 15 instead of 16? Use 2 test cases for the value of age to test your code to see the results of both print statements.
   ~~~~
   public class DriversLicenseTest
   {
      public static void main(String[] args)
      {
        int age = 16;
        if (age >= 16)
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
           String target = "age >= 15";
           boolean passed = checkCodeContains("check age >= 15", target);
           assertTrue(passed);
       }
    }