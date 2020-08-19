.. activecode:: OverrideEquals
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
   :total_students_attempting: 4
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 1.0

   Try to guess what this code will print out before running it. Click on the CodeLens button to step forward through the code and watch the memory.
   ~~~~
   public class Person
   {
      private String name;
   
      public Person(String theName)
      {
         this.name = theName;
      }
   
      /** Overriden equals method that checks if names are equal
          in this Person object and an the other Object.
          */
      public boolean equals(Object other)
      {
         // Type cast other to a Person
         Person otherPerson = (Person) other;
         // Check if names are equal
         return this.name.equals(otherPerson.name);
      }
   
      public static void main(String[] args)
      {
         Person p1 = new Person("Gabe");
         Person p2 = new Person("Gus");
         Person p3 = new Person("Gabe");
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
             String expect = "false\nfalse\ntrue\ntrue";
   
             boolean passed = getResults(expect, output, "Checking output from main()", true);
             assertTrue(passed);
   
         }
     }