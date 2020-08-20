.. parsonsprob:: StringScrambleB1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit8-ArrayList
  :subchapter: stringScrambleB
  :topics: Unit8-ArrayList/stringScrambleB
  :from_source: T
  :numbered: left
  :adaptive:

  The method test below contains the correct code for one solution to this problem, but it is mixed up.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
  -----
  public static void test(List<String> wordList) {
  =====
    int i = 0;
    while (i < wordList.size()) {
  =====
       String current = wordList.get(i);
       String scrambled = scrambleWord(current);
  =====
       if (scrambled.equals(current))
  =====
          wordList.remove(i);
  =====
       else
       {
  =====
          wordList.set(i,scrambled);
  =====
          i++;
  =====
       } // end else
  =====
    } // end while
  =====
  } // end method