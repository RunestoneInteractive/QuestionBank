.. parsonsprob:: ch17RandStrA1
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

   The mixed up code below includes the correct code for the class, a field, a constructor, and the <code>getNext</code> method.  In the constructor it will create an <code>ArrayList</code> and fill it by looping through the array and adding each string to the list.  In the <code>getNext</code> method, if the list length is greater than zero, it will pick a position at random in the list and remove the item from that position and return it.  Otherwise, if the list is empty, it returns "NONE".  The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class RandomStringChooser
   {
   =====
       /* fields */
       private List<String> words;
   =====
       /* fields */
       public List<String> words; #paired
   =====
       /* constructor */
       public RandomStringChooser(String[] wordArray)
       {
   =====
           words = new ArrayList<String>();
   =====
           for (String singleWord : wordArray)
           {
               words.add(singleWord);
           } // end for each word in wordArray

       } // end RandomStringChooser Constructor
   =====

       /* getNext method */
       public String getNext()
       {
           int pos = 0;
   =====
           if (words.size() > 0)
           {
   =====
               pos = (int) (Math.random() * words.size());
   =====
               pos = Math.random() * words.size(); #paired
   =====
               return words.remove(pos);
   =====
               return words.get(pos); #paired
   =====
           } // end if words.size() > 0
   =====
           return "NONE";
       } // end getNext()
   } // end class