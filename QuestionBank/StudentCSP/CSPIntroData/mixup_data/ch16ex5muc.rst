.. parsonsprob:: ch16ex5muc
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
   :pct_on_first: 0.1203703704
   :total_students_attempting: 216
   :num_students_correct: 152.0
   :mean_clicks_to_correct: 6.5723684211

   The following program segment should iterate through the list <i>terms</i> and then add each item to the list <i>vocab</i> if it is not already in the list. If the word is already in <i>vocab</i>, then the program should add 1 to the variable "counter". But the blocks have been mixed up and include extra blocks that aren't needed in the solution. Drag the needed blocks from the left and put them in the correct order on the right. Click the <i>Check Me</i> button to check your solution.</p>
   -----
   terms = ["accent", "vertigo", "libra", "illusion"]
   vocab = ["hereditary", "illusion", "vertigo", "velocity", "fallacy"]
   counter = 0
   =====
   for word in terms:
   =====
       if word NOT in vocab:
   =====
           vocab.append(word)
   =====
           word.append(vocab) #distractor
   =====
       elif word in vocab:
   =====
           counter += 1
   =====
           counter + 1 #distractor