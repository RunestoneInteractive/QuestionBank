.. mchoice:: yet_another_example_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: yet_another_example
   :topics: Chapter11/yet_another_example
   :from_source: T
   :answer_a: Before the parameter list.
   :answer_b: Inside the parameter list.
   :answer_c: After the parameter list.
   :answer_d: Implicit parameters are always const and don't need to be declared.
   :correct: c
   :feedback_a: Incorrect! Try again!
   :feedback_b: Incorrect! This would be correct if we were talking about a free-standing function.
   :feedback_c: Correct!
   :feedback_d: Incorrect! Parameters are only const if they are not modified inside the function, implicit parameters are no exception.

   When writing a member function, where should you declare the implicit parameter to be ``const``?