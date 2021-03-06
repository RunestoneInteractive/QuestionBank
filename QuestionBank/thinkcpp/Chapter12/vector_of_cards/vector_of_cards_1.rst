.. mchoice:: vector_of_cards_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter12
   :subchapter: vector_of_cards
   :topics: Chapter12/vector_of_cards
   :from_source: T
   :multiple_answers:
   :answer_a: There are 16 cards in the deck.
   :answer_b: The deck is single-suited.
   :answer_c: There are no face cards in the deck.
   :answer_d: The deck does not contain any Hearts.
   :answer_e: There are two Jacks in the deck.
   :correct: a,d,e
   :feedback_a: Correct! You can verify this by checking how many times the for loops execute.
   :feedback_b: Incorrect! Look at the conditions of the outer for loop, you'll find that there are two suits in this deck.
   :feedback_c: Incorrect! Look at the conditions of the inner for loop, you'll find that this deck contains face cards.
   :feedback_d: Correct! The two suits in this deck are Clubs and Diamonds.
   :feedback_e: Correct! The deck contains the Jack of Clubs and the Jack of Diamonds.

   Take a look at the code below. What can we say about the deck that is created?
   ::

     vector<Card> createDeck() {
        vector<Card> deck (16);
        int i = 0;
        for (int suit = 0; suit <= 1; suit++) {
           for (int rank = 4; rank <= 11; rank++) {
              deck[i].suit = suit;
              deck[i].rank = rank;
              i++;
           }
        }
        return deck;
     }