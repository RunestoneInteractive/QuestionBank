.. activecode:: challenge1-4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.5553522415
   :total_students_attempting: 1093
   :num_students_correct: 939.0
   :mean_clicks_to_correct: 2.0436634718

   Calculate your age and your pet's age from the birthdates, and then your pet's age in dog years.
   ~~~~
   public class Challenge1_4
   {
      public static void main(String[] args)
      {
          // Fill in values for these variables
          int currentYear =
          int birthYear =
          int dogBirthYear =
   
          // Write a formula to calculate your age
          // from the currentYear and your birthYear variables
          int age =
   
          // Write a formula to calculate your dog's age
          // from the currentYear and dogBirthYear variables
          int dogAge =
   
          // Calculate the age of your dog in dogYears (7 times your dog's age in human years)
          int dogYearsAge =
   
          // Print out your age, your dog's age, and your dog's age in dog years. Make sure you print out text too so that the user knows what is being printed out.
   
   
   
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    public class RunestoneTests extends CodeTestHelper
    {
       @Test
       public void testAsgn1() throws IOException
       {
           String target = "age = currentYear - birthYear";
           boolean passed = checkCodeContains("formula for age", target);
           assertTrue(passed);
       }
       @Test
       public void testAsgn2() throws IOException
       {
           String target = "dogAge = currentYear - dogBirthYear";
           boolean passed = checkCodeContains("formula for dogAge", target);
           assertTrue(passed);
       }
       @Test
       public void testAsgn3() throws IOException
       {
           String target1 = removeSpaces("dogYearsAge = dogAge * 7");
           String target2 = removeSpaces("dogYearsAge = 7 * dogAge");
           String code = removeSpaces(getCode());
   
           boolean passed1 = code.contains(target1);
           boolean passed2 = code.contains(target2);
           boolean passed = passed1 || passed2;
           getResults("true", ""+passed, "formula for dogYearsAge using dogAge", passed);
           assertTrue(passed);
       }
    }