.. parsonsprob:: ch16FrRSC1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: FreeResponse
   :subchapter: RandomStringChooserParsons1
   :topics: FreeResponse/RandomStringChooserParsons1
   :from_source: F
   :adaptive:
   :noindent:

   The code below will copy the array of strings to a list in the constructor using a for each loop.  In ``getNext`` it will check if the list length is greater than zero and if it is it will pick a position at random in the list and remove the item from that position and return it.  Otherwise the list is empty so it returns "NONE".  The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
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
           words = new List<String>(); #paired
   =====
           for (String singleWord : wordArray)
           {
   =====
               words.add(singleWord);
   =====
               words.add(singleword); #paired
   =====
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
   =====
       } // end getNext()
   } // end class