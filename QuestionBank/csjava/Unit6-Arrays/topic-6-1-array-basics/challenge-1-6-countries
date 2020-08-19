.. activecode:: challenge-1-6-countries
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest

   public class Countries
   {
     public static void main(String[] args)
     {
        // 1. Declare 4 arrays and initialize them to the given values.
        // Countries: China, Egypt, France, Germany, India, Japan, Kenya, Mexico, United Kingdom, United States
        // Capitals: Beijing, Cairo, Paris, Berlin, New Delhi, Tokyo, Nairobi, Mexico City, London, Washington D.C.
        // Languages: Chinese, Arabic, French, German, Hindi, Japanese, Swahili, Spanish, English, English
        // Filenames for map images: China.jpg, Egypt.jpg, France.jpg, Germany.jpg, India.jpg, Japan.jpg, Kenya.jpg, Mexico.jpg, UK.jpg, US.jpg

        // 2. Pick a random number up to the length of one of the arrays and save in the variable index

        // 3. Print out the info in each array using the random index

        // Sample image printing - this will only work in Active Code
         // Countries obj = new Countries();
         // obj.printHTMLimage( images[index] );

      }

      // This method will just work in Active Code which interprets html
      public void printHTMLimage(String filename)
      {
        String baseURL = "https://raw.githubusercontent.com/bhoffman0/CSAwesome/master/_sources/Unit6-Arrays/6-1-images/";
        System.out.print("<img src=" + baseURL + filename + ">");
      }
     }
     ====
     // Test for Lesson 6.1 - challenge
     import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;

     public class RunestoneTests extends CodeTestHelper
     {
        public RunestoneTests() {
            super("Countries");
        }

        @Test
        public void test1() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Country Capital Language Image";

            int len = expect.split(" ").length;

            boolean passed = len == 4 && output.contains(".jpg");

            passed = getResults(expect, expect, "Did you print all the info?", passed);
            assertTrue(passed);
        }

        @Test
        public void test2() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "<img src";

            boolean passed = output.contains(expect);

            //passed = getResults(expect + "...", output, "Did you uncomment the image code?", passed);
            passed = getResults("image", "image", "Did you uncomment the image code?", passed);
            assertTrue(passed);
        }

        @Test
        public void test3() throws IOException
        {
            String[] lines = new String[10];

            for (int i = 0; i < lines.length; i++)
            {
                lines[i] = getMethodOutput("main");
            }

            int difft = 10;

            for (int i = 0; i < lines.length-1; i++) {
                if (lines[i].equals(lines[i+1])) {
                    difft--;
                }
            }

            boolean passed = difft > 3;

            passed = getResults("> 3 Countries", difft + " countries", "Can pick a random different country > 3 times?", passed);
            assertTrue(passed);
        }


        @Test
        public void testArrays() throws IOException {
            //System.out.println(program);
            String program = getCode();

            int arrays = 0;
            int index = program.indexOf("String[]");
            while (index >= 0) {
                arrays++;
                index = program.indexOf("String[]", index + 7);
            }

            boolean passed = getResults("5 x String[]", arrays + " x String[]", "Did you declare 4 arrays?");
            assertTrue(passed);
        }
     }