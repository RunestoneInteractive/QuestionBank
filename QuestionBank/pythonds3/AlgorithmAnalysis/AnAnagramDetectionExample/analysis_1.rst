.. mchoice:: analysis_1
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
    :correct: b
    :feedback_a: In an example like this you want to count the nested loops. especially the loops that are dependent on the same variable, in this case, n.
    :feedback_b: A singly nested loop like this is O(n^2)
    :feedback_c: log n typically is indicated when the problem is iteratvely made smaller
    :feedback_d: In an example like this you want to count the nested loops. especially the loops that are dependent on the same variable, in this case, n.
    :pct_on_first: 0.8947368421
    :total_students_attempting: 19
    :num_students_correct: 19
    :mean_clicks_to_correct: 1.1052631579

    Given the following code fragment, what is its Big-O running time?
    
    .. code-block:: python
    
      test = 0
      for i in range(n):
         for j in range(n):
            test = test + i * j