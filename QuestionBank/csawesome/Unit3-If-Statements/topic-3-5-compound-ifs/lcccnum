.. activecode:: lcccnum
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3306122449
   :total_students_attempting: 245
   :num_students_correct: 226.0
   :mean_clicks_to_correct: 1.6592920354

   Explore how && and || are used with numbers below. Try different values for score like -10 and 110 in the code below.
   ~~~~
   public class TestNum
   {
      public static void main(String[] args)
      {
        int score = 10; // Try -10 and 110
        if (score < 0 || score > 100)
        {
            System.out.println("Score has an illegal value.");
        }
        if (score >= 0 && score <= 100)
        {
            System.out.println("Score is in the range 0-100");
        }
   
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
         @Test
        public void testChangedCode() {
            String origCode = "public class TestNum{public static void main(String[] args){int score = 10;  if (score < 0 || score > 100){ System.out.println(\"Score has an illegal value.\");}if (score >= 0 && score <= 100){ System.out.println(\"Score is in the range 0-100\");}}}";
   
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }