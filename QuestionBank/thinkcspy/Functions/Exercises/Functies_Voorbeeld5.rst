.. activecode:: Functies_Voorbeeld5
    :author: Jan Persan
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python

    Voorbeeld 5
    ~~~~
    def rechthoek(lengte, breedte):
        alex=turtle.Turtle()
        alex.fd(lengte)
        alex.right(90)
        alex.fd(breedte)
        alex.right(90)
        alex.fd(lengte)
        alex.right(90)
        alex.fd(breedte)
        alex.right(90)

    import turtle
    rechthoek(100,50)