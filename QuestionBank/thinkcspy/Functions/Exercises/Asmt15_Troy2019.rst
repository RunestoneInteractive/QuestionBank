.. activecode:: Asmt15_Troy2019
    :author: Shawn Haarer
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
   
    You have been given two functions

    findAvg ( )  will find the average of 3 quiz scores

    findMax( ) will find the maximum of 3 quiz scores 

    Write a main program that will input 3 of your quiz scores

    Then find the average

    Then find the maxiumum

    Then print the results


    After this works, add code that will do the same for a friend.  


    BONUS:  Write a function that will find the minimum or lowest quiz score.  
    Use that function to print your lowest quiz score and your friends.  
    ~~~~
    # ASMT 15  QUIZ SCORES   BY    ** YOUR NAME **  

    # --- MODULES --------------------------------------------

    # --- FUNCTIONS -------------------------------------------

    def findAvg(n1, n2, n3):

	""" Find the average of three numbers, parameters n1, n2, n3"""
		
	total = n1 + n2 + n3
	av = total / 3.0
	return av         # Return the answer (the average) to the main program


    def findMax(n1, n2, n3):

	""" Find the maximum of three numbers, parameters n1, n2, n3"""
		
	mx = n1
		
	if (n2 > mx):
		mx = n2
	if (n3 > mx): 
		mx = n3
			
	return mx        # Return the answer (the max) to the main program 
		


    #--- MAIN PROGRAM ------------------------------------------------

    print ("This program by, YOUR NAME, will compare my 3 quiz scores with my frenemy's scores") 
    print()

    q1 = float (input ("Enter a quiz score: "))










    print ("My highest quiz score was ")



    print()
    print("What about my friend's scores?")









    print()
    print("Well done.  Keep up those high scores.")