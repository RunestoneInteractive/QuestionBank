.. parsonsprob:: tip1
   :author: Craig Miller
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Order the code so that it prompts the user for the amount of
   a check at a restaurant.  It should then print out the total 
   with a 20% tip added.
   -----
   amount = eval(input('What is the amount of the check in dollars? ')
   =====
   tip = amount * 0.2
   =====
   total = amount + tip
   =====
   print("The total with 20% tip is " + str(total) + ".")