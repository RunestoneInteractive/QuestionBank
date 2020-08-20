.. activecode:: challenge-9-1-online-store
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-1-inheritance-day2
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day2
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.8
  :total_students_attempting: 5
  :num_students_correct: 5.0
  :mean_clicks_to_correct: 1.2

  Declare at least 2 instance variables for each of the classes below. Create an inheritance or association relationship for some of them.
  ~~~~
  class ItemForSale
  {
  
  }
  
  class Movie
  {
  
  }
  
  class Book
  {
  
  }
  
  class Author
  {
  
  }
  
  public class Store
  {
       // instance variable (could be an array or ArrayList of one of the classes above)
  
       public static void main(String[] args)
       {
          Store s = new Store();
          Book b = new Book();
          System.out.println(b instanceof ItemForSale);
       }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Store");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "true";
  
            boolean passed = getResults(expect, output, "Running main", true);
            assertTrue(passed);
  
        }
  
        @Test
        public void test2()
        {
            String code = getCode();
            String target = "extends ItemForSale";
  
            int num = countOccurences(code, target);
  
            boolean passed = num >= 2;
            getResults("2", ""+num, "Testing code for " + target);
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariablesItemForSale()
        {
            String cname = "ItemForSale";
            changeClass(cname);
            String expect = "2+ Private";
            String output = testPrivateInstanceVariables();
  
            int num = Integer.parseInt(output.substring(0, output.indexOf(" ")));
  
            boolean passed = num >= 2;
  
            getResults(expect, output, "Checking Instance Variables - " + cname, passed);
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariablesAuthor()
        {
            String cname = "Author";
            changeClass(cname);
            String expect = "2+ Private";
            String output = testPrivateInstanceVariables();
  
            int num = Integer.parseInt(output.substring(0, output.indexOf(" ")));
  
            boolean passed = num >= 2;
  
            getResults(expect, output, "Checking Instance Variables - " + cname, passed);
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariablesMovie()
        {
            String cname = "Movie";
            changeClass(cname);
            String expect = "2+ Private";
            String output = testPrivateInstanceVariables();
  
            int num = Integer.parseInt(output.substring(0, output.indexOf(" ")));
  
            boolean passed = num >= 2;
  
            getResults(expect, output, "Checking Instance Variables - " + cname, passed);
            assertTrue(passed);
        }
  
        @Test
        public void testPrivateVariablesBook()
        {
            String cname = "Book";
            changeClass(cname);
            String expect = "2+ Private";
            String output = testPrivateInstanceVariables();
  
            int num = Integer.parseInt(output.substring(0, output.indexOf(" ")));
  
            boolean passed = num >= 2;
  
            getResults(expect, output, "Checking Instance Variables - " + cname, passed);
            assertTrue(passed);
        }
    }