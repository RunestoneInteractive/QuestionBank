.. activecode:: Functies_Voorbeeld7
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python

    Voorbeeld 7
    ~~~~
    def discriminant(a,b,c):
        return(b**2-4*a*c)

    a=int(input("Geef a"))
    b=int(input("Geef b"))
    c=int(input("Geef c"))
    D=discriminant(a,b,c)
    print("De discriminant is",D)