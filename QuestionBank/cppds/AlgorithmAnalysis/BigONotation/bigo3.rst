.. mchoice:: bigo3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: BigONotation
    :topics: AlgorithmAnalysis/BigONotation
    :from_source: T
    :answer_a: O(2n)
    :answer_b: O(n)
    :answer_c: O(3n<sup>2</sup>)
    :answer_d: O(n<sup>2</sup>)
    :answer_e: More than one of the above
    :correct: d
    :feedback_a: No, 3n<sup>2</sup> dominates 2n. Try again.
    :feedback_b: No, n<sup>2</sup> dominates n. Try again.
    :feedback_c: No, the 3 should be omitted because n<sup>2</sup> dominates.
    :feedback_d: Right!
    :feedback_e: No, only one of them is correct. Try again.
    :pct_on_first: 0.7572815534
    :total_students_attempting: 103
    :num_students_correct: 103
    :mean_clicks_to_correct: 1.2621359223

    
    If the exact number of steps is :math:`T(n)=2n+3n^{2}-1` what is the Big O?