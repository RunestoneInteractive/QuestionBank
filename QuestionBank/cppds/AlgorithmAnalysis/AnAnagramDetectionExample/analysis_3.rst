.. mchoice:: analysis_3
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
    :correct: c
    :feedback_a: No. Look carefully at the loop variable i.  Notice that the value of i is cut in half each time through the loop.  This is a big hint that the performance is better than O(n)
    :feedback_b: No. Check again, is this a nested loop?
    :feedback_c: Right! The value of i is cut in half each time through the loop so it will only take log n iterations.
    :feedback_d: No. Check again, is this a nested loop?
    :pct_on_first: 0.5
    :total_students_attempting: 94
    :num_students_correct: 94
    :mean_clicks_to_correct: 1.6276595745

    Given the following code fragment what is its Big-O running time?
    
    .. code-block:: cpp
    
      int main(){
          int i = n;
          int count = 0;
          while (i > 0){
              count = count + 1;
              i = i // 2;
          }
          return 0;
      }