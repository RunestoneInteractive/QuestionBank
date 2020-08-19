.. activecode:: PersonClassThis
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-9-this
  :topics: Unit5-Writing-Classes/topic-5-9-this
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 121
  :num_students_correct: 121.0
  :mean_clicks_to_correct: 1.0

  Observe the use of the keyword this in the code below. Click on the CodeLens button and then forward to see the memory in action.
  ~~~~
  public class Person
  {
     // instance variables
      private String name;
      private String email;
      private String phoneNumber;
  
     // constructor
     public Person(String theName)
     {
        this.name = theName;
     }
  
     // accessor methods - getters
     public String getName() { return this.name;}
     public String getEmail() { return this.email;}
     public String getPhoneNumber() { return this.phoneNumber;}
  
     // mutator methods - setters
     public void setName(String theName) { this.name = theName;}
     public void setEmail(String theEmail) {this.email = theEmail;}
     public void setPhoneNumber(String thePhoneNumber) { this.phoneNumber = thePhoneNumber;}
     public String toString()
     {
        return this.name + " " + this.email + " " + this.phoneNumber;
     }
  
     // main method for testing
     public static void main(String[] args)
     {
        Person p1 = new Person("Sana");
        System.out.println(p1);
        Person p2 = new Person("Jean");
        p2.setEmail("jean@gmail.com");
        p2.setPhoneNumber("404 899-9955");
        System.out.println(p2);
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
            public void testMain() throws IOException
            {
               String output = getMethodOutput("main");
                String expect = "Sana null null\nJean jean@gmail.com 404 899-9955";
  
                boolean passed = getResults(expect, output, "Expected output from main", true);
                assertTrue(passed);
            }
      }