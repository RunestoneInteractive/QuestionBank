.. mchoice:: deck_members_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter13
   :subchapter: deck_member_functions
   :topics: Chapter13/deck_member_functions
   :from_source: T
   :multiple_answers:
   :answer_a: Use the keyword this.
   :answer_b: Define Deck before Card.
   :answer_c: Pass a Card parameter in the Card member function find.
   :answer_d: Declare Deck before Card and then define Deck afterwards.
   :correct: a,d
   :feedback_a: We use this to refer to the Card that the function is invoked on.
   :feedback_b: We don't have to define Deck before Card.
   :feedback_c: What do we pass as a parameter in find?
   :feedback_d: This is how we implemented our code!

   Multiple Response: What are some tricks we can use to write ``find`` as a ``Card`` member function?