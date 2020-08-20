.. parsonsprob:: m2-guess-word-length
   :author: Kathryn Cunningham
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :numbered: left
   :noindent:

   Solve my really cool parsons problem...if you can.
   -----
   def play(self):
   =====
	while self.guess != self.word:
   =====
    	    input_word = input("Guess a word from the list of words: ")
    =====
	    self.guess = input_word
    =====
    	  if len(self.guess) < len(self.word):
            print("The guessed word is shorter.")
    =====
    	  elif len(self.guess) > len(self.word):
            print("The guessed word is longer.")
    =====
    	  else:
            print("You won!")