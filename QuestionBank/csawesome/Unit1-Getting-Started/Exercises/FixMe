.. activecode:: FixMe
   :author: Joshua Underwood
   :difficulty: 2.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.3939393939
   :total_students_attempting: 33
   :num_students_correct: 31.0
   :mean_clicks_to_correct: 5.3548387097

   You have an attempt at the complete class named "FixMe".  Unfortunately, the code contains several errors. When completed correctly, it will produce the following output:
   
   
           You have successfully
   
           fixed the class!
   
           Well done!
   
   
   
   ~~~~
   //Todo: Fix the FixMe Class
   
   public FixMe{
   
     public main(){
   
       System.out.print("You have successfully");
       System.out.Print("fixed the class!")
       systemoutprintln(Well done!);
   
   }
   
   ====
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;
   import java.lang.reflect.Method;
   
   public class RunestoneTests extends CodeTestHelper
   {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "You have successfully\nfixed the class!\nWell done!";
            if(output.equals(expect)){
               boolean passed = getResults(expect, output, "Expected output from main");
               assertTrue(passed);
            } else {
               boolean passed = getResults(expect, "See gray output", "Your output does not match the expected. Be sure to review it carefully for typos.");
               assertTrue(false);
            }
        }
   
        @Test
        public void testClass() throws IOException
        {
            boolean a = false;
            try{
               Class.forName("FixMe");
               a = true;
            } catch (Exception e) {
            }
   
            if(a){
               boolean passed = getResults("classname: FixMe", "classname: FixMe", "Testing that you named your class properly");
               assertTrue(true);
            } else {
               boolean passed = getResults("FixMe", "see your class name in your code", "Testing that you named your class properly");
               assertTrue(false);
            } 
        }
   }