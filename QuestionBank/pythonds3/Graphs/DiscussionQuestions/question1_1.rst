.. mchoice:: question1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Graphs
   :subchapter: DiscussionQuestions
   :topics: Graphs/DiscussionQuestions
   :from_source: T
   :answer_a: O(n)
   :answer_b: O(n<sup>2</sup>)
   :answer_c: O(1)
   :answer_d: O(n<sup>3</sup>)
   :correct: b
   :feedback_a: O(n) would suggest that there is no nesting. There are several nested for loops.
   :feedback_b: Correct. The two consecutively nested for loops would dictate that this is in the realm of O(n<sup>2</sup>).
   :feedback_c: O(1) would suggest that the function is constant. Since there are multiple for loops intertwined, it is not in constant time.
   :feedback_d: O(n<sup>3</sup>) would suggest that there are three consecutively nested for loops. There are only two.

   4. What is the Big-O running time of the ``buildGraph`` function?