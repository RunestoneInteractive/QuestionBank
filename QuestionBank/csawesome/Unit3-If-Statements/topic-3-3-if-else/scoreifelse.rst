.. activecode:: scoreifelse
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-3-if-else
   :topics: Unit3-If-Statements/topic-3-3-if-else
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.0516431925
   :total_students_attempting: 213
   :num_students_correct: 146.0
   :mean_clicks_to_correct: 3.9931506849

   Try the following code. Add an else statement to the if statement that prints out "Good job!" if the score is greater than 9. Change the value of score to test it. Can you change the boolean test to only print out "Good job" if the score is greater than 20?
   ~~~~
   public class ScoreTest
   {
      public static void main(String[] args)
      {
          int score = 8;
          if (score <= 9)
          {
            System.out.println("Try for a higher score!");
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
            String origCode = "public class ScoreTest   {      public static void main(String[] args)      {        int score = 8;        if (score <= 9)         {            System.out.println(\"Try for a higher score!\");        }      }} ";
   
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
        @Test
        public void testCodeContainsElse(){
          boolean ifCheck2 = checkCodeContains("else", "else");
          assertTrue(ifCheck2);
        }
        @Test
        public void testCodeContains(){
            boolean ifCheck1 = checkCodeContains("if testing with 20", "if (score <= 20)");
            assertTrue(ifCheck1);
        }
    }