.. activecode:: StudentToString
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-4-accessor-methods
  :topics: Unit5-Writing-Classes/topic-5-4-accessor-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 226
  :num_students_correct: 226.0
  :mean_clicks_to_correct: 1.0

  See the toString() method in action.
  ~~~~
  public class TesterClass
  {
     // main method for testing
     public static void main(String[] args)
     {
        Student s1 = new Student("Skyler", "skyler@sky.com", 123456);
        System.out.println(s1);
     }
   }
  
  class Student
  {
     private String name;
     private String email;
     private int id;
  
     public Student(String initName, String initEmail, int initId)
     {
        name = initName;
        email = initEmail;
        id = initId;
     }
  
     // toString() method
     public String toString()
     {
       return id + ": " + name + ", " + email;
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
            String output = getMethodOutput("main");
            String expect = "123456: Skyler, skyler@sky.com";
            boolean passed = getResults(expect, output, "Checking for expected output", true);
            assertTrue(passed);
        }
    }