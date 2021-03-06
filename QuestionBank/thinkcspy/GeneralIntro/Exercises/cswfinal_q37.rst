.. mchoice:: cswfinal_q37
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F
   :answer_a: O(N**2)
   :answer_b: O(N)
   :answer_c: O(logN)
   :answer_d: O(1)
   :correct: a
   :random: 
   :pct_on_first: 0.7435897436
   :total_students_attempting: 39
   :num_students_correct: 39.0
   :mean_clicks_to_correct: 1.3846153846

   37. What is the computational complexity of the greenscreen algorithm? Hint: Remember that the program has to look at every pixel in the image. Consider, too, how many pixels are in a 10 x 10 image, a 20 x 20 image, a 30 x 30 image, and so forth. There are two images (foreground and background) so the number of operations is doubled - but we ignore the constant multiplier when calculating computational complexity. For example, if an algorithm is O(4N**N) we drop the 4 and just say it's O(N**N).