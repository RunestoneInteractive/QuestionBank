.. activecode:: challenge-5-6-song
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-6-writing-methods
  :topics: Unit5-Writing-Classes/topic-5-6-writing-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.1333333333
  :total_students_attempting: 120
  :num_students_correct: 54.0
  :mean_clicks_to_correct: 3.2962962963

  Create method(s) with parameters to print out verses of the song The Ants Go Marching. https://www.lyrics.com/lyric/5526512/The+Ants+Go+Marching
  ~~~~
  public class Song
  {
     // Create at least 1 method called verse that takes 2 parameters
     // that can be used to print out the verses of the song The Ants Go Marching
  
  
     public static void main(String args[])
     {
         // Create a Song object and call its method(s) to print out
         // the verses of The Ants Go Marching
         // There should be atleast 1 method called verse that takes 2 arguments.
  
  
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
        boolean passed = checkCodeContains("verse method call with 2 arguments for verse 1", "verse(\"one\", \"suck his thumb\"");
        assertTrue(passed);
      }
  
      @Test
      public void checkCodeContains2(){
         //check verse 2
          boolean passed = checkCodeContains("verse method call with 2 arguments for verse 2", "verse(\"two\", \"tie his shoe\"");
        assertTrue(passed);
      }
  
      @Test
      public void checkCodeContains3(){
         //check verse 3
          boolean passed = checkCodeContains("verse method call with 2 arguments for verse 3", "verse(\"three\", \"climb a tree\"");
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
    }