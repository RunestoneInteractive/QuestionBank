.. activecode:: deck_members_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: deck_member_functions
   :topics: Chapter13/deck_member_functions
   :from_source: T
   :language: cpp

   The active code below uses the ``find`` function that we just wrote.
   ~~~~
   #include <iostream>
   #include <string>
   #include <vector>
   using namespace std;

   enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES };

   enum Rank { ACE=1, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,
   TEN, JACK, QUEEN, KING };

   struct Card {
       Rank rank;
       Suit suit;
       Card ();
       Card (Suit s, Rank r);
       void print () const;
       bool equals (const Card& c2) const;
   };

   struct Deck {
       vector<Card> cards;
       Deck ();
       void print () const;
       int find (Card card) const;
   };

   int main() {
       Deck deck;
       Card card (CLUBS, ACE);
       Card card2 (DIAMONDS, ACE);
       // Should output 0 and 13
       cout << deck.find(card) << endl;
       cout << deck.find(card2) << endl;
   }

   ====
   Card::Card () {
       suit = SPADES;  rank = ACE;
   }

   Card::Card (Suit s, Rank r) {
       suit = s;  rank = r;
   }

   void Card::print () const {
       vector<string> suits (4);
       suits[0] = "Clubs";
       suits[1] = "Diamonds";
       suits[2] = "Hearts";
       suits[3] = "Spades";

       vector<string> ranks (14);
       ranks[1] = "Ace";
       ranks[2] = "2";
       ranks[3] = "3";
       ranks[4] = "4";
       ranks[5] = "5";
       ranks[6] = "6";
       ranks[7] = "7";
       ranks[8] = "8";
       ranks[9] = "9";
       ranks[10] = "10";
       ranks[11] = "Jack";
       ranks[12] = "Queen";
       ranks[13] = "King";

       cout << ranks[rank] << " of " << suits[suit] << endl;
   }

   Deck::Deck () {
       vector<Card> temp (52);
       cards = temp;

       int i = 0;
       for (Suit suit = CLUBS; suit <= SPADES; suit = Suit(suit+1)) {
           for (Rank rank = ACE; rank <= KING; rank = Rank(rank+1)) {
               cards[i].suit = suit;
               cards[i].rank = rank;
               i++;
           }
       }
   }

   void Deck::print () const {
       for (size_t i = 0; i < cards.size(); i++) {
           cards[i].print ();
       }
   }

   int Deck::find (Card card) const {
       for (size_t i = 0; i &#60; cards.size(); i++) {
           if (cards[i].equals(card)) {
               return i;
           }
       }
       return -1;
   }

   bool Card::equals (const Card& c2) const {
       return (rank == c2.rank && suit == c2.suit);
   }