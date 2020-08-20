.. activecode:: changeparamvalue
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  Use the CodeLens button or copy the code into the |visualizer| to watch how the square method
  alters the value of x, while the value of y in the main method is not affected.

  Try changing the name of the variable in the main method to "x" and rerun the program.  You should see
  that the variable in the main method remains unaffected by changes made in the square method, even when
  the variables have the same name.
  ~~~~
  public class CallByValue
  {
    public static void square(int x)
    {
      x = x * x;
      System.out.print(x);
    }

    public static void main(String[] args)
    {
      int y = 5;
      square(y);
    }
  }

  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("CallByValue");
    }

    @Test
    public void test1()
    {
      String code = getCode();
      int num = countOccurences(code, "square(");
      boolean passed = numVerses = 1;
      passed = getResults("1 call", 1 + " ca;;", "The main should call the square method", passed);
      assertTrue(passed);
    }
  }