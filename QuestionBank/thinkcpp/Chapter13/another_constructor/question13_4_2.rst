.. parsonsprob:: question13_4_2
      :author: bmiller
      :difficulty: 3.0
      :basecourse: thinkcpp
      :chapter: Chapter13
      :subchapter: another_constructor
      :topics: Chapter13/another_constructor
      :from_source: F
      :numbered: left
      :adaptive:

      Let's write a constructor for a deck of cards that uses 40 cards.
      This deck uses all 4 suits and ranks Ace through 10, omitting all
      face cards.
      -----
      Deck::Deck () {
      =====
         vector<Card> temp (40);
      =====
         vector<Card> temp (52);                         #paired
      =====
         cards = temp;
         int i = 0;
      =====
         for (Suit suit = CLUBS; suit <= SPADES; suit = Suit(suit+1)) {
      =====
         for (Suit suit = CLUBS; suit < SPADES; suit = Suit(suit+1)) {                         #paired
      =====
            for (Rank rank = ACE; rank <= TEN; rank = Rank(rank+1)) {
      =====
            for (Rank rank = ACE; rank <= KING; rank = Rank(rank+1)) {                         #paired
      =====
              cards[i].suit = suit;
              cards[i].rank = rank;
      =====
              cards[i].suit = rank;
              cards[i].rank = suit;                         #paired
      =====
              i++;
            }
         }
      }