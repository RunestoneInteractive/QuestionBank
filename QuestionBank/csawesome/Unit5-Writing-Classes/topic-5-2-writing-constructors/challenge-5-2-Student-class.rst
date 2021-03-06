.. activecode:: challenge-5-2-Student-class
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-2-writing-constructors
  :topics: Unit5-Writing-Classes/topic-5-2-writing-constructors
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.3163265306
  :total_students_attempting: 196
  :num_students_correct: 113.0
  :mean_clicks_to_correct: 2.1150442478

  Create a class Student with 4 instance variables, 3 constructors, and a print method. Write a main method that creates 3 Student objects with the 3 different constructors and calls their print() method.
  ~~~~
  /** class Student
   * with 4 instance variables,
   * 3 constructors, a print method,
   * and a main method to test them.
   */
   public class Student
   {
       // Write 4 instance variables
  
  
       // Write 3 constructors to initialize the instance variables
       //  1. no parameters using default values
       //  2. 1 parameter and the rest default values
       //  3. 4 parameters
  
  
       // Write a print method that prints all the instance variables
       public void print()
       {
  
  
       }
  
      // main method
      public static void main(String[] args)
      {
         // Construct 3 Student objects using the 3 different constructors
  
  
         // call their print() methods
  
      }
   }
   ====
   // Test Code for Lesson 5.2.1 - Challenge - Student
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
  
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Student");
  
            Object[] values = new Object[]{"Name", 0};
            setDefaultValues(values);
        }
  
        @Test
        public void testDefaultConstructor()
        {
            String output = checkDefaultConstructor();
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking default constructor");
            assertTrue(passed);
        }
  
        @Test
        public void testConstructor4()
        {
            String output = checkConstructor(4);
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking constructor with 4 parameters");
            assertTrue(passed);
        }
  
        @Test
        public void testConstructor1()
        {
            String output = checkConstructor(1);
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking constructor with 1 parameter");
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariables()
        {
            String expect = "4 Private";
            String output = testPrivateInstanceVariables();
  
            boolean passed = getResults(expect, output, "Checking Private Instance Variable(s)");
            assertTrue(passed);
        }
  
        @Test
        public void testPrint()
        {
            String output = getMethodOutput("print");
            String expect = "More than 15 characters";
            String actual = " than 15 characters";
  
            if (output.length() < 15) {
                actual = "Less" + actual;
            } else {
                actual = "More" + actual;
            }
            boolean passed = getResults(expect, actual, "Checking print method");
            assertTrue(passed);
        }
  
  
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");//.split("\n");
            String expect = "3+ line(s) of text";
            String actual = " line(s) of text";
            int len = output.split("\n").length;
  
            if (output.length() > 0) {
                actual = len + actual;
            } else {
                actual = output.length() + actual;
            }
            boolean passed = len >= 3;
  
            getResults(expect, actual, "Checking output", passed);
            assertTrue(passed);
        }
    }