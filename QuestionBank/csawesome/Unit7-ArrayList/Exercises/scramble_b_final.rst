.. parsonsprob:: scramble_b_final
   :author: Leonardo Alvarez
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: Exercises
   :topics: Unit7-ArrayList/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 11
   :num_students_correct: 9.0
   :mean_clicks_to_correct: 10.8888888889

   Solve my really cool parsons problem...if you can.
   -----
   public static void scrambleOrRemove(List<String> wordList) {
   =====
       int index = 0;
   =====
      while (index < wordList.size() ) {
   =====
          String word = wordList.get(index);
          String scrambled = scrambleWord(word);
   =====
          if (word.equals(scrambled)) {
                 wordList.remove(index);
          }
   =====
          else   {
   =====
              wordList.set(index, scrambled);
   ===== 
              index++; 
   =====
          } //end if statement
   =====
     } // end while 
   =====
   } // end method