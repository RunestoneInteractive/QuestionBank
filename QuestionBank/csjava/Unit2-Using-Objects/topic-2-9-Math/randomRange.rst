.. activecode:: randomRange
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-9-Math
   :topics: Unit2-Using-Objects/topic-2-9-Math
   :from_source: F
   :language: java
   :autograde: unittest

   Run the code below several times to see how the value changes each time. How could you change the code to return a random integer from 1 to 10?  Modify the code and see if your answer is correct. Try removing the parentheses from around (Math.random() * 10) and run the code several times. What happens? The parentheses are necessary because (int) will cast the closest expression, and (int)Math.random() will always be 0 since anything after the decimal point is dropped.
   ~~~~
   public class Test4
   {
      public static void main(String[] args)
      {
        System.out.println((int) (Math.random() * 10));
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
       @Test
       public void testContainsRange() throws IOException
       {
           String target = "+ 1";
           boolean passed = checkCodeContains("Math.random in range 1 to 10", target);
           assertTrue(passed);
       }
    }