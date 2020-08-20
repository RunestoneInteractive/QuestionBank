.. mchoice:: decks_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: decks
   :topics: Chapter13/decks
   :from_source: T
   :answer_a: The ranks amd suits of the cards are initialized to the proper ranks and suits in a standard deck of cards.
   :answer_b: There will be 52 cards.
   :answer_c: The ranks and suits will be initialized to their default values.
   :answer_d: The only instance variable in the deck is cards.
   :answer_e: You can't access individual cards in the deck.
   :correct: b,c,d
   :feedback_a: Unless you the programmer tell it to, the computer won't do it.
   :feedback_b: We initialized cards with a value of 52.
   :feedback_c: In our case is, the default values are zero.
   :feedback_d: cards is a vector of Cards!
   :feedback_e: You can access any card by indexing, for example: deck.cards[n].

   Take a look at the state diagram above. When we create a deck of cards using ``Deck deck (52)``,
   what is true about our new deck?