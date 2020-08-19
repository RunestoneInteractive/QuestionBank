.. activecode:: fourleafcloversong
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-1-writing-methods
  :topics: Unit5-Writing-Methods/topic-5-1-writing-methods
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  Run the following code to see the song print out.
  Notice the first line of code in the main method
  is a call to the new method ``chorus()``.
  Can you replace the last two lines in the second verse in the main
  method with another call to the ``chorus()`` method?
  Step through using on the Code Lens button to see how the main method calls the chorus method.
  ~~~~
  public class Song
  {
    // The chorus method
    public static void chorus()
    {
       System.out.println("I'm looking over a four-leaf clover");
       System.out.println("That I overlooked before");
    }

    public static void main(String args[])
    {
      chorus();
      System.out.println("One leaf is sunshine, the second is rain");
      System.out.println("Third is the roses that grow in the lane");
      System.out.println();
      System.out.println("No need explaining, the one remaining");
      System.out.println("Is somebody I adore");
      // Can you replace these 2 lines with a method call to chorus()?
      System.out.println("I'm looking over a four-leaf clover");
      System.out.println("That I overlooked before");
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
            String output = getMethodOutput("main");
            String expect = "I'm looking over a four-leaf clover\nThat I overlooked before\nOne leaf is sunshine, the second is rain\nThird is the roses that grow in the lane\n\nNo need explaining, the one remaining\nIs somebody I adore\nI'm looking over a four-leaf clover\nThat I overlooked before";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }

        @Test
        public void testcodeContains(){
          int count = countOccurences(getCode(),"chorus();");
          boolean passed = count > 1;
          passed = getResults("> 1 chorus call",  count  + " chorus call(s)", "Added second call to chorus?", passed);
          assertTrue(passed);
        }

    }