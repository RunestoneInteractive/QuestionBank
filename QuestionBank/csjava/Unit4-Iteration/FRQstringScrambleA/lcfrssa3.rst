.. activecode:: lcfrssa3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: FRQstringScrambleA
   :topics: Unit4-Iteration/FRQstringScrambleA
   :from_source: T
   :language: java
   :autograde: unittest

   public class Test
   {
      public static void main(String[] args)
      {
         System.out.println("ABRACADABRA".substring(0,1)); // get the A
         System.out.println("ABRACADABRA".substring(1,2)); // get the B
         // compare the A and B and swap them which results in BARACADABRA
         System.out.println("ABRACADABRA".substring(2,3)); // get the R
         System.out.println("ABRACADABRA".substring(3,4)); // get the A
         // compare the R and A and do nothing
         System.out.println("ABRACADABRA".substring(3,4)); // get the A
         System.out.println("ABRACADABRA".substring(4,5)); // get the C
         // compare the A and C and swap them which results in BARCAADABRA
         System.out.println("ABRACADABRA".substring(5,6)); // get the A
         System.out.println("ABRACADABRA".substring(6,7)); // get the D
         // compare the A and D and swap them which results in BARCADAABRA
         System.out.println("ABRACADABRA".substring(7,8)); // get the A
         System.out.println("ABRACADABRA".substring(8,9)); // get the B
         // compare the A and B and swap them which results in BARCADABARA
         System.out.println("ABRACADABRA".substring(9,10)); // get the R
         System.out.println("ABRACADABRA".substring(10,11)); // get the A
         // compare R and A and do nothing
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "A\nB\nR\nA\nA\nC\nA\nD\nA\nB\nR\nA\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
    }