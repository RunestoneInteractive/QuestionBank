.. activecode:: RowYourBoat
   :author: Joshua Underwood
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.4117647059
   :total_students_attempting: 34
   :num_students_correct: 32.0
   :mean_clicks_to_correct: 3.75

   Write a complete class named "RowYourBoat".  It must have a main method and produces the following output:
   
   
   Row, row, row your boat
   
   Gently down the stream
   
   Merrily merrily, merrily, merrily
   
   Life is but a dream
   
   ~~~~
   // enter your here: 
   //Todo: write the complete class RowYourBoat
   
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
            String expect = "Row, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream";
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
               Class.forName("RowYourBoat");
               a = true;
            } catch (Exception e) {
            }
   
            if(a){
               boolean passed = getResults("classname: RowYourBoat", "classname: RowYourBoat", "Testing that you named your class properly");
               assertTrue(true);
            } else {
               boolean passed = getResults("RowYourBoat", "see your class name in your code", "Testing that you named your class properly");
               assertTrue(false);
            } 
        }
   }