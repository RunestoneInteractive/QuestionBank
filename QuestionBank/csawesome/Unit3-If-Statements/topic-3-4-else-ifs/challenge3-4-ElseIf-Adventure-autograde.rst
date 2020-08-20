.. activecode:: challenge3-4-ElseIf-Adventure-autograde
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit3-If-Statements
  :subchapter: topic-3-4-else-ifs
  :topics: Unit3-If-Statements/topic-3-4-else-ifs
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.1927710843
  :total_students_attempting: 83
  :num_students_correct: 61.0
  :mean_clicks_to_correct: 2.2786885246

  Copy and paste your all of your code from repl.it and run to see if it passes the autograder tests. Include the link to your repl.it code in comments. Note that this code will only run with the autograder's input and will not ask the user for input.
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
        }
  
        private static int goal = 5;
        private static String input1 = "n s e w y y y y y y y y y y y y y y";
        private static String input2 = "s e w y n y y y y y y y y y y y y y";
        private static String input3 = "e w y n s y y y y y y y y y y y y y";
        private static String input4 = "w y n s e y y y y y y y y y y y y y";
        private static String input5 = "y n s e w y y y y y y y y y y y y y";
        private String output1, output2, output3, output4, output5;
  
        @Test
        public void test1()
        {
            String input = input1.replaceAll(" ", "\n");
            String output = getMethodOutputWithInput("main", input);
            output1 = output;
  
            String[] lines = output.split("\n");
  
            boolean passed = lines.length >= goal;
  
            passed = getResults(goal +"+ lines", "" + lines.length + " lines", "Outputs at least " + goal +" lines", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test2()
        {
            String input = input2.replaceAll(" ", "\n");
            String output = getMethodOutputWithInput("main", input);
            output2 = output;
  
            input = input3.replaceAll(" ", "\n");
            output = getMethodOutputWithInput("main", input);
            output3 = output;
  
            input = input4.replaceAll(" ", "\n");
            output = getMethodOutputWithInput("main", input);
            output4 = output;
  
            input = input5.replaceAll(" ", "\n");
            output = getMethodOutputWithInput("main", input);
            output5 = output;
  
            if (output1 == null) {
                input = input1.replaceAll(" ", "\n");
                output1 = getMethodOutputWithInput("main", input);
            }
  
            boolean passed = !output1.equals(output2) && !output1.equals(output3) && !output1.equals(output4) && !output1.equals(output5);
  
            passed = getResults("true", "" + passed, "Outputs different results for different inputs", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, "if");
            boolean passed = num >= 4;
  
            getResults("4", "" + num, "Number of if statements", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test4()
        {
            String code = getCode();
            int elseif = countOccurences(code, "else if");
            boolean passed = elseif == 3;
  
            getResults(""+3, ""+elseif, "Number of else if statements", passed);
            assertTrue(passed);
        }
  
        @Test
        public void test5()
        {
            String code = getCode();
            int num = countOccurences(code, "else {");
            boolean passed = num >= 1;
  
            getResults("1", "" + num, "Number of else statements", passed);
            assertTrue(passed);
        }
    }