.. activecode:: Song2
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
  :pct_on_first: 0.1941747573
  :total_students_attempting: 206
  :num_students_correct: 171.0
  :mean_clicks_to_correct: 2.1169590643

  Run the following code to see the song This Old Man print out using the verse and chorus methods.  You can also see this code run in the |visualizer| by clicking on the Show Code Lens button below. Can you add verse three with the rhyme "knee"? Can you add verse four with the rhyme "door"? How many verses do you know?
  ~~~~
  public class Song
  {
  
    /** Verse - prints out a verse of the song
     * @param number - a String like "one", "two", etc.
     * @param rhyme - a String like "thumb", "shoe", etc.
     */
     public void verse(String number, String rhyme)
     {
       System.out.println("This old man, he played " + number);
       System.out.println("He played knick knack on my " + rhyme);
     }
  
    // The chorus method
    public void chorus()
    {
       System.out.println("With a knick knack paddy whack, give a dog a bone.");
       System.out.println("This old man came rolling home.");
    }
  
    public static void main(String args[])
    {
        Song mySong = new Song();
        mySong.verse("one", "thumb");
        mySong.chorus();
        mySong.verse("two", "shoe");
        mySong.chorus();
    }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testThree()
        {
            boolean passed = checkCodeContains("verse three", "mySong.verse(\"three\", \"knee\");");
            assertTrue(passed);
        }
  
        @Test
        public void testFour()
        {
            boolean passed = checkCodeContains("verse four", "mySong.verse(\"four\", \"door\");");
            assertTrue(passed);
        }
    }