.. activecode:: challenge-5-5-Pet-Class
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-5-mutator-methods
  :topics: Unit5-Writing-Classes/topic-5-5-mutator-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.1794871795
  :total_students_attempting: 117
  :num_students_correct: 56.0
  :mean_clicks_to_correct: 2.7321428571

  Create a Pet class that keeps track of the name, age, weight, type of animal, and breed for records at an animal clinic with 2 constructors, accessor (get) methods, a toString method, and mutator (set) methods for each instance variable.
  ~~~~
  /**
      Pet class (complete comments)
      @author
      @since
  
  */
  class Pet
  {
     // complete class definition with set methods
  
  }
  
  public class TesterClass
  {
     // main method for testing
     public static void main(String[] args)
     {
        // Create Pet objects and test all your set methods
  
     }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
  
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests()
        {
            super("TesterClass");
        }
  
        @Test
        public void testConstructors()
        {
           changeClass("Pet");
            int count = 0;
  
            for (int i = 0; i < 6; i++) {
                if (checkConstructor(i).equals("pass"))
                    count++;
            }
  
            boolean passed = count >= 2;
  
            getResults("2+", ""+count, "Checking for 2 constructors", passed);
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariables()
        {
            changeClass("Pet");
            String expect = "5 Private";
            String output = testPrivateInstanceVariables();
  
            boolean passed = getResults(expect, output, "Checking Private Instance Variables");
            assertTrue(passed);
        }
  
        @Test
        public void test1()
        {
            String code = getCode();
            String target = "public * get*()";
  
            int num = countOccurencesRegex(code, target);
  
            boolean passed = num >= 5;
  
            getResults("5", ""+num, "Checking accessor (get) methods for each variable", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test2()
        {
            String code = getCode();
            String target = "public void set*(*)";
  
            int num = countOccurencesRegex(code, target);
  
            boolean passed = num >= 5;
  
            getResults("5", ""+num, "Checking mutator (set) methods for each variable", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test3()
        {
            String target = "public String toString()";
            boolean passed = checkCodeContains("toString() method", target);
            assertTrue(passed);
        }
  
        @Test
        public void test4()
        {
            String code = getCode();
            String target = "Pet * = new Pet(";
  
            int num = countOccurencesRegex(code, target);
  
            boolean passed = num >= 3;
  
            getResults("3", ""+num, "Checking main method creates three Pet objects", passed);
            assertTrue(passed);
        }
  
  
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
  
            String expect = "3+ line(s) of text";
            String actual = " line(s) of text";
  
            int len = output.split("\n").length;
  
            if (output.length() > 0) {
                actual = len + actual;
            } else {
                actual = output.length() + actual;
            }
            boolean passed = len >= 3;
  
            getResults(expect, actual, "Checking main method prints info for 3 Pet objects", passed);
            assertTrue(passed);
        }
    }