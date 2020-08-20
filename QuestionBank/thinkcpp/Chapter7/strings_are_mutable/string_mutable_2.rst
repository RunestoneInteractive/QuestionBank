.. mchoice:: string_mutable_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: strings_are_mutable
   :topics: Chapter7/strings_are_mutable
   :from_source: T
   :practice: T
   :answer_a: message[9] = "w";
   :answer_b: message[10] = "w";
   :answer_c: "w" = message[9];
   :answer_d: message[8] = "w";
   :correct: a
   :feedback_a: Since "l" is at index 9, replacing it with "w" fixes the message.
   :feedback_b: Remember indexing starts at 0.
   :feedback_c: In order to change a letter in a string, the ``[]`` operator must be on the left of the assignment.
   :feedback_d: Remember indexing starts at 0.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   How can we fix the message to be "You're a wizard Harry"?
   
   .. code-block:: cpp
   
      string message = "You're a lizard Harry";