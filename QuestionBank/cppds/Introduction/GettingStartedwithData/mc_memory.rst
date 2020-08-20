.. mchoice:: mc_memory
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: GettingStartedwithData
  :topics: Introduction/GettingStartedwithData
  :from_source: T
  :answer_a: using ``&``
  :answer_b: using ``*``
  :answer_c: using ``id``
  :answer_d: It depends upon the implementation.
  :answer_e: none of the above
  :correct: a
  :feedback_a: Right! ``&`` is the "address-of" operator, used to reference an address.
  :feedback_b: No. ``int *p;`` defines a pointer to an integer, and ``*p`` would dereference that pointer, i.e. retrieve the data that p points to.
  :feedback_c: No. This is used in other languages such as Python.
  :feedback_d: No. The implementation remains consistent.
  :feedback_e: One of the above is indeed correct.
  :pct_on_first: 0.6234567901
  :total_students_attempting: 162
  :num_students_correct: 161
  :mean_clicks_to_correct: 1.5838509317

  How may one reference a variable's memory address in C++?