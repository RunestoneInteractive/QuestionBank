.. activecode:: FarmerVerse
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

  A refrain is similar to a chorus, although usually shorter in length such as a single line that gets repeated.
  Add a method named "refrain" to reduce redundancy in the following code.
  You should update the main method to call the new method.
  ~~~~
  public class FarmerSong
  {

    public static void main(String args[])
    {
       System.out.println("The farmer in the dell");
       System.out.println("The farmer in the dell");
       System.out.println("Heigh ho the derry-o");
       System.out.println("The farmer in the dell");
    }

  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testSignature(){
          int count = countOccurences(getCode(),"public static void refrain()");
          boolean passed = count == 1;
          passed = getResults("1 refrain signature",  count  + " refrain signature", "Is your refrain method signature correct?", passed);
          assertTrue(passed);
        }

        @Test
        public void testcodeContains(){
          int count = countOccurences(getCode(),"refrain();");
          boolean passed = count == 3;
          passed = getResults("3 refrain calls",  count  + " refrain calls", "Added enough calls to refrain?", passed);
          assertTrue(passed);
        }

    }