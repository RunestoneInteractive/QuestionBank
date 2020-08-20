.. mchoice:: analysis_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: AlgorithmAnalysis
    :subchapter: AnAnagramDetectionExample
    :topics: AlgorithmAnalysis/AnAnagramDetectionExample
    :from_source: T
    :answer_a: O(n)
    :answer_b: O(n^2)
    :answer_c: O(log n)
    :answer_d: O(n^3)
    :correct: c
    :feedback_a: Look carefully at the loop variable i.  Notice that the value of i is cut in half each time through the loop.  This is a big hint that the performance is better than O(n)
    :feedback_b: Check again, is this a nested loop?
    :feedback_d: Check again, is this a nested loop?
    :feedback_c: The value of i is cut in half each time through the loop so it will only take log n iterations.
    :pct_on_first: 0.6470588235
    :total_students_attempting: 17
    :num_students_correct: 17
    :mean_clicks_to_correct: 1.4117647059

    Given the following code fragment what is its Big-O running time?
    
    .. code-block:: python
    
      i = n
      while i > 0:
         k = 2 + 2
         i = i // 2