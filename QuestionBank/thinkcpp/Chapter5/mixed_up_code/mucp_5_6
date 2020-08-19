.. parsonsprob:: mucp_5_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: mixed_up_code
   :topics: Chapter5/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :practice: T

   On a distant planet, depending on the characteristics of an egg, a kenchic,
   an ooseg, or a guinpen might hatch from it. Let's write the function
   ``birdType`` which returns an ``int`` corresponding to each type of bird
   (1 for kenchic, 2 for ooseg, and 3 for guinpen). If the egg is round, then it is a
   guinpen. But if the egg is round and it isn't gray, then it is a kenchic. If
   the egg isn't round or it is gray, then it's an ooseg.
   Put the necessary blocks of code in the correct order.
   -----
   int birdType (bool isRound, bool isGray) {
   =====
   void birdType (bool isRound, bool isGray) {  #distractor
   =====
   double birdType (int isRound, char isGray) {  #distractor
   =====
      if (isRound && !isGray) {
   =====
      if (!isRound && !isGray) {  #paired
   =====
         return 1;
      }
   =====
      else if (!isRound || isGray) {
   =====
      else if (!(isRound || isGray)) {  #paired
   =====
         return 2;
      }
   =====
      else {
   =====
         return 3;
      }
   =====
         return 0;  #distractor
      }
   =====
   }