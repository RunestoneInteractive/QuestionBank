.. activecode:: ArrayListWordPair1bd
   :author: Brian Dahlem
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: F
   :language: java

   Create an Arraylist of WordPair objects.
   ~~~~
   import java.util.*;

   public class Test {
       public static void main(String[] args)
       {
           // Create an ArrayList of WordPair objects called pairs


           pairs.add(new WordPair("hi","there"));
           pairs.add(new WordPair("hi","bye"));
           System.out.println(pairs);
       }
   }

   class WordPair {
       private String word1;
       private String word2;

       public WordPair(String w1, String w2) {
           word1 = w1;
           word2 = w2;
       }
       public String getFirst() {
           return word1;
       }
       public String getSecond() {
           return word2;
       }
       public String toString() {
           return "(" + word1 + ", " + word2 + ")";
       }
   }