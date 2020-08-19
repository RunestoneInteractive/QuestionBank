.. parsonsprob:: mergesort_help_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: mergesort
   :topics: Chapter13/mergesort
   :from_source: T
   :numbered: left
   :adaptive:

   First, let's write the code for the merge function. merge should
   take two decks as parameters and return a deck with the deck merged.
   -----
   Deck merge (const Deck& d1, const Deck& d2) {
   =====
   void merge (const Deck& d1, const Deck& d2) {                         #paired
   =====
    Deck result (d1.cards.size() + d2.cards.size());
   =====
    size_t i = 0;
    size_t j = 0;
   =====
    for (size_t k = 0; k < result.cards.size(); ++k) {
   =====
     if (d1.cards.empty()) {
      result.cards[k] = d2.cards[j];
      ++j;
     }
   =====
     if (d1.cards.empty()) {
      result.cards[k] = d1.cards[i];                         #paired
      ++i;
     }
   =====
     else if (d2.cards.empty()) {
      result.cards[k] = d1.cards[i];
      ++i;
     }
   =====
     else if (d1.cards.empty()) {
      result.cards[k] = d2.cards[j];                         #paired
      ++j;
     }
   =====
     else {
   =====
      if (j >= d2.cards.size()) {
       result.cards[k] = d1.cards[i];
       ++i;
      }
   =====
      else if (i >= d1.cards.size() || d1.cards[i].isGreater(d2.cards[j])) {
       result.cards[k] = d2.cards[j];
       ++j;
      }
   =====
      else {
       result.cards[k] = d1.cards[i];
       ++i;
      }
     }
   =====
    }
    return result;
   }