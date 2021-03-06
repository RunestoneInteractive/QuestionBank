.. parsonsprob:: subdecks_help_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: subdecks
   :topics: Chapter13/subdecks
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for this version of the findBisect function.
   findBisect should take a subdeck and a card as parameters and
   return the index of the card in the subdeck or -1 if it's not found.
   -----
   int findBisect (Deck subdeck, Card card) {
   =====
   int findBisect (Subdeck subdeck, Card card) {                         #paired
   =====
    if (subdeck.size() == 1 && !subdeck[0].equals(card)) return -1;
   =====
     int mid = subdeck.size() / 2;
   =====
     int mid = (high + low) / 2;                         #paired
   =====
    if (subdeck[mid].equals(card)) return mid;
   =====
    else if (subdeck[mid].isGreater(card)) {
     return findBisect (subdeck.subdeck(0, mid - 1), card);
    }
   =====
    else if (subdeck[mid].isGreater(card)) {                         #paired
     return findBisect (subdeck.subdeck(mid + 1, subdeck.size()), card);
    }
   =====
    else {
     return findBisect (subdeck.subdeck(mid + 1, subdeck.size()), card);
    }
   }