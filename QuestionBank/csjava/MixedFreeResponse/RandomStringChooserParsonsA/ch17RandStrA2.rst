.. parsonsprob:: ch17RandStrA2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: MixedFreeResponse
   :subchapter: RandomStringChooserParsonsA
   :topics: MixedFreeResponse/RandomStringChooserParsonsA
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The mixed up code below includes the correct code for the class, a field, a constructor, and the <code>getNext</code> method.  In the constructor it will create an <code>ArrayList</code> and fill it by looping through the array and adding each string to the list.  In <code>getNext</code> it will return "NONE" if the length of the list is 0.  Otherwise, it will calculate a random index in the list, remove the string at that index, and return it. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class RandomStringChooser
   {

       /* fields */
       private List<String> words;

       /* constructor */
       public RandomStringChooser(String[] wordArray)
       {
   =====
           words = new ArrayList<String>();
   =====
           wordList = new ArrayList<String>(); #paired
   =====
           for (int i = 0; i < wordArray.length; i++)
           {
               words.add(wordArray[i]);
           } // end for loop
   =====
       } // end RandomStringChooser Constructor
   =====

       /* getNext method */
       public String getNext()
       {
           int pos = 0;

           if (words.size() == 0)
           {
   =====
               return "NONE";
   =====
           } // end if words.size() equals 0
   =====
           pos = (int) (Math.random() * words.size());
   =====
           pos = Math.random() * words.size(); #paired
   =====
           return words.remove(pos);
   =====
       } // end getNext()
   } // end class