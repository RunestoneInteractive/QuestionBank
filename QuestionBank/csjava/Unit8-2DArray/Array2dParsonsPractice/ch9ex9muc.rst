.. parsonsprob:: ch9ex9muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit8-2DArray/Array2dParsonsPractice
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   The following program segment is a method that should accept a two-dimensional String array, in which each row contains the characters of a word.  The method should return a single-dimensional (normal) String array containing the words in each row of the two-dimensional array.

   Take for example, the input 2d array: { {"b", "a", "t", "h"},
                                          {"t", "e", "n", "s"},
                                          {"j", "a", "c", "k"},
                                          {"l", "a", "z", "y"}}

   Resulting array: {"bath", "tens", "jack", "lazy"}

   But, the blocks have been mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public static String[] breakIntoLetters(String[][] words) {
   =====
      String[] result = new String[words.length];
   =====
      for (int i = 0; i < words.length; i++) {
   =====
          String word = "";
   =====
          for (int j = 0; j < words[i].length; j++) {
              word += words[i][j];
          }
   =====
          result[i] = word;
   =====
      } //end for loop
      return result;
   =====
   } //end method