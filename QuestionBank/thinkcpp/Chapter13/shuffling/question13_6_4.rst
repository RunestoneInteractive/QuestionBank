.. parsonsprob:: question13_6_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: shuffling
   :topics: Chapter13/shuffling
   :from_source: F
   :numbered: left
   :adaptive:

   Let's write the code for the ``shuffleDeck`` function. We'll use ``randomInt``
   and ``swapCards`` in our implementation of ``shuffleDeck``.
   -----
   void Deck::shuffleDeck () {
   =====
   Deck Deck::shuffleDeck (Deck deck) {                         #paired
   =====
      for (size_t i = 0; i < cards.size(); i++) {
   =====
         int x = randomInt (i, cards.size() - 1);
   =====
         int x = randomInt (i, cards.size());                         #paired
   =====
         swapCards (i, x);
      }
   }