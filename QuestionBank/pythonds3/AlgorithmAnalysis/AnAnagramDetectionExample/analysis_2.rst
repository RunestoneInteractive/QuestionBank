.. mchoice:: analysis_2
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
    :correct: a
    :feedback_b: Be careful, in counting loops you want to make sure the loops are nested.
    :feedback_d: Be careful, in counting loops you want to make sure the loops are nested.
    :feedback_c: log n typically is indicated when the problem is iteratvely made smaller
    :feedback_a: Even though there are two loops they are not nested.  You might think of this as O(2n) but we can ignore the constant 2.
    :pct_on_first: 0.7894736842
    :total_students_attempting: 19
    :num_students_correct: 18
    :mean_clicks_to_correct: 1.1666666667

    Given the following code fragment what is its Big-O running time?
    
    .. code-block:: python
    
      test = 0
      for i in range(n):
         test = test + 1
    
      for j in range(n):
         test = test - 1