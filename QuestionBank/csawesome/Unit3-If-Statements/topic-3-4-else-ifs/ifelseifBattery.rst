.. activecode::  ifelseifBattery
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit3-If-Statements
  :subchapter: topic-3-4-else-ifs
  :topics: Unit3-If-Statements/topic-3-4-else-ifs
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.5163043478
  :total_students_attempting: 184
  :num_students_correct: 155.0
  :mean_clicks_to_correct: 1.9806451613

  Finish the following code so that it prints "Plug in your phone!" if the battery is below 50, "Unplug your phone!" if it is above 100, and "All okay!" otherwise. Change the battery value to test all 3 conditions.
  ~~~~
  public class BatteryTest
  {
      public static void main(String[] args)
      {
          int battery = 60;
  
          System.out.println("All okay!");
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
            String origCode = "public class BatteryTest {  public static void main(String[] args)  {  int battery = 60;  System.out.println(\"All okay!\");  }  }";
  
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
  
        @Test
        public void testCodeContains3(){
          boolean ifCheck1 = checkCodeContains("if statement for battery above 100", "if (battery > 100)");
            assertTrue(ifCheck1);
        }
  
        @Test
        public void testCodeContains5(){
            boolean ifCheck1 = checkCodeContains("if statement for battery less than 50", "if (battery < 50)");
            assertTrue(ifCheck1);
        }
  
        @Test
        public void testCodeContains4(){
          boolean ifCheck2 = checkCodeContains("else", "else");
          assertTrue(ifCheck2);
        }
    }