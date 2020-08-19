.. activecode:: shuffling_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: shuffling
   :topics: Chapter13/shuffling
   :from_source: T
   :language: cpp

   Try writing the ``randomInt`` and ``swapCards`` functions in the commented sections
   of the active code below. Once you're done with ``randomInt`` and ``swapCards``,
   try using them to implement the ``Deck`` member function ``shuffleDeck``. If done correctly,
   the program should output a shuffled deck of cards. If you stuck, you can reveal the
   extra problems at the end for help.
   ~~~~
   #include <iostream>
   #include <string>
   #include <vector>
   #include <cstdlib>
   using namespace std;

   enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES };

   enum Rank { ACE=1, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,
   TEN, JACK, QUEEN, KING };

   int randomInt (int low, int high) {
       // ``randomInt`` should choose a random integer between
       // the low and high parameters and return an integer.
       // Delete the return 0 and write your implementation here.
       return 0;
   }

   struct Card {
       Rank rank;
       Suit suit;
       Card ();
       Card (Suit s, Rank r);
       void print () const;
   };

   struct Deck {
       vector<Card> cards;
       Deck ();
       void print () const;
       void swapCards (int index1, int index2);
       void shuffleDeck ();
   };

   void Deck::swapCards (int index1, int index2) {
       // ``swapCards`` should take two indices and switch the cards
       // at the indicated positions. Write your implementation here.
   }

   void Deck::shuffleDeck () {
       // Follow the pseudocode from above and use ``randomInt`` and
       // ``swapCards`` to write the ``shuffle`` member function.
       // Write your implementation here.
   }

   int main() {
       Deck deck;
       deck.shuffleDeck ();
       deck.print ();
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