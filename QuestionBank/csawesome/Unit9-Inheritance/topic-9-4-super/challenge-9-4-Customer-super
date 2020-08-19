.. activecode:: challenge-9-4-Customer-super
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
   :total_students_attempting: 4
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 2.3333333333

   Complete the OnlineCustomer class below to inherit from Customer and add an email address, a constructor, and override the toString() method.
   ~~~~
   public class Customer
   {
       private String name;
       private String address;
   
       public Customer(String n, String a)
       {
          name = n;
          address = a;
       }
   
       public String toString()
       {
          return "Name: " + name + "\nAddress: " + address;
       }
   
       public static void main(String[] args)
       {
          Customer c = new Customer("Fran Santiago", "123 Main St., Anytown, USA");
          System.out.println(c);
   
          // Uncomment these to test OnlineCustomer
          // OnlineCustomer c2 = new OnlineCustomer("Jasper Smith", "456 High St., Anytown, USA", "jsmith456@gmail.com");
          // System.out.println(c2);
       }
    }
   
    // Complete the OnlineCustomer class to inherit from Customer
    // It should have an email attribute,
    // a constructor with 3 arguments (name, address, email) that uses the super constructor,
    // and an overriden toString() method that calls the super toString() method
    //  and then prints "\nEmail:" and the email variable.
    class OnlineCustomer
    {
   
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
         String expect = "Name: Fran Santiago\n" +
                         "Address: 123 Main St., Anytown, USA\n" +
                         "Name: Jasper Smith\n" +
                         "Address: 456 High St., Anytown, USA\n" +
                         "Email: jsmith456@gmail.com";
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
        @Test
        public void containsExtends()
        {
           String target = "OnlineCustomer extends Customer";
           boolean passed = checkCodeContains(target);
           assertTrue(passed);
        }
   
       @Test
        public void test1()
        {
         String code = getCode();
         String target = "public String toString()";
   
         int num = countOccurencesRegex(code, target);
         boolean passed = (num == 2);
   
         getResults("2", ""+num, "2 toString methods", passed);
         assertTrue(passed);
       }
   
        @Test
        public void containsSuper()
        {
           String target = "super(";
           boolean passed = checkCodeContains(target);
           assertTrue(passed);
         }
     }