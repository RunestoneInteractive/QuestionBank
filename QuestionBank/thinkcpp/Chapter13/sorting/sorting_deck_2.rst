.. activecode:: sorting_deck_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: sorting
   :topics: Chapter13/sorting
   :from_source: T
   :language: cpp

   Try writing the ``findLowestCard`` function in the commented section
   of the active code below. Once you're done with ``findLowestCard``,
   try using it along with ``swapCards`` to implement the ``Deck`` member
   function ``sortDeck``. If done correctly, the program should output a
   sorted deck of cards. If you get stuck, you can reveal the extra problems
   at the end for help.
   ~~~~
   #include <iostream>
   #include <string>
   #include <vector>
   #include <cstdlib>
   using namespace std;

   enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES };

   enum Rank { ACE=1, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE,
   TEN, JACK, QUEEN, KING };

   int randomInt (int low, int high);

   struct Card {
       Rank rank;
       Suit suit;
       Card ();
       Card (Suit s, Rank r);
       void print () const;
       bool isGreater (const Card& c2) const;
   };

   struct Deck {
       vector<Card> cards;
       Deck ();
       void print () const;
       void swapCards (int index1, int index2);
       int findLowestCard (int index);
       void shuffleDeck ();
       void sortDeck ();
   };

   int Deck::findLowestCard (int index) {
       // ``findLowestCard`` should search through the vector of cards
       // starting at index and return the index of the smallest card.
       // Delete the return 0 and write your implementation here.
       return 0;
   }

   void Deck::sortDeck () {
       // Follow the pseudocode from above and use ``findLowestCard`` and
       // ``swapCards`` to write the ``sort`` member function.
       // Write your implementation here.
   }

   int main() {
       Deck deck;
       deck.shuffleDeck ();
       deck.sortDeck ();
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

   bool Card::isGreater (const Card& c2) const {
       if (suit > c2.suit) return true;
       if (suit < c2.suit) return false;
       if (rank > c2.rank) return true;
       if (rank < c2.rank) return false;
       return false;
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

   int randomInt (int low, int high) {
       srand (time(NULL));
       int x = random ();
       int y = x % (high - low + 1) + low;
       return y;
   }

   void Deck::swapCards (int index1, int index2) {
       Card temp = cards[index1];
       cards[index1] = cards[index2];
       cards[index2] = temp;
   }

   void Deck::shuffleDeck () {
       for (size_t i = 0; i < cards.size(); i++) {
           int x = randomInt (i, cards.size() - 1);
           swapCards (i, x);
       }
   }