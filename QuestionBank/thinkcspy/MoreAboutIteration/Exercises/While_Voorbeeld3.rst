.. activecode:: While_Voorbeeld3
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python

    Voorbeeld 3
    ~~~~
    getal=int(input("Geef een positief getal"))
    while(getal<0):
        getal=int(input(str(getal) + " is geen positief getal! Probeer opnieuw"))
    print("Jouw positief getal was: ",getal)