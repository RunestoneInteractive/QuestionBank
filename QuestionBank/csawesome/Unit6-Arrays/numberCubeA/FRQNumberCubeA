.. activecode:: FRQNumberCubeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: numberCubeA
   :topics: Unit6-Arrays/numberCubeA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.0

   FRQ Number Cube A: Write the method ``getCubeTosses`` that takes a number cube and a number of tosses as parameters. The method should return an array of the values produced by tossing the number cube the given number of times.
   ~~~~
    import java.util.Arrays;
    public class NumberCube
    {
   
        public int toss()
        {
            return (int)( (Math.random() * 6) + 1 );
        }
   
        public static int[] getCubeTosses(NumberCube cube, int numTosses)
        {
            // Complete this method
        }
   
        public static void main(String[] args) {
            NumberCube cube = new NumberCube();
            int numTosses = 9;
            int[] tosses = getCubeTosses(cube, numTosses);
   
            if(tosses.length < numTosses) {
              System.out.println("It looks like you are not returning an array of the correct size:");
              System.out.println(Arrays.toString(tosses));
            } else {
              System.out.println("You returned an array of the correct size:");
              System.out.println(Arrays.toString(tosses));
            }
        }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testleng() throws IOException
        {
            String expect = "You returned an array of the correct size";
            String actual = getMethodOutput("main");
   
            boolean passed = getResults(expect, actual, "Checking output from main()");
            assertTrue(passed);
        }
   
        @Test
        public void test1() {
            NumberCube c = new NumberCube();
            int[] results = NumberCube.getCubeTosses(c, 20);
   
            String expect = "20";
            String actual = "" + results.length;
   
            boolean passed = getResults(expect, actual, "Checking getNumTosses() returns an array of the correct size");
            assertTrue(passed);
        }
   
        @Test
        public void test2() {
            NumberCube c = new NumberCube();
            int[] results = NumberCube.getCubeTosses(c, 100);
   
            boolean passed = true;
            int same = 0;
   
            for (int i = 0; i < results.length; i++) {
                if (i < results.length - 1 && results[i] == results[i+1])
                    same++;
   
                if (results[i] < 1 || results[i] > 6)
                    passed = false;
            }
   
            if (same > 25) passed = false;
   
            String expect = "true";
            String actual = "" +passed;
   
            passed = getResults(expect, actual, "Checking that tosses are within proper range (1-6, no 0)", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test3() {
            String target = "cube.toss()";
            boolean passed = checkCodeContains("call to cube.toss()", target);
            assertTrue(passed);
        }
    }