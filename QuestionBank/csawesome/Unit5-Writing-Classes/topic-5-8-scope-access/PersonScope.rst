.. activecode:: PersonScope
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-8-scope-access
  :topics: Unit5-Writing-Classes/topic-5-8-scope-access
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.4782608696
  :total_students_attempting: 69
  :num_students_correct: 63.0
  :mean_clicks_to_correct: 1.6825396825

  Try the following code to see that you cannot access the variables outside of their scope levels in the toString() method. Explain to someone sitting next to you why you can't access these. Try to fix the errors by either using variables that are in scope or moving the variable declarations so that the variables have larger scope.
  ~~~~
  public class Person
  {
     private String name;
     private String email;
  
     public Person(String initName, String initEmail)
     {
        name = initName;
        email = initEmail;
     }
  
     public String toString()
     {
       for (int i=0; i < 5; i++) {
          int id = i;
       }
       // Can you access the blockScope variables i or id?
       System.out.println("i at the end of the loop is " + i);
       System.out.println("The last id is " + id);
  
       // Can toString() access parameter variables in Person()?
       return  initName + ": " + initEmail;
     }
  
     // main method for testing
     public static void main(String[] args)
     {
        // call the constructor to create a new person
        Person p1 = new Person("Sana", "sana@gmail.com");
        System.out.println(p1);
     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testCodeContains(){
          boolean passed = checkCodeContains("returning instance variables", "return  name + \": \" + email;");
          assertTrue(passed);
        }
  
        @Test
        public void testCodeContains2(){
          boolean passed = checkCodeContains("declaration and initialization of id to 0", "int id = 0;");
          assertTrue(passed);
        }
    }