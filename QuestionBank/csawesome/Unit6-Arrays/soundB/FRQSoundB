.. activecode:: FRQSoundB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: soundB
   :topics: Unit6-Arrays/soundB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.75
   :total_students_attempting: 4
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 1.25

   FRQ Sound B: Finish writing the method ``trimSilenceFromBeginning`` below that removes the silence from the beginning of a sound. To remove starting silence, a new array of values is created that contains the same values as the original ``samples`` array in the same order but without the leading zeros. The instance variable ``samples`` is updated to refer to the new array.
   ~~~~
   import java.util.Arrays;
   public class Sound
   {
       /** the array of values in this sound; guaranteed not to be null */
       private int[] samples = {0, 0, 0, 0, -14, 0, -35, -39, 0, -7, 16, 32, 37, 29, 0, 0};
   
       /** Removes all silence from the beginning of this sound.
        *  Silence is represented by a value of 0.
        *  Precondition: samples contains at least one nonzero value
        *  Postcondition: the length of samples reflects the removal of starting silence
        */
       public void trimSilenceFromBeginning()
       {
         // Complete this method
       }
   
       public static void main(String[] args)
       {
   
         Sound s = new Sound();
   
         System.out.println("The original array of samples is " + Arrays.toString(s.samples));
         s.trimSilenceFromBeginning();
         System.out.println("The new array of samples is " + Arrays.toString(s.samples));
         System.out.println("The length of the new array should be 12 and is " + s.samples.length);
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    import java.lang.reflect.Field;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "-14, 0, -35, -39, 0, -7, 16, 32, 37, 29, 0, 0";
   
            boolean passed = output.contains(expect);
   
            expect = "The original array of samples is [0, 0, 0, 0, -14, 0, -35, -39, 0, -7, 16, 32, 37, 29, 0, 0]\nThe new array of samples is [-14, 0, -35, -39, 0, -7, 16, 32, 37, 29, 0, 0]";
   
            getResults(expect, output, "Checking output from main()", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2() {
            Sound s = new Sound();
            s.trimSilenceFromBeginning();
   
            try {
                Field sampleField = Sound.class.getDeclaredField("samples");
                sampleField.setAccessible(true);
   
                int[] samples = (int[]) sampleField.get(s);
   
                String expected = "12";
                String actual = ""+ samples.length;
   
                String msg = "Checking samples array length after trimSilenceFromBeginning()";
                boolean passed = getResults(expected, actual, msg);
                assertTrue(passed);
   
            } catch (Exception e) {
                getResults("", "", "There was a error with the testing code.", false);
                fail();
            }
        }
    }