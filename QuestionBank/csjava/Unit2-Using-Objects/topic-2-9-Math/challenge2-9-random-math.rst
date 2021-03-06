.. activecode:: challenge2-9-random-math
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-9-Math
   :topics: Unit2-Using-Objects/topic-2-9-Math
   :from_source: F
   :language: java
   :autograde: unittest

   Complete the combination lock challenge below.
   ~~~~
   public class MathChallenge
   {
      public static void main(String[] args)
      {
        // 1. Use Math.random() to generate 3 integers from 0-40 (not including 40) and print them out.


        // 2. Calculate the number of combinations to choose 3 numbers between 0-40 (not including 40) using Math.pow() and print it out.
        // For example, Math.pow(10,2) is 10^2 and the number of permutations to choose 2 numbers between 0-9.


      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    import java.util.ArrayList;

    public class RunestoneTests extends CodeTestHelper
    {


        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String[] lines = output.split("\\s+");

            boolean passed = lines.length >= 2;

            passed = getResults("2+ lines of output", lines.length + " lines of output", "Expected output", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("main");

            boolean passed = output.contains("6400");

            passed = getResults("true", "" + passed, "Prints 40^3", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, "Math.random()");

            boolean passed = num >= 3;
            passed = getResults("3 or more", ""+num, "Calls to Math.random()", passed);
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            String code = getCode();
            int num = countOccurences(code, "Math.pow(");

            boolean passed = num >= 1;
            passed = getResults("1 or more", ""+num, "Calls to Math.pow(...)", passed);
            assertTrue(passed);
        }

        @Test
        public void test5() {
            int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;

            String output = "";
            String[] lines;
            int[] nums = new int[4];
            int countUniqueNums = 0;

            for (int i = 0; i < 1000; i++) {
                output = getMethodOutput("main");
                lines = output.split("\\s+");

                if (lines.length == nums.length) {
                    nums[0] = Integer.parseInt(lines[0]);
                    nums[1] = Integer.parseInt(lines[1]);
                    nums[2] = Integer.parseInt(lines[2]);

                    min = Math.min(min, Math.min(nums[0], Math.min(nums[1], nums[2])));
                    max = Math.max(max, Math.max(nums[0], Math.max(nums[1], nums[2])));

                    if (nums[0] != nums[1] && nums[1] != nums[2])
                        countUniqueNums++;
                }
            }

            boolean passed = min == 0 && max == 39 && countUniqueNums > 5;
            getResults("Min: " + 0 + "\nMax: " + 39, "Min: " + min + "\nMax: " + max, "Checking random results", passed);
            assertTrue(passed);
        }
    }