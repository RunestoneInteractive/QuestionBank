.. activecode::  ooEx5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.3333333333

   Override the taste method from the Candy class in the Chocolate class to return ``tastes chocolately``.  It should print ``tastes sweet!`` and then ``tastes chocolately``.
   ~~~~
   public class Candy
   {
       public String taste()
       {
           return "tastes sweet!";
       }
   
       public static void main(String[] args)
       {
           Candy c1 = new Candy();
           System.out.println(c1.taste());
           Candy c2 = new Chocolate();
           System.out.println(c2.taste());
       }
   }
   
   class Chocolate extends Candy
   {
       // ADD CODE HERE
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
        String expect = "tastes sweet!\n" +
                        "tastes chocolately\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
    @Test
      public void test1()
      {
        String code = getCode();
        String target = "public String taste()";
   
        int num = countOccurencesRegex(code, target);
   
        boolean passed = (num == 2);
   
        getResults("2", ""+num, "2 taste methods", passed);
        assertTrue(passed);
      }
    }