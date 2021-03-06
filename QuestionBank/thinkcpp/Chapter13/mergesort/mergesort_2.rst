.. activecode:: mergesort_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: mergesort
   :topics: Chapter13/mergesort
   :from_source: T
   :language: cpp

   Write your implementation of ``merge`` in the commented area of the active
   code below. Read the comments in ``main`` to see how we'll test if your
   ``merge`` function works. If you get stuck, you can reveal the extra problem
   at the end for help.
   ~~~~
   #include <iostream>
   #include <string>
   #include <vector>
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
       bool equals (const Card& c2) const;
   };

   struct Deck {
       vector<Card> cards;
       Deck ();
       Deck (int n);
       void print () const;
       void swapCards (int index1, int index2);
       int findLowestCard (int index);
       void shuffleDeck ();
       void sortDeck ();
       Deck subdeck (int low, int high) const;
   };

   int findBisect (Deck subdeck, Card card);

   Deck merge (const Deck& d1, const Deck& d2) {
       // ``merge`` should merge d1 with d2 and return
       // a merged deck. Follow the pseudocode above,
       // delete the existing code, and write your
       // implementation here.
       Deck deck(0); return deck;
   }

   int main() {
       Deck deck;

       // Shuffle a deck of cards and split it in half
       deck.shuffleDeck();
       Deck d1 = deck.subdeck(0, 25);
       Deck d2 = deck.subdeck(26, 51);

       // Sort each half
       d1.sortDeck();
       d2.sortDeck();
       cout << "Sorted first half:" << endl;
       d1.print();
       cout << endl;
       cout << "Sorted second half:" << endl;
       d2.print();
       cout << endl;

       // Merge sorted decks together
       Deck finished = merge(d1, d2);

       // We should see a sorted standard deck of 52 cards
       cout << "Merged sorted full deck:" << endl;
       finished.print();
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

   bool Card::equals (const Card& c2) const {
       return (rank == c2.rank && suit == c2.suit);
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

   Deck::Deck (int size) {
       vector<Card> temp (size);
       cards = temp;
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

   int Deck::findLowestCard (int index) {
       int min = index;
       for (size_t i = index; i < cards.size(); ++i) {
           if (cards[min].isGreater(cards[i])) {
               min = i;
           }
       }
       return min;
   }

   Deck Deck::subdeck (int low, int high) const {
       Deck sub (high-low+1);

       for (size_t i = 0; i<sub.cards.size(); i++) {
           sub.cards[i] = cards[low+i];
       }
       return sub;
   }

   int findBisect (Deck subdeck, Card card) {
      if (subdeck.cards.size() == 1 && !subdeck.cards[0].equals(card)) return -1;
      int mid = subdeck.cards.size() / 2;
      if (subdeck.cards[mid].equals(card)) return mid;
      else if (subdeck.cards[mid].isGreater(card)) {
          return findBisect (subdeck.subdeck(0, mid - 1), card);
      }
      else {
          return findBisect (subdeck.subdeck(mid + 1, subdeck.cards.size()), card);
      }
   }

   void Deck::shuffleDeck () {
       for (size_t i = 0; i < cards.size(); i++) {
           int x = randomInt (i, cards.size() - 1);
           swapCards (i, x);
       }
   }

   void Deck::sortDeck () {
       for (size_t i = 0; i < cards.size(); i++) {
           int x = findLowestCard (i);
           swapCards (i, x);
       }
   }