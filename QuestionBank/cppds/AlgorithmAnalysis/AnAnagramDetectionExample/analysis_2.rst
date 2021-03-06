.. mchoice:: analysis_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: AnAnagramDetectionExample
    :topics: AlgorithmAnalysis/AnAnagramDetectionExample
    :from_source: T
    :answer_a: O(n)
    :answer_b: O(n<sup>2</sup>)
    :answer_c: O(log n)
    :answer_d: O(n<sup>3</sup>)
    :correct: a
    :feedback_a: Right! Even though there are two loops they are not nested.  You might think of this as O(2n) but we can ignore the constant 2.
    :feedback_b: No. Be careful, in counting loops you want to look carefully at whether or not the loops are nested.
    :feedback_c: No. log n typically is indicated when the problem is iteratively made smaller.
    :feedback_d: No. Be careful, in counting loops you want to look carefully at whether or not the loops are nested.
    :pct_on_first: 0.752688172
    :total_students_attempting: 93
    :num_students_correct: 93
    :mean_clicks_to_correct: 1.3978494624

    Given the following code fragment what is its Big-O running time?
    
    .. code-block:: cpp
    
      int main(){
          int test = 0;
          for (int i = 0; i < n; i++){
              test = test + 1;
          }
          for (int j = 0; j < n; j++){
              test = test - 1;
          }
          return 0;
      }