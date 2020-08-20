.. parsonsprob:: question13_5_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: deck_member_functions
   :topics: Chapter13/deck_member_functions
   :from_source: F
   :numbered: left
   :adaptive:

   Write ``find`` as a ``Deck`` member function that takes a ``Card`` as a parameter.
   -----
   int Deck::find (Card card) const {
   =====
   int find (Card) {                         #paired
   =====
      for (size_t i = 0; i &#60; cards.size(); i++) {
   =====
      for (size_t i = 0; i &#60; deck.cards.size(); i++) {                       #paired
   =====
         if (cards[i].equals(card)) {
            return i;
         }
   =====
         if (equals (deck.cards[i], *this)) {                         #paired
            return i;
         }
   =====
      }
      return -1;
   }