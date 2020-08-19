.. activecode:: code5_2_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T

  Use the CodeLens button to watch how the main method
  passes actual argument values into each call to the verse method.
  Update the main method to add a third verse to the song with another animal and noise.
  Rerun the program to confirm the third verse is correct.
  ~~~~
  public class Song
  {

    public static void verse(String animal, String noise)
    {
      System.out.println( "Old MacDonald had a farm" );
      System.out.println( "E-I-E-I-O" );
      System.out.println( "And on that farm he had a " + animal );
      System.out.println( "E-I-E-I-O" );
      System.out.println( "With a " + noise + "-" + noise + " here") ;
      System.out.println( "And a " + noise + "-" + noise + " there" );
      System.out.println( "Here a " + noise + ", there a " + noise );
      System.out.println( "Everywhere a " + noise + "-" + noise );
      System.out.println( "Old MacDonald had a farm" );
      System.out.println( "E-I-E-I-O" );
    }

    public static void main(String[] args)
    {
      verse( "cow" , "moo" );
      verse( "duck" , "quack" );
    }
  }
  ====
  import static org.junit.Assert.*;
  import org.junit.*;;
  import java.io.*;

  public class RunestoneTests extends CodeTestHelper
  {

    public RunestoneTests() {
      super("Song");
    }

    @Test
    public void test1()
    {
      String code = getCode();
      int numVerses = countOccurences(code, "verse(");
      numVerses--; //exclude definition
      boolean passed = numVerses >= 3;

      passed = getResults("3 verses", numVerses + " verses", "Update the main with a third verse call", passed);
      assertTrue(passed);
    }
  }