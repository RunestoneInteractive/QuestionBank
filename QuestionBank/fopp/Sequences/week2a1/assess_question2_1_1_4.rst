.. mchoice:: assess_question2_1_1_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: T
   :answer_a: ['travel', 'lights', 'moon']
   :answer_b: ['world', 'travel', 'lights']
   :answer_c: ['travel', 'lights']
   :answer_d: ['world', 'travel']
   :correct: c
   :feedback_a: When we take a slice of something, it includes the item at the first index and excludes the item at the second index.
   :feedback_b: When we take a slice of something, it includes the item at the first index and excludes the item at the second index. Additionally, Python is a zero-index based language.
   :feedback_c: Yes, python is a zero-index based language and slices are inclusive of the first index and exclusive of the second.
   :feedback_d: Python is a zero-index based language.
   :practice: T

   What will the output be for the following code?

   .. sourcecode:: python

    ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
    new = ls[2:4]
    print(new)