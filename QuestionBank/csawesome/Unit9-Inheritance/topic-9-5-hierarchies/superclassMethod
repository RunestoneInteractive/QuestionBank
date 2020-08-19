.. activecode:: superclassMethod
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-5-hierarchies
  :topics: Unit9-Inheritance/topic-9-5-hierarchies
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 8
  :num_students_correct: 8.0
  :mean_clicks_to_correct: 1.0

  Which toString() method is called below? What would happen if you commented out the Student toString() method? Which one would be called now?
  ~~~~
  public class Tester
  {
       // This will implicitly call the toString() method of object p
       public void print(Person p)
       {
          System.out.println(p);
       }
       public static void main(String[] args)
       {
          Person p = new Person("Sila");
          Student s = new Student("Tully", 1001);
          Tester t = new Tester();
          t.print(p); //call print with a Person
          t.print(s); //call print with a Student
       }
    }
  
    class Person
    {
       private String name;
       public Person(String name)
       {
          this.name = name;
       }
       public String toString()
       {
          return name;
       }
    }
  
    class Student extends Person
    {
       private int id;
       public Student(String name, int id)
       {
          super(name);
          this.id = id;
       }
       public String toString()
       {
          return super.toString() + " " + id;
       }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Tester");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Sila\nTully 1001";
  
            boolean passed = getResults(expect, output, "Running main", true);
            assertTrue(passed);
  
        }
    }