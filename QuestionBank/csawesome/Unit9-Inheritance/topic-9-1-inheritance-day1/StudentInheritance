.. activecode:: StudentInheritance
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-1-inheritance-day1
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day1
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.8181818182
  :total_students_attempting: 11
  :num_students_correct: 9.0
  :mean_clicks_to_correct: 1.0

  What do you need to add to the Student class declaration below to make it inherit from type Person? When you fix the code, the **instanceof** operator will return true that Student s is an instance of both the Student and the Person class. What other private instance variables could you add to Person and Student? In which class would you put an address attribute? Where would you put gpa?
  ~~~~
  class Person
  {
       private String name;
  }
  
  // How can we make the Student class inherit from class Person?
  public class Student
  {
       private int id;
  
       public static void main(String[] args)
       {
          Student s = new Student();
          System.out.println(s instanceof Student);
          System.out.println(s instanceof Person);
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
            String expect = "true\ntrue";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void containsExtends()
        {
           boolean passed = checkCodeContains("Student extends Person");
           assertTrue(passed);
        }
    }