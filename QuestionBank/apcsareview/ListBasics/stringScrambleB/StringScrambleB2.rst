.. parsonsprob:: StringScrambleB2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: ListBasics
  :subchapter: stringScrambleB
  :topics: ListBasics/stringScrambleB
  :from_source: T

  The method test below contains the correct code for another solution to this problem, but it is mixed up and contains extra blocks that are not needed.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
  -----

  public static void test(List<String> wordList) {
  =====
     for (int i = wordList.size() - 1; i >= 0; i--) {
  =====
        String word = wordList.get(i);
  =====
        String scrambled = scrambleWord(word);
  =====
        if (!scrambled.equals(word))
  =====
           wordList.set(i, scrambled);
  =====
        else
  =====
           wordList.remove(i);
  =====
     } // end for
  =====
  } // end method