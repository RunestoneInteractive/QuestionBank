.. parsonsprob:: question13_10_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: mergesort
   :topics: Chapter13/mergesort
   :from_source: F
   :numbered: left
   :adaptive:

   Let's write the code for the ``mergeSort`` function. ``mergeSort``
   should be a ``Deck`` member function that returns a sorted deck.
   -----
   Deck Deck::mergeSort () const {
   =====
   Deck mergeSort () {                         #paired
   =====
      int mid = cards.size() / 2;
   =====
      Deck d1 = subdeck(0, mid - 1);
      Deck d2 = subdeck(mid, cards.size() - 1);
   =====
      d1.sortDeck();
      d2.sortDeck();
   =====
      return merge(d1, d2);
   }