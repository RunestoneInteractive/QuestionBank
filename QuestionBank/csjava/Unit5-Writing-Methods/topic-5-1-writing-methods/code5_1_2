.. activecode:: code5_1_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-1-writing-methods
  :topics: Unit5-Writing-Methods/topic-5-1-writing-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T

  A refrain is similar to a chorus, although usually shorter in length such as a single line that gets repeated.
  In the song below, the refrain is "The farmer in the dell".
  Add a method named "refrain" and update the main method to call the new method 3 times.  Run your program to ensure the output is correct.
  ~~~~
  public class FarmerSong
  {

    //add your new method here



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