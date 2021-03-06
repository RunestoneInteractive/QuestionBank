.. activecode:: code6_1_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-1-parts-of-class
  :topics: Unit6-Writing-Classes/topic-6-1-parts-of-class
  :from_source: T
  :language: java
  :autograde: unittest

  Run the following class. Try changing the Person p2 object in main to your name.
  ~~~~
  public class Person
  {
     // instance variables
     private String name;
     private String email;
     private String phoneNumber;

     // constructor: construct a Person copying in the data into the instance variables
     public Person(String initName, String initEmail, String initPhone)
     {
        name = initName;
        email = initEmail;
        phoneNumber = initPhone;
     }

     // Print all the data for a person
     public void print()
     {
       System.out.println("Name: " + name);
       System.out.println("Email: " + email);
       System.out.println("Phone Number: " + phoneNumber);
     }

     // main method for testing
     public static void main(String[] args)
     {
        // call the constructor to create a new person
        Person p1 = new Person("Sana", "sana@gmail.com", "123-456-7890");
        // call p1's print method
        p1.print();
        Person p2 = new Person("Jean", "jean@gmail.com", "404 899-9955");
        p2.print();
     }
  }

  ====
  // Test for Lesson 5.1.0 - Person class - should pass if/when they run code
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {
        @Test
        public void testMain() throws IOException
        {
           String output = getMethodOutput("main");
            String expect = "Name: Sana\nEmail: sana@gmail.com\nPhone Number: 123-456-7890\nName: Jean\nEmail: jean@gmail.com\nPhone Number: 404 899-9955";

            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
  }