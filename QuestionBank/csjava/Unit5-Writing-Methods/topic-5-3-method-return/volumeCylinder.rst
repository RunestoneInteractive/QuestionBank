.. activecode:: volumeCylinder
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-3-method-return
  :topics: Unit5-Writing-Methods/topic-5-3-method-return
  :from_source: F
  :language: java
  :autograde: unittest
  :practice: T

  The method ``volumeCylinder`` takes parameters representing the radius and height of a cylinder,
  and returns the corresponding volume.  The method returns a value that has type ``double``.
  Use the CodeLens to step through the code.
  Experiment with passing different values to the method.

  ~~~~
  public class VolumeExample
  {
    public static double volumeCylinder(double radius, double height)
    {
      return Math.PI * radius * radius * height;
    }

    public static void main(String args[])
    {
      // Calculate the volume of a cylinder  radius=4 and height=10
      double vol = volumeCylinder(4, 10);
      System.out.println(vol);
    }
  }
  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("VolumeExample");
    }

    @Test
      public void test1()
      {
        boolean passed = getResults("true", "true", "main()");
        assertTrue(passed);
      }
  }