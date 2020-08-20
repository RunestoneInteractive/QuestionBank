.. activecode::  ooEx11q
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
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.0

   Override the compareTo method so that it returns a postive number if the current Person is older than the passed other and a negative number if they are younger. If their age is the same then return the compareTo result on the names.
   ~~~~
   public class Person implements Comparable<Person>
   {
       private String name;
       private int age;
   
       public Person(String name, int age)
       {
           this.name = name;
           this.age = age;
       }
   
       public int compareTo(Person other)
       {
           // ADD CODE HERE
       }
   
       public static void main(String[] args)
       {
           Person p1 = new Person("Carlos",17);
           Person p2 = new Person("Lia",18);
           Person p3 = new Person("Asraf", 17);
           Person p4 = new Person("Lia", 17);
           Person p5 = new Person("Karla", 17);
           System.out.println(p1.compareTo(p2));
           System.out.println(p2.compareTo(p3));
           System.out.println(p3.compareTo(p1));
           System.out.println(p4.compareTo(p3));
           System.out.println(p4.compareTo(p5));
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
        String expect = "-1\n1\n-2\n11\n1\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        Person p1 = new Person("Carlos",17);
        Person p2 = new Person("Lia",18);
        String output = String.valueOf(p1.compareTo(p2));
        String expect = "-1";
   
        boolean passed = getResults(expect, output, "test1: compareTo method, ages different");
   
        assertTrue(passed);
      }
   
      @Test
      public void test2()
      {
        Person p2 = new Person("Lia",18);
        Person p3 = new Person("Asraf", 17);
        String output = String.valueOf(p2.compareTo(p3));
        String expect = "1";
   
        boolean passed = getResults(expect, output, "test2: compareTo method, ages different");
   
        assertTrue(passed);
      }
   
      @Test
      public void test3()
      {
        Person p4 = new Person("Lia", 17);
        Person p5 = new Person("Karla", 17);
   
        String output = String.valueOf(p4.compareTo(p5));
        String expect = "1";
   
        boolean passed = getResults(expect, output, "test2: compareTo method, ages same");
         assertTrue(passed);
      }
    }