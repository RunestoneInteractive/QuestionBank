.. activecode:: hw13bDE
    :author: Damon Ellingston
    :difficulty: 4.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F

    **Homework 13 b  - -  doubling time**

    "Doubling time" is the time it takes for an investment to double in value. Write a program that calculates the doubling time in years for an initial investment P_o at an annual interest rate of R percent. Recall the compound interest formula::


     P(t)=P_o(1 +R/100)^t


    where R is entered as a percent by the user, for example 5%. A couple of suggestions: Set P_o to $100 for simplicity, it doesn't affect the doubling time. Ask the user for a straight percent R. Use a ``while`` loop similar to the one we programmed on Wednesday, I've inserted it for you but you're free to write your own. Your program should ask for an interest rate and should return the doubling time in years. Be sure to check your results against some realistic values.


    ~~~~

    while P<200: