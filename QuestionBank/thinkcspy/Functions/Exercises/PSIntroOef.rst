.. activecode:: PSIntroOef
    :author: Gilles Fiers
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python

    Bekijk onderstaande code. Wat doet dit programma ? Vul de ontbrekende gedeelten aan. 
    ~~~~
    import math
    def discriminant(a,b,c):
        return(b**2-4*a*c)

    a=int(input("Geef a"))
    b=int(input("Geef b"))
    c=int(input("Geef c"))
    D=discriminant(a,b,c)
    if(...):
        print("De eerste oplossing is",(-b+math.sqrt(D))/(2*a)," en de tweede oplossing is",(-b-math.sqrt(D))/(2*a))
    elif(D==0):
        print("De oplossing is",...)
    else:
        print("...")