.. activecode:: code5_4_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit5-Writing-Methods
    :subchapter: topic-5-4-comments
    :topics: Unit5-Writing-Methods/topic-5-4-comments
    :from_source: T
    :language: java
    :autograde: unittest

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