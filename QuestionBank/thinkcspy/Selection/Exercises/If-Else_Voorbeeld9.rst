.. activecode:: If-Else_Voorbeeld9
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :language: python

    Voorbeeld 9
    ~~~~
    getal=int(input("Geef een getal in"))
    if getal>0:
        print("Je hebt een positief getal ingegeven")
    elif getal<0:
       print("Je hebt een negatief getal ingegeven")
    else:
       print("Je getal is 0")