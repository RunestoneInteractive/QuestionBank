.. activecode:: SongFarm
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-4-methods-with-params
    :topics: Unit2-Using-Objects/topic-2-4-methods-with-params
    :from_source: T
    :language: java
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.2966101695
    :total_students_attempting: 118
    :num_students_correct: 86.0
    :mean_clicks_to_correct: 1.6976744186

    Add another verse in main that calls the method verse with a different animal and noise.
    ~~~~
    public class Song
    {
    
        public void verse(String animal, String noise)
        {
            System.out.println("Old MacDonald had a farm");
            chorus();
            System.out.println("And on that farm he had a " + animal);
            chorus();
            System.out.println("With a " + noise + " " + noise + " here,");
            System.out.println("And a " + noise + " " + noise + " there,");
            System.out.println("Old MacDonald had a farm");
            chorus();
        }
        public void chorus()
        {
            System.out.println("E-I-E-I-O");
        }
    
        public static void main(String[] args)
        {
           Song s = new Song();
           s.verse("cow", "moo");
           s.verse("duck","quack");
        }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    
    public class RunestoneTests extends CodeTestHelper
    {
        public String expected = "Old MacDonald had a farm\nE-I-E-I-O\nAnd on that farm he had a cow\nE-I-E-I-O\nWith a moo moo here,\nAnd a moo moo there,\nOld MacDonald had a farm\nE-I-E-I-O\nOld MacDonald had a farm\nE-I-E-I-O\nAnd on that farm he had a duck\nE-I-E-I-O\nWith a quack quack here,\nAnd a quack quack there,\nOld MacDonald had a farm\nE-I-E-I-O";
    
        public RunestoneTests() {
            super("Song");
        }
    
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
    
            boolean passed = output.contains(expected);
    
            passed = getResults(expected, output, "Still have the old output", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
    
            boolean passed = output.contains(expected) && !output.equals(expected);
    
            passed = getResults(expected, output, "Verse added", passed);
            assertTrue(passed);
        }
    
        @Test
        public void test3()
        {
            String code = getCode();
            int numVerses = countOccurences(code, "verse(");
            boolean passed = numVerses >= 4;
            // + 1 because of verse method definition
            passed = getResults("3 or more", ""+numVerses, "Number of verses", passed);
            assertTrue(passed);
        }
    }