.. activecode:: StudentObjExample2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-5-mutator-methods
  :topics: Unit5-Writing-Classes/topic-5-5-mutator-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.9174311927
  :total_students_attempting: 109
  :num_students_correct: 104.0
  :mean_clicks_to_correct: 1.1442307692

  Fix the main method to include a call to the appropriate set method.
  ~~~~
  public class TesterClass
  {
     // main method for testing
     public static void main(String[] args)
     {
        Student s1 = new Student("Skyler", "skyler@sky.com", 123456);
        System.out.println(s1);
        s1.setName("Skyler 2");
        // Main doesn't have access to email, use set method!
        s1.email = "skyler2@gmail.com";
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
     // mutator methods - setters
     public void setName(String newName)
     {
       name = newName;
     }
     public void setEmail(String newEmail)
     {
       email = newEmail;
     }
     public void setId(int newId)
     {
       id = newId;
     }
     // accessor methods - getters
     public String getName()
     {
        return name;
     }
     public String getEmail()
     {
        return email;
     }
     public int getId()
     {
        return id;
     }
     public String toString() {
        return id + ": " + name + ", " + email;
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
        public void test1()
        {
            String target = "s1.setEmail(\"skyler2@gmail.com\");";
            boolean passed = checkCodeContains("call to setEmail()", target);
            assertTrue(passed);
        }
  
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "123456: Skyler, skyler@sky.com\n123456: Skyler 2, skyler2@gmail.com";
  
            boolean passed = getResults(expect, output, "Checking main()", true);
            assertTrue(passed);
        }
    }