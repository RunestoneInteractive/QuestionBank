.. activecode:: StudentArrayList
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit7-ArrayList
  :subchapter: topic-7-2-arraylist-methods
  :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 19
  :num_students_correct: 19.0
  :mean_clicks_to_correct: 1.0

  An example of an ArrayList of Student objects. Add a new student with your name and info in it.
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
        public RunestoneTests() {
            super("StudentList");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[123456: Skyler, skyler@sky.com, 789012: Ayanna, ayanna@gmail.com]";
  
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }