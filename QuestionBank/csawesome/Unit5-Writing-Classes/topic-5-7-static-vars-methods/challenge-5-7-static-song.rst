.. activecode:: challenge-5-7-static-song
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-7-static-vars-methods
  :topics: Unit5-Writing-Classes/topic-5-7-static-vars-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.2235294118
  :total_students_attempting: 85
  :num_students_correct: 30.0
  :mean_clicks_to_correct: 2.0333333333

  public class Song
  {
    // Add a static verse counter variable
  
  
    // Change the method(s) to be static
  
  
  
    public static void main(String args[])
    {
      // Call the static method(s) to print out the Song
  
    }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void checkCodeContains1(){
        //check verse 1
        boolean passed = checkCodeContains("verse one method call", "verse(\"one\", \"suck his thumb\"");
        assertTrue(passed);
  
      }
  
      @Test
      public void checkCodeContains2(){
         //check verse 2
          boolean passed = checkCodeContains("verse two method call", "verse(\"two\", \"tie his shoe\"");
        assertTrue(passed);
  
      }
  
      @Test
      public void checkCodeContains3(){
         //check verse 3
          boolean passed = checkCodeContains("verse three method call", "verse(\"three\", \"climb a tree\"");
        assertTrue(passed);
  
      }
      @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "The ants go marching three by three\nThe little one stops to climb a tree";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Expected output from main contains 3 verses", passed);
            assertTrue(passed);
        }
  
      @Test
      public void checkCodeContains4(){
         //check static
         String code = getCode();
         int actual = countOccurences(code, "static void");
         String expected = "2";
  
         boolean passed = actual >= 2;
         getResults(expected, ""+actual, "Static void methods", passed);
        assertTrue(passed);
      }
      @Test
      public void checkCodeContains5(){
         //check static
         String code = getCode();
         int actual = countOccurences(code, "static int");
         String expected = "1";
  
         boolean passed = actual >= 1;
         getResults(expected, ""+actual, "Static int variable", passed);
        assertTrue(passed);
  
      }
    }