.. activecode:: challenge-5-8-Debug
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-8-scope-access
  :topics: Unit5-Writing-Classes/topic-5-8-scope-access
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.387755102
  :total_students_attempting: 49
  :num_students_correct: 42.0
  :mean_clicks_to_correct: 2.5238095238

  Debug the following program that has scope violations. Then, add comments that label the variable declarations as class, method, or block scope.
  ~~~~
  public class TesterClass
  {
     public static void main(String[] args)
     {
        Fraction f1 = new Fraction();
        Fraction f2 = new Fraction(1,2);
        System.out.println(f1);
        System.out.println(f2.numerator / f2.denominator);
     }
   }
  
  /** Class Fraction */
  class Fraction
  {
     //  instance variables
     private int numerator;
     private int denominator;
  
     // constructor: set instance variables to default values
     public Fraction()
     {
        int d = 1;
        numerator = d;
        denominator = d;
     }
  
     // constructor: set instance variables to init parameters
     public Fraction(int initNumerator, int initDenominator)
     {
        numerator = initNumerator;
        denominator = initDenominator;
     }
  
     public String toString()
     {
       // if the denominator is 1, then just return the numerator
       if (denominator == d) {
          int newNumerator = 1;
       }
       return newNumerator + "/" + denominator;
     }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("TesterClass");
        }
  
        @Test
        public void test1() {
            String orig = "public class TesterClass\n{\n   public static void main(String[] args)\n   {\n      Fraction f1 = new Fraction();\n      Fraction f2 = new Fraction(1,2);\n      System.out.println(f1);\n      System.out.println(f2.numerator / f2.denominator);\n   }\n }\n\n/** Class Fraction */\nclass Fraction\n{\n   //  instance variables\n   private int numerator;\n   private int denominator;\n\n   // constructor: set instance variables to default values\n   public Fraction()\n   {\n      int d = 1;\n      numerator = d;\n      denominator = d;\n   }\n\n   // constructor: set instance variables to init parameters\n   public Fraction(int initNumerator, int initDenominator)\n   {\n      numerator = initNumerator;\n      denominator = initDenominator;\n   }\n\n   public String toString()\n   {\n     // if the denominator is 1, then just return the numerator\n     if (denominator == d) {\n        int newNumerator = 1;\n     }\n     return newNumerator + \"/\" + denominator;\n   }\n}\n";
  
            boolean passed = codeChanged(orig);
            assertTrue(passed);
        }
  
        @Test
        public void test2() {
            String expect = "1\n1/2";
            String actual = getMethodOutput("main");
  
            boolean passed = getResults(expect, actual, "Testing main()");
            assertTrue(passed);
        }
    }