.. mchoice:: question1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: Graphs
   :subchapter: DiscussionQuestions
   :topics: Graphs/DiscussionQuestions
   :from_source: T
   :answer_a: O(1)
   :answer_b: O(n<sup>3</sup>)
   :answer_c: O(n)
   :answer_d: O(n<sup>2</sup>)
   :correct: d
   :feedback_a: O(1) would mean that the algorithm runs in constant time. This isn't true because there are several comparisons happening in the algorithm.
   :feedback_b: O(n<sup>3</sup>) suggests that there are three consecutively nested loops. If you look at the example algorithm, it is obvious that there are not three nested loops.
   :feedback_c: O(n) is linear time. The time it takes for this program to run doesn't grow linearly.
   :feedback_d: Correct. Since you are not only comparing the weight of a branch but also if the branch has already been connected to, this would make the Big-O of the algorithm O(n<sup>2</sup>)
   :pct_on_first: 0.2478632479
   :total_students_attempting: 117
   :num_students_correct: 115.0
   :mean_clicks_to_correct: 2.2956521739

   12. What is the Big-O running time for Prim’s minimum
    spanning tree algorithm?