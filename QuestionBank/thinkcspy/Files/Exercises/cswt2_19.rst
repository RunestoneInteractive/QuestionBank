.. mchoice:: cswt2_19
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :answer_a: All the text of the file in one string
   :answer_b: Only the 'r' characters from the file
   :answer_c: None
   :answer_d: All characters from the file except the 'r' characters
   :correct: a
   :random: 
   :pct_on_first: 0.6802325581
   :total_students_attempting: 172
   :num_students_correct: 171.0
   :mean_clicks_to_correct: 1.6315789474

   19. Assume that "pease.txt" is the name of a text file holding the text to the poem "Pease Porridge Hot." What is the content of the variable t after executing the following code segment?::
   
      f = open("pease.txt", "r")
      t = f.read()