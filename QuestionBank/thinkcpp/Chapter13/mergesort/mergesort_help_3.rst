.. parsonsprob:: mergesort_help_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: mergesort
   :topics: Chapter13/mergesort
   :from_source: T
   :numbered: left
   :adaptive:

   Let's take it one step further and rewrite ``mergeSort`` as a
   recursive function.
   -----
   Deck Deck::mergeSort (Deck deck) const {
   =====
    if (deck.cards.size() == 0 || deck.cards.size() == 1) {
     return deck;
    }
   =====
    int mid = deck.cards.size() / 2;
   =====
    Deck d1 = subdeck(0, mid - 1);
    Deck d2 = subdeck(mid, deck.cards.size() - 1);
   =====
    Deck merged1 = d1.mergeSort(d1);
    Deck merged2 = d2.mergeSort(d2);
   =====
    return merge(merged1, merged2);
   }