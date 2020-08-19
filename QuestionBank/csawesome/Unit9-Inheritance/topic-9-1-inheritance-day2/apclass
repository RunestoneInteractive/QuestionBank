.. activecode:: apclass
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-1-inheritance-day2
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day2
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.9230769231
  :total_students_attempting: 13
  :num_students_correct: 12.0
  :mean_clicks_to_correct: 1.0

  What do you think the following code will print out?
  ~~~~
  import java.util.*;
  
    class Student
    {
      private String name;
      private int id;
    }
  
    class Course
    {
      private String title;
      private ArrayList<Student> roster;
    }
  
    public class APcourse extends Course
    {
       private String APexamDate;
  
       public static void main(String[] args)
       {
          APcourse csa = new APcourse();
          System.out.print("Is an APcourse a Course? ");
          System.out.println(csa instanceof Course);
       }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Is an APcourse a Course? true\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
    }