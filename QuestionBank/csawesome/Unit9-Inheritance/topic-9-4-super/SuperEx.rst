.. activecode:: SuperEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-4-super
   :topics: Unit9-Inheritance/topic-9-4-super
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 6
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 2.3333333333

   Add another subclass called Vegan that inherits from the Student class. Add a Vegan contructor that takes a name as an argument and passes it to the super constructor. Override the getFood() method in Vegan to call the superclass getFood() but add a "No " in front of it and then say "but " and add a vegan food. Change Javier to a Vegan object in main() and try it out!
   ~~~~
   public class Person
   {
         private String name = null;
   
         public Person(String theName)
         {
            name = theName;
         }
   
         public String getFood()
         {
            return "Hamburger";
         }
   
         public static void main(String[] args)
         {
            Person p = new Student("Javier");
            System.out.println(p.getFood());
         }
      }
   
      class Student extends Person
      {
         private int id;
         private static int nextId = 0;
   
         public Student(String theName)
         {
           super(theName);
           id = nextId;
           nextId++;
         }
   
         public String getFood()
         {
            String output = super.getFood();
            return output + " and Pizza";
         }
   
         public int getId() {return this.id;}
         public void setId (int theId)
         {
            this.id = theId;
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
            public RunestoneTests(){
              super("Person");
            }
   
            @Test
            public void testMain() throws IOException
            {
              String output = getMethodOutput("main");
   
              String expect = "No Hamburger and Pizza but * \n";
   
              boolean passed = getResults(expect, output, "Expected output from main");
              assertTrue(passed);
            }
   
            @Test
            public void test1()
            {
              String target = "No \" + super.getFood()";
              boolean passed = checkCodeContains("\"No \" + super.getFood() called in Vegan class",  target);
              assertTrue(passed);
            }
          }