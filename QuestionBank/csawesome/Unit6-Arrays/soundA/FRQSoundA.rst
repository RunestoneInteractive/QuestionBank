.. activecode:: FRQSoundA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: soundA
   :topics: Unit6-Arrays/soundA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.0

   FRQ Sound A: Write the method ``limitAmplitude`` that will change any value that has an amplitude greater than the given limit. Values that are greater than ``limit`` are replaced with ``limit``, and values that are less than ``-limit`` are replaced with ``–limit``. The method returns the total number of values that were changed in the array.  The ``main`` method has code to test your solution.
   ~~~~
   import java.util.Arrays;
   public class Sound
   {
       // the array of values in this sound; guaranteed not to be null
       private int[] samples = { 40, 2532, 17, -2300, -17, -4000, 2000, 1048, -420, 33, 15, -32, 2030, 3223};
   
       /** Changes those values in this sound that have an amplitude greater than limit
        *  Values greater than limit are changed to limit.
        *  @param limit the amplitude limit
        *         Precondition: limit >= 0
        *  @return the number of values in this sound that this method changed
        */
       public int limitAmplitude(int limit){
        // Complete this method
       }
   
       public static void main(String[] args){
   
           Sound s = new Sound();
           System.out.println("The original array is: " + Arrays.toString(s.samples));
           System.out.println("limitAmplitude(2000) should return 5 " +
                              "and returned " + s.limitAmplitude(2000));
           System.out.println("The changed array is: " + Arrays.toString(s.samples));
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.Arrays;
    import java.lang.reflect.Field;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "40, 2000, 17, -2000, -17, -2000, 2000, 1048, -420, 33, 15, -32, 2000, 2000";
            boolean passed = output.contains(expect);
   
            expect = "The original array is: [40, 2532, 17, -2300, -17, -4000, 2000, 1048, -420, 33, 1\n5, -32, 2030, 3223]\nlimitAmplitude(2000) should return 5 and returned 5\nThe changed array is: [40, 2000, 17, -2000, -17, -2000, 2000, 1048, -420, 33, 15, -32, 2000, 2000]";
   
            getResults(expect, output, "Checking output from main()", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test1() {
            Sound s = new Sound();
   
            String expected = "8";
            String actual = "" + s.limitAmplitude(75);
   
            String msg = "Checking limitAmplitude(75) return value";
            boolean passed = getResults(expected, actual, msg);
            assertTrue(passed);
   
        }
   
        @Test
        public void test2() {
            Sound s = new Sound();
            s.limitAmplitude(75);
   
            try {
                Field sampleField = Sound.class.getDeclaredField("samples");
                sampleField.setAccessible(true);
   
                int[] samples = (int[]) sampleField.get(s);
   
                String expected = "[40, 75, 17, -75, -17, -75, 75, 75, -75, 33, 15, -32, 75, 75]";
                String actual = Arrays.toString(samples);
   
                String msg = "Checking limitAmplitude(75) array results";
                boolean passed = getResults(expected, actual, msg);
                assertTrue(passed);
   
            } catch (Exception e) {
                getResults("", "", "There was a error with the testing code.", false);
                fail();
            }
        }
    }