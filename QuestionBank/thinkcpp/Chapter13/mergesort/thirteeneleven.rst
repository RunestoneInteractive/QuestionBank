.. activecode:: thirteeneleven
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: mergesort
   :topics: Chapter13/mergesort
   :from_source: F
   :language: cpp

   Now that we've written ``merge``, it's time to write the ``mergeSort`` function. Try writing
   the non-recursive version of ``mergeSort`` first before writing the recursive version. Follow the
   comments in ``main`` to test your functions. If done correctly, the program should output a sorted
   deck of cards. If you get stuck, you can reveal the extra problems at the end for help.
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
     Deck mergeSort () const;
     Deck mergeSort (Deck deck) const;
   };

   int findBisect (Deck subdeck, Card card);
   Deck merge (const Deck& d1, const Deck& d2);

   Deck Deck::mergeSort () const {
     // This version of ``mergeSort`` is the non-recursive version.
     // Follow the pseudocode above delete the existing code,
     // and write your implementation here.
     Deck deck(0); return deck;
   }

   Deck Deck::mergeSort (Deck deck) const {
     // This version of ``mergeSort`` is the recursive version.
     // Follow the pseudocode above delete the existing code,
     // and write your implementation here.
     Deck deck1(0); return deck;
   }

   int main() {
     Deck deck1;
     deck1.shuffleDeck();
     Deck sorted1 = deck1.mergeSort();
     sorted1.print();

     // Once you get the above code to work, comment it
     // out and uncomment the code below to test the
     // recursive version of ``mergeSort``.

     /*
     Deck deck2;
     deck2.shuffleDeck();
     Deck sorted2 = deck2.mergeSort(deck2);
     sorted2.print();
     */
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

   bool Card::equals (const Card& c2) const
    {
      return (rank == c2.rank && suit == c2.suit);
    }

   Deck::Deck ()
   {
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

   Deck::Deck (int size)
   {
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

   Deck merge (const Deck& d1, const Deck& d2) {
      Deck result (d1.cards.size() + d2.cards.size());
      size_t i = 0;
      size_t j = 0;
      for (size_t k = 0; k < result.cards.size(); ++k) {
         if (d1.cards.empty()) {
            result.cards[k] = d2.cards[j];
            ++j;
         }
         else if (d2.cards.empty()) {
            result.cards[k] = d1.cards[i];
            ++i;
         }
         else {
            if (j >= d2.cards.size()) {
               result.cards[k] = d1.cards[i];
               ++i;
            }
            else if (i >= d1.cards.size() || d1.cards[i].isGreater(d2.cards[j])) {
               result.cards[k] = d2.cards[j];
               ++j;
            }
            else {
               result.cards[k] = d1.cards[i];
               ++i;
            }
         }
      }
      return result;
   }