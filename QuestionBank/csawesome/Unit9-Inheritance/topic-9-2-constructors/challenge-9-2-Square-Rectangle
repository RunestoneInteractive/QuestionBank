.. activecode:: challenge-9-2-Square-Rectangle
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-2-constructors
  :topics: Unit9-Inheritance/topic-9-2-constructors
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.2
  :total_students_attempting: 10
  :num_students_correct: 3.0
  :mean_clicks_to_correct: 1.6666666667

  Create a Square class that inherits from Rectangle.
  ~~~~
  class Rectangle
  {
      private int length;
      private int width;
  
      public Rectangle()
      {
         length = 1;
         width = 1;
      }
  
      public Rectangle(int l, int w)
      {
         length = l;
         width = w;
      }
  
      public void draw()
      {
        for(int i=0; i < length; i++)
        {
           for(int j=0; j < width; j++)
               System.out.print("* ");
            System.out.println();
        }
        System.out.println();
      }
  
  }
  
  // 1. Make the class square inherit from Rectangle
  public class Square
  {
       // 2. Add a Square no-argument constructor
  
       // 3. Add a Square constructor with 1 argument for a side
  
       public static void main(String[] args)
       {
          Rectangle r = new Rectangle(3,5);
          r.draw();
          // 4. Uncomment these to test
          // Square s1 = new Square();
          // s1.draw();
          // Square s = new Square(3);
          // s.draw();
       }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Square");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main").trim();
            String expect = "* * * * *\n* * * * * \n* * * * * \n\n* \n\n* * * \n* * * \n* * *";
  
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
  
        @Test
        public void test2()
        {
            String target = "extends Rectangle";
  
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
        }
  
        @Test
        public void test3()
        {
            String output = checkDefaultConstructor();
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking Square no-argument constructor");
            assertTrue(passed);
        }
  
        @Test
        public void test4()
        {
            String output = checkConstructor(new Object[]{1});
            String expect = "pass";
  
            boolean passed = getResults(expect, output, "Checking Square constructor with 1 argument (int)");
            assertTrue(passed);
        }
    }