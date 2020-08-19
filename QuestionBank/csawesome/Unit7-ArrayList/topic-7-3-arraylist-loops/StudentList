.. activecode:: StudentList
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit7-ArrayList
  :subchapter: topic-7-3-arraylist-loops
  :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.6666666667
  :total_students_attempting: 15
  :num_students_correct: 13.0
  :mean_clicks_to_correct: 1.2307692308

  Add a for each loop that prints out each student and then a new line.
  ~~~~
  import java.util.*;
  
  public class StudentList
  {
     // main method for testing
     public static void main(String[] args)
     {
        ArrayList<Student> roster = new ArrayList<Student>();
        roster.add(new Student("Skyler", "skyler@sky.com", 123456));
        roster.add(new Student("Ayanna", "ayanna@gmail.com", 789012));
        // Replace this with a for each loop that prints out each student on a separate line
        System.out.println(roster);
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
            String expect = "123456: Skyler, skyler@sky.com\n789012: Ayanna, ayanna@gmail.com";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
         @Test
        public void loopCode()
        {
          boolean passed = checkCodeContains("for loop", "for");
          assertTrue(passed);
        }
    }