.. mchoice:: 2012GreyScale_alg2_ans
 :author: bmiller
 :difficulty: 3.0
 :basecourse: csawesome
 :chapter: Unit8-2DArray
 :subchapter: grayImageA
 :topics: Unit8-2DArray/grayImageA
 :from_source: T
 :answer_a: (int row = 0; row < pixelValues.length - 1; row++)
 :answer_b: (int row = 0; row < pixelValues.length; row++)
 :answer_c: (int row = 0; row < pixelValues.height; row++)
 :answer_d: (int row = 0; row < pixelValues.height - 1; row++)
 :correct: b
 :feedback_a: This does not iterate through all the rows of the array
 :feedback_b: Correct
 :feedback_c: The .height method does not exist
 :feedback_d: The .height method does not exist
 :pct_on_first: 0.6666666667
 :total_students_attempting: 3
 :num_students_correct: 3.0
 :mean_clicks_to_correct: 1.6666666667

 What could you write for the outer for loop so that it iterates through the rows of the array?