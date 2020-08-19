.. activecode:: randomNumberInRange
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-3-method-return
  :topics: Unit5-Writing-Methods/topic-5-3-method-return
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  Write a function ``randomInteger`` that takes two integer
  parameters ``min`` and ``max`` and returns a random integer value between min and max (inclusive).
  Have the main method call the function with different values.  You might want to go back and
  review random number generation in Unit 2-9.

  ~~~~
  public class RandomNumberInRange
  {
      //add your method here

      public static void main(String args[])
      {
         //test your method by calling it

      }
  }

  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("RandomNumberInRange");
    }

    @Test
    public void checkCodeContainsSig(){
      String code = getCode();
      int num = countOccurences(code, "public static int randomInteger(int min, int max");
      boolean passed = num ==1;
      passed = getResults("1", num , "The randomInteger signature is not correct. Check your return type and the parameters", passed);
      assertTrue(passed);
    }

    @Test
    public void checkCodeContainsReturn(){
      String code = getCode();
      int num = countOccurences(code, "return");
      boolean passed = num ==1;
      passed = getResults("1", num , "The method randomInteger is missing a return statement", passed);
      assertTrue(passed);
    }

    @Test
      public void test1()
      {
          String code = getCode();
          int numRandom = countOccurences(code, "Math.random()");

          boolean passed = numRandom >= 1;
          passed = getResults("1+", ""+numRandom, "1 call to Math.random()", passed);
          assertTrue(passed);
      }

  }