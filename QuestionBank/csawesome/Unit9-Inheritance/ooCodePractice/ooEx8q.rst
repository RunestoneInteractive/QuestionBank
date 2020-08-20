.. activecode::  ooEx8q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Finish the Teacher constructor.  Use super to use the Person construtor to set the fields inherited from Person.  It should print ``Destini 20`` followed by ``Erica 55 Masters in Teaching``.
   ~~~~
   public class Person
   {
       private String name;
       private int age;
   
       public Person(String name, int age)
       {
           this.name = name;
           this.age = age;
       }
   
       public String getName() { return this.name; }
   
       public int getAge() { return this.age; }
   
       public String toString()
       {
           return getName() + " " + getAge();
       }
   
       public static void main(String[] args)
       {
          Person p = new Person("Destini", 20);
          System.out.println(p);
          Teacher p2 = new Teacher("Erica", 55, "Masters in Teaching");
          System.out.println(p2);
       }
   }
   
   class Teacher extends Person
   {
       String degree;
   
       public String getDegree() { return this.degree; }
   
       public String toString()
       {
           return getName() + " " + getAge() + " " + getDegree();
       }
   
       public Teacher(String name, int age, String theDegree)
       {
           // ADD CODE HERE
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.List;
    import java.util.ArrayList;
   
    public class RunestoneTests extends CodeTestHelper
    {
   
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Destini 20\n" +
                        "Erica 55 Masters in Teaching\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        Teacher p2 = new Teacher("Erica", 55, "Masters in Teaching");
   
        String output = p2.toString();
        String expect = "Erica 55 Masters in Teaching";
   
        boolean passed = getResults(output, expect, "Teacher class extends Person class");
        assertTrue(passed);
      }
    }