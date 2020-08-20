.. activecode:: lcfrsbasicGapWidth
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: 2016freeresponseQ4B
   :topics: ListBasics/2016freeresponseQ4B
   :from_source: T
   :language: java

   import java.util.*;
   public class StringFormatter
   {
       /** Returns the basic gap width when wordList is used to produce
       *  a formatted string of formattedLen characters.
       *  Precondition: wordList contains at least two words, consisting of letters only.
       *            formattedLen is large enough for all the words and gaps.
       */
       public static int basicGapWidth(List<String> wordList,
                                       int formattedLen)
       {
       }

       public static int totalLetters(List<String> wordList)
       {
           int numLetters = 0;
           for (String s : wordList)
           {
               numLetters = numLetters + s.length();
           }
           return numLetters;
       }

       public static void main(String[] args)
       {
           List<String> wordList = new ArrayList<String>();
           wordList.add("AP");
           wordList.add("COMP");
           wordList.add("SCI");
           wordList.add("ROCKS");
           System.out.println("Should print 2 and prints: " + basicGapWidth(wordList,20));

           List<String>words2 = new ArrayList<String>();
           words2.add("GREEN");
           words2.add("EGGS");
           words2.add("AND");
           words2.add("HAM");
           System.out.println("Should print 1 and prints: " + basicGapWidth(words2,20));

           List<String>words3 = new ArrayList<String>();
           words3.add("BEACH");
           words3.add("BALL");
           System.out.println("Should print 11 and prints: " + basicGapWidth(words3,20));
       }
   }