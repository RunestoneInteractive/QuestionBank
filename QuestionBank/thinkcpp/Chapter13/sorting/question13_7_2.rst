.. parsonsprob:: question13_7_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: sorting
   :topics: Chapter13/sorting
   :from_source: F
   :numbered: left
   :adaptive:

   Let's write the code for the ``sortDeck`` function. We'll use ``findLowestCard``
   and ``swapCards`` in our implementation of ``sortDeck``.
   -----
   void Deck::sortDeck () {
   =====
   Deck::sortDeck () {                         #paired
   =====
      for (size_t i = 0; i < cards.size(); i++) {
   =====
         int x = findLowestCard (i);
   =====
         int x = findLowestCard (cards.size());                         #paired
   =====
         swapCards (i, x);
      }
   }