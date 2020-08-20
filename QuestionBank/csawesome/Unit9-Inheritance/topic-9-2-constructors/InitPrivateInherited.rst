.. activecode:: InitPrivateInherited
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-2-constructors
  :topics: Unit9-Inheritance/topic-9-2-constructors
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.3846153846
  :total_students_attempting: 13
  :num_students_correct: 8.0
  :mean_clicks_to_correct: 1.5

  Try creating another Employee object in the main method that passes in your name and then use the get methods to print it out. Which class constructor sets the name? Which class constructor sets the id?
  ~~~~
  class Person
  {
     private String name;
  
     public Person(String theName)
     {
        this.name = theName;
     }
  
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
  
     public Employee(String theName)
     {
        super(theName);
        id = nextId;
        nextId++;
     }
  
     public int getId()
     {
        return id;
     }
  
     public static void main(String[] args)
     {
        Employee emp = new Employee("Dani");
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
        public RunestoneTests() {
            super("Employee");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Dani\n#";
  
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
  
        @Test
        public void test2()
        {
            String code = getCode();
            String target = "Employee * = new Employee";
  
            int num = countOccurencesRegex(code, target);
  
            boolean passed = num >= 2;
  
            getResults("2+", "" + num, "Creating new Employee()", passed);
            assertTrue(passed);
        }
    }