.. activecode:: RandomStrChooserB1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: FreeResponse
   :subchapter: RandomStringChooserB
   :topics: FreeResponse/RandomStringChooserB
   :from_source: T
   :language: java
   :datafile: RandomStringChooser.java

   import java.util.List;
   import java.util.ArrayList;

   public class RandomLetterChooser extends RandomStringChooser
   {
       /** Constructs a random letter chooser using the given string str.
        *  Precondition: str contains only letters.
        */
       public RandomLetterChooser (String str)
       {
         //*** write the constructor here ***!
       }

       /** Returns an array of single-letter strings.
        *  Each of these strings consists of a single letter from str.  Element k
        *  of the returned array contains the single letter at position k of str.
        *  For example, getSingleLetters("cat") return the
        *  array {"c", "a", "t" }.
        */
       public static String[] getSingleLetters(String str)
       {
          String[] strArr = new String[str.length()];
          for (int i = 0; i < str.length(); i++)
          {
             strArr[i] = str.substring(i, i+1);
          }
          return strArr;
       }

       public static void main(String[] args)
       {
           RandomLetterChooser letterChooser = new RandomLetterChooser("cat");
           System.out.println("This should print three letters at random from cat and then NONE");
           for (int k = 0; k < 4; k++)
           {
               System.out.print(letterChooser.getNext());
           }
        }
   }