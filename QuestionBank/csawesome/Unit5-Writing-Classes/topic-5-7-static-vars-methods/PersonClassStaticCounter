.. activecode:: PersonClassStaticCounter
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-7-static-vars-methods
  :topics: Unit5-Writing-Classes/topic-5-7-static-vars-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.9951456311
  :total_students_attempting: 206
  :num_students_correct: 206.0
  :mean_clicks_to_correct: 1.0048543689

  What will the following code print out? Try adding another Person object and see what happens. Try the CodeLens button to run the code step by step.
  ~~~~
  public class Person
  {
     // instance variables
     private String name;
     private String email;
     private String phoneNumber;
  
     // Static counter variable
     public static int personCounter = 0;
  
     // static method to print out counter
     public static void printPersonCounter() {
          System.out.println("Person counter: " + personCounter);
     }
  
     // constructor: construct a Person copying in the data into the instance variables
     public Person(String initName, String initEmail, String initPhone)
     {
        name = initName;
        email = initEmail;
        phoneNumber = initPhone;
        personCounter++;
     }
  
     // toString() method
     public String toString()
     {
       return  name + ": " + email + " " + phoneNumber;
     }
  
     // main method for testing
     public static void main(String[] args)
     {
         // call the constructor to create a new person
         Person p1 = new Person("Sana", "sana@gmail.com", "123-456-7890");
         Person p2 = new Person("Jean", "jean@gmail.com", "404 899-9955");
  
         Person.printPersonCounter();
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
            String expect = "Person counter: 2";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }