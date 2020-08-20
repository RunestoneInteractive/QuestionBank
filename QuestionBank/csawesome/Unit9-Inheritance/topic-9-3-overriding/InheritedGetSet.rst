.. activecode:: InheritedGetSet
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-3-overriding
  :topics: Unit9-Inheritance/topic-9-3-overriding
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 10
  :num_students_correct: 10.0
  :mean_clicks_to_correct: 1.0

  Demonstrated inherited get/set methods.
  ~~~~
  class Person
  {
     private String name;
  
     public String getName()
     {
        return name;
     }
  
     public boolean setName(String theNewName)
     {
        if (theNewName != null)
        {
           this.name = theNewName;
           return true;
        }
        return false;
     }
  }
  
  public class Employee extends Person
  {
  
     private static int nextId = 1;
     private int id;
  
     public Employee()
     {
        id = nextId;
        nextId++;
     }
  
     public int getId()
     {
        return id;
     }
  
     public static void main(String[] args)
     {
        Employee emp = new Employee();
        emp.setName("Dina");
        System.out.println(emp.getName());
        System.out.println(emp.getId());
     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
      public RunestoneTests(){
        super("Employee");
      }
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Dina\n1";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }