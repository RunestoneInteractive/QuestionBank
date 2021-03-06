.. activecode:: class-Fraction
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-2-writing-constructors
  :topics: Unit6-Writing-Classes/topic-6-2-writing-constructors
  :from_source: F
  :language: java
  :autograde: unittest

  The following class defines a Fraction with the instance variables numerator and denominator.
  It uses 2 constructors. Note that this constructor sets the default instance
  variable values to 1 rather than 0 -- so we don't end up with divide by zero. Try to guess what it will print before you run it.  Hint!  Remember to start with the main method! You can also view it in the |Java visualizer| by clicking on the Code Lens button below.
  ~~~~
  public class Fraction
  {
     //  instance variables
     private int numerator;
     private int denominator;

     // constructor: set instance variables to default values
     public Fraction()
     {
        numerator = 1;
        denominator = 1;
     }

     // constructor: set instance variables to init parameters
     public Fraction(int initNumerator, int initDenominator)
     {
        numerator = initNumerator;
        denominator = initDenominator;
     }

     // Print fraction
     public void print()
     {
       System.out.println(numerator + "/" + denominator);
     }

     // main method for testing
     public static void main(String[] args)
     {
        Fraction f1 = new Fraction();
        Fraction f2 = new Fraction(1,2);
        // What will these print out?
        f1.print();
        f2.print();
     }
  }
  ====
  // Test Code for Lesson 5.2.0.1 - Fraction
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;

    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "1/1\n1/2";

            boolean passed = getResults(expect, output, "Running main", true);
            assertTrue(passed);
        }

    }