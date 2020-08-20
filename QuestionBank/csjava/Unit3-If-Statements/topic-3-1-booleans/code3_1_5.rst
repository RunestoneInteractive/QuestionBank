.. activecode:: code3_1_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-1-booleans
   :topics: Unit3-If-Statements/topic-3-1-booleans
   :from_source: T
   :language: java
   :autograde: unittest

   Try to guess what the code below will print out before you run it.
   ~~~~
   public class BooleanExpressions
   {
      public static void main(String[] args)
      {
        boolean isRaining = true;
        boolean hasMoney = false;

        // Will these print true or false?
        System.out.println( isRaining );
        System.out.println( !isRaining );
        System.out.println( hasMoney );
        System.out.println( !hasMoney );
        System.out.println( 5 == 7 );
        System.out.println( !(5 == 7) );

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
            boolean passed = getResults("true", "true", "main()");
            assertTrue(passed);
        }
    }