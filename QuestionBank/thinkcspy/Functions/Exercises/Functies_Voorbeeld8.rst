.. activecode:: Functies_Voorbeeld8
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python

    Voorbeeld 8
    ~~~~
    import math
    def discriminant(a,b,c):
        return(b**2-4*a*c)

    a=int(input("Geef a"))
    b=int(input("Geef b"))
    c=int(input("Geef c"))
    D=discriminant(a,b,c)
    if(D>0):
        print("De eerste oplossing is",(-b+math.sqrt(D))/(2*a)," en de tweede oplossing is",(-b-math.sqrt(D))/(2*a))
    elif(D==0):
        print("De oplossing is",-b/(2*a))
    else:
        print("Er is geen oplossing")