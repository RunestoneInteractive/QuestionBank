.. activecode:: substring-preconditions
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit5-Writing-Classes
    :subchapter: topic-5-3-comments-conditions
    :topics: Unit5-Writing-Classes/topic-5-3-comments-conditions
    :from_source: T
    :language: java
    :autograde: unittest
    :pct_on_first: 0.2756756757
    :total_students_attempting: 185
    :num_students_correct: 158.0
    :mean_clicks_to_correct: 2.7848101266

    The following code breaks the preconditions of the substring method and throws an IndexOutOfBoundsException. Can you fix the code by changing the arguments for the substring method to print out the substring "lo"? What are the preconditions for the substring method?
    ~~~~
    public class SubstringPreconditions
    {
      public static void main(String[] args)
      {
          String str = "hello";
          System.out.println( str.substring(-1,10) );
      }
    }
    ====
    // Test for Lesson 5.3.2 Substring-preconditions
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("SubstringPreconditions");
        }
    
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "lo";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }