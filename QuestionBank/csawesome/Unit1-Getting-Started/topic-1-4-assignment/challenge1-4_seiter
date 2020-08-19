.. activecode:: challenge1-4_seiter
   :author: Linda Seiter
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6666666667
   :total_students_attempting: 9
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 1.625

   Calculate your age and your pet's age from the birthdates, and then your pet's age in dog years.
   Add another variable `myDogYearsAge` to calculate and print your age in dog years, 
   i.e. your age multiplied by 7.
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
   
         // Declare and assign a new variable myDogYearsAge to calculate your age in dogYears (7 times your age in human years)
         
   
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
            String target1 = "dogYearsAge = dogAge * 7";
            String target2 = "dogYearsAge = 7 * dogAge";
            boolean passed =
       checkCodeContainsNoRegex("formula for dogYearsAge using dogAge", target1) || checkCodeContainsNoRegex("formula for dogYearsAge using dogAge in another order", target2);
            assertTrue(passed);
       }
   
       @Test
       public void testAsgn4() throws IOException
       {
            String target1 = "myDogYearsAge = age * 7";
            String target2 = "myDogYearsAge = 7 * age";
            boolean passed =
       checkCodeContainsNoRegex("formula for mDogYearsAge using age", target1) || checkCodeContainsNoRegex("formula for myDogYearsAge using age in another order", target2);
            assertTrue(passed);
       }
   
   
    }