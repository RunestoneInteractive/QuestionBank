.. activecode:: ObjEquals
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-7-Object
   :topics: Unit9-Inheritance/topic-9-7-Object
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.0

   Try to guess what this code will print out before running it.
   ~~~~
   public class Person
   {
      private String name;
   
      public Person(String theName)
      {
         this.name = theName;
      }
   
      public static void main(String[] args)
      {
         Person p1 = new Person("Kairen");
         Person p2 = new Person("Jewel");
         Person p3 = new Person("Kairen");
         Person p4 = p3;
         System.out.println(p1.equals(p2));
         System.out.println(p2.equals(p3));
         System.out.println(p1.equals(p3));
         System.out.println(p3.equals(p4));
   
      }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         public RunestoneTests() {
             super("Person");
         }
   
         @Test
         public void test1()
         {
             String output = getMethodOutput("main");
             String expect = "false\nfalse\nfalse\ntrue";
   
             boolean passed = getResults(expect, output, "Checking output from main()", true);
             assertTrue(passed);
   
         }
     }