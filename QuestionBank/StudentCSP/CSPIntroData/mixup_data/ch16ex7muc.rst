.. parsonsprob:: ch16ex7muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: mixup_data
   :topics: CSPIntroData/mixup_data
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.0552763819
   :total_students_attempting: 199
   :num_students_correct: 133.0
   :mean_clicks_to_correct: 6.8120300752

   The following program segment should first print out the program's instructions. Next it should continuously ask the user if it wants to add a word to a list <i>vocabulary</i> and then append it to the end the list IF the word is not already in the list. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   print("Enter a word to add it to the vocabulary list or type in 'quit' to end the program.")
   response = 0
   vocabulary = []
   =====
   while response != "quit":
   =====
   while response == "quit": #distractor
   =====
       response = input("Enter a vocabulary word:")
   =====
       if response not in vocabulary:
   =====
           vocabulary.append(response)