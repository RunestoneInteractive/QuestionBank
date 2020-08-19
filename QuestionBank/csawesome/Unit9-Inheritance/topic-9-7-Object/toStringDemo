.. activecode:: toStringDemo
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-7-Object
  :topics: Unit9-Inheritance/topic-9-7-Object
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.2
  :total_students_attempting: 5
  :num_students_correct: 3.0
  :mean_clicks_to_correct: 1.6666666667

  After trying the code below, complete the subclass called APStudent that extends Student with a new attribute called APscore and override the toString() method to call the superclass method and then add on the APscore. Uncomment the APStudent object in the main method to test it.
  ~~~~
  public class Person
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
       public static void main(String[] args)
       {
          Person p = new Person("Sila");
          Student s = new Student("Tully", 1001);
          System.out.println(p); //call Person toString
          System.out.println(s);  //call Student toString
          // Uncomment the code below to test the APStudent class
          /*
          APStudent ap = new APStudent("Ayanna", 1002, 5);
          System.out.println(ap);
          */
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
  
    class APStudent extends Student
    {
       private int score;
       public APStudent(String name, int id, int score)
       {
          super(name, id);
          this.score = score;
       }
       // Add a toString() method here that calls the super class toString
  
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
             String expect = "Sila\nTully 1001\nAyanna 1002 5";
  
             boolean passed = getResults(expect, output, "Checking output from main()");
             assertTrue(passed);
         }
          @Test
         public void containsToString()
         {
           String code = getCode();
           String target = "public String toString()";
  
           int num = countOccurencesRegex(code, target);
           boolean passed = (num >= 3);
  
           getResults("3", ""+num, "3 toString methods", passed);
           assertTrue(passed);
         }
     }