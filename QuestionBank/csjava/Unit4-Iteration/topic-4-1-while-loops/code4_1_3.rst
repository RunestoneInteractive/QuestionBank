.. activecode:: code4_1_3
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit4-Iteration
  :subchapter: topic-4-1-while-loops
  :topics: Unit4-Iteration/topic-4-1-while-loops
  :from_source: T
  :language: java
  :autograde: unittest

  Copy and paste all of your code from your repl.it and run to see if it passes the autograder tests. Include the link to your repl.it code in comments. Note that this code will only run with the autograder's input and will not ask the user for input.
  ~~~~
  // Copy in your link to your code on repl.it here:
  // Copy in all of your code from repl.it below (include import and public class Main)


  ====
  import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Main", input1.replaceAll(" ", "\n")); // For Book
            //super("GuessingGame", input1.replaceAll(" ", "\n")); // For Repl.it
        }

        private static int goal = 1;
        private static String input1 = "100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0";
        private static String input2 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100";
        private String output1, output2;


        @Test
        public void test1()
        {
            String input = input1.replaceAll(" ", "\n");
            String output = getMethodOutputWithInput("main", input);
            output1 = output;

            String[] lines = output.split("\n");

            boolean passed = lines.length >= goal;

            passed = getResults(">" + goal +" lines", "" + lines.length + " lines", "Outputs at least " + goal +" lines", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String input = input2.replaceAll(" ", "\n");
            String output = getMethodOutputWithInput("main", input);
            output2 = output;

            if (output1 == null) {
                input = input1.replaceAll(" ", "\n");
                output1 = getMethodOutputWithInput("main", input);
            }

            boolean passed = !output1.equals(output2);

            passed = getResults("true", "" + passed, "Outputs different results for different inputs", passed);
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, "if");
            boolean passed = num >= 2;

            getResults("2", "" + num, "Number of if statements", passed);
            assertTrue(passed);
        }

        @Test
        public void test4()
        {
            boolean passed = checkCodeContainsRegex("while loop", "while(*)");
            assertTrue(passed);
        }

        @Test
        public void test5()
        {
            String input = input1.replaceAll(" ", "\n");
            int[] values = new int[10];

            for (int i = 0; i < values.length; i++) {
                String output = getMethodOutputWithInput("main", input);
                values[i] = output.split("\n").length;
            }

            boolean passed = false;
            for (int i = 0; i < values.length-1; i++) {
                if (values[i] != values[i+1])
                    passed = true;

            }

            passed = getResults("true", "" + passed, "Guesses random numbers", passed);
            assertTrue(passed);
        }
    }