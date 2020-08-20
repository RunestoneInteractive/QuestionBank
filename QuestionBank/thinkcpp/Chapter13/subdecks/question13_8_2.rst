.. mchoice:: question13_8_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: subdecks
   :topics: Chapter13/subdecks
   :from_source: F
   :practice: T
   :answer_a: 4
   :answer_b: 9
   :answer_c: 49
   :answer_d: Invalid num! Please try again.
   :answer_e: Code will not run.
   :correct: c
   :feedback_a: Incorrect! Try running it with the active code.
   :feedback_b: Incorrect! Try running it with the active code.
   :feedback_c: Correct!
   :feedback_d: Incorrect! Try running it with the active code.
   :feedback_e: Incorrect! Try running it with the active code.

   What is the correct output of the code below?

   .. code-block:: cpp

      int main() {
        Deck deck;
        Deck sub = deck.subdeck(0, 12);
        clubs.print();
        Card card1 (CLUBS, SEVEN);
        Card card2 (DIAMONDS, KING);
        cout << endl;
        cout << "The Seven of Clubs is at index " << findBisect (clubs, card1) << endl;
        cout << "The King of Diamonds is at index " << findBisect (clubs, card2) << endl;
      }