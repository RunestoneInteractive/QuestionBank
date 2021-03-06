.. activecode:: challenge-5-1-Riddle-Class
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-1-parts-of-class
  :topics: Unit5-Writing-Classes/topic-5-1-parts-of-class
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.3270676692
  :total_students_attempting: 266
  :num_students_correct: 183.0
  :mean_clicks_to_correct: 2.5027322404

  Complete the Riddle class below and complete the main method to construct 2 Riddle objects and call their printQuestion() and printAnswer() methods.
  ~~~~
  public class Riddle
  {
      // write 2 instance variables for Riddle's question and answer: private type variableName;
  
  
      // constructor
      public Riddle(String initQuestion, String initAnswer)
      {
          // set the instance variables to the init parameter variables
  
      }
  
      // Print riddle question
      public void printQuestion()
      {
          // print out the riddle question with System.out.println
  
      }
  
      // Print riddle answer
      public void printAnswer()
      {
          // print out the riddle answer with System.out.println
  
      }
  
      // main method for testing
      public static void main(String[] args)
      {
          // call the constructor to create 2 new Riddle objects
  
         // call their printQuestion() and printAnswer methods
  
      }
  }
  ====
  // Test Code for Lesson 5.1.5 - Riddle
  // @author Kate McDonnell
  // Test Code for Lesson 5.1.5 - Riddle
  import static org.junit.Assert.*;
  import org.junit.*;
  
  import java.io.*;
  
  public class RunestoneTests extends CodeTestHelper
  {
        public RunestoneTests()
        {
            super("Riddle"); // class name / location of main
  
            Object[] values = new Object[]{"Question", "Answer"};
            setDefaultValues(values);
        }
  
        @Test
        public void testPrintQuestion()
        {
            String output = getMethodOutput("printQuestion");
            String expect = "Question";
  
            boolean passed = getResults(expect, output, "Checking method printQuestion()");
            assertTrue(passed);
        }
  
        @Test
        public void testPrintAnswer()
        {
            String output = getMethodOutput("printAnswer");
            String expect = "Answer";
  
            boolean passed = getResults(expect, output, "Checking method printAnswer()");
            assertTrue(passed);
        }
  
        @Test
        public void testDefaultConstructor()
        {
            String[] args = {"Question 1", "Answer 1"};
            String output = checkDefaultConstructor();
            String expect = "fail";
  
            boolean passed = getResults(expect, output, "Checking default constructor");
            assertTrue(passed);
        }
  
        @Test
        public void testConstructor()
        {
            String[] args = {"Question 1", "Answer 1"};
            String output = checkConstructor(args);
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking constructor with parameters");
            assertTrue(passed);
        }
  
        @Test
        public void testVariableTypes()
        {
            String varTypes = "String String";
            String output = testInstanceVariableTypes(varTypes.split(" "));
  
            boolean passed = getResults(varTypes, output, "Checking Instance Variable Type(s)");
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariables()
        {
            String expect = "2 Private";
            String output = testPrivateInstanceVariables();
  
            boolean passed = getResults(expect, output, "Checking Private Instance Variable(s)");
            assertTrue(passed);
        }
  
  
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
  
            String expect = "2+ line(s) of text";
            String actual = " line(s) of text";
  
            int len = output.split("\n").length;
  
            if (output.length() > 0) {
                actual = len + actual;
            } else {
                actual = output.length() + actual;
            }
            boolean passed = len >= 2;
  
            getResults(expect, actual, "Checking main method", passed);
            assertTrue(passed);
        }
    }