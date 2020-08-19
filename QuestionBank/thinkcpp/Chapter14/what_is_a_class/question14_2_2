.. mchoice:: question14_2_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter14
   :subchapter: what_is_a_class
   :topics: Chapter14/what_is_a_class
   :from_source: T
   :practice: T
   :answer_a: Remove the ``private:`` label.
   :answer_b: Change ``struct`` to ``class`` and remove the ``public:`` label.
   :answer_c: Remove the ``public:`` label.
   :answer_d: Change ``struct`` to ``class``.
   :correct: b
   :feedback_a: Incorrect! ``Deck`` is still a ``struct``.
   :feedback_b: Incorrect! We don't want to make the constructors and all member functions private.
   :feedback_c: Incorrect! We don't want to make the constructors and all member functions private.
   :feedback_d: Correct! ``Deck`` is now a ``class`` and it's okay that we kept the ``private:`` label.

   How can we change ``Deck``, which is currently a ``struct``, into a ``class``?

   .. code-block:: cpp

      struct Deck {
      private:
        vector<Card> cards;

      public:
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