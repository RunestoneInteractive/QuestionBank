.. activecode:: StringFind
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-6-writing-methods
  :topics: Unit5-Writing-Classes/topic-5-6-writing-methods
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.0366492147
  :total_students_attempting: 191
  :num_students_correct: 104.0
  :mean_clicks_to_correct: 3.9519230769

  Run the following program which contains a method called findLetter that takes a letter and a text as parameters and uses a loop to see if that letter is in the text and returns true if it is, false otherwise. Set the variables ``letter`` and ``message`` to new values in the main method and run it again to try finding a different letter. Then, change the code of the findLetter method to return how many times it finds letter in text, using a new variable called ``count``. How would the return type change?
  ~~~~
  public class StringFind
  {
    /** findLetter looks for a letter in a String
     * @param String letter to look for
     * @param String text to look in
     * @return boolean true if letter is in text
     * After running the code, change this method to return
     * an int count of how many times letter is in the text.
     */
     public boolean findLetter(String letter, String text)
     {
         boolean flag = false;
         for(int i=0; i < text.length(); i++)
         {
             if (text.substring(i, i+1).equalsIgnoreCase(letter))
                 {
                flag = true;
                 }
         }
         return flag;
      }
  
      public static void main(String args[])
      {
          StringFind test = new StringFind();
          String message = "Apples and Oranges";
          String letter = "p";
          System.out.println("Does " + message +  " contain a " + letter + "?");
          System.out.println( test.findLetter(letter, message) );
      }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void tryfindLetter() throws IOException
        {
           String message = "Apples and Oranges";
           String letter = "p";
           Object[] args = {letter,message};
           String output = getMethodOutput("findLetter", args);
           String expect = "2";
  
           boolean passed = getResults(expect, output,
                    "findLetter(\"p\",\"Apples and Oranges\")");
           assertTrue(passed);
        }
  
         @Test
        public void tryfindLetter2() throws IOException
        {
           String message = "Test strings";
           String letter = "s";
           Object[] args = {letter,message};
           String output = getMethodOutput("findLetter", args);
           String expect = "3";
  
           boolean passed = getResults(expect, output,
                    "findLetter(\"s\",\"Test strings\")");
           assertTrue(passed);
        }
        @Test
        public void test2()
        {
            boolean passed = checkCodeContains("changed return type of findLetter", "public int findLetter(String letter, String text)");
            assertTrue(passed);
        }
  
         @Test
        public void test1()
        {
            boolean passed = checkCodeContains("variable count set to 0", "int count = 0;");
            assertTrue(passed);
        }
  
         @Test
        public void test3()
        {   String code = removeSpaces(getCode());
            boolean passed = code.contains("count++;") ||
            code.contains("count=count+1;") || code.contains("count=1+count;") || code.contains("count+=1;") || code.contains("++count;");
            passed = getResults("count incremented",Boolean.toString(passed),"Count incremented?", passed);
            assertTrue(passed);
        }
    }