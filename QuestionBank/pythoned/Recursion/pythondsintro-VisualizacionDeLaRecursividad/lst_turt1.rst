.. activecode:: lst_turt1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Recursion
    :subchapter: pythondsintro-VisualizacionDeLaRecursividad
    :topics: Recursion/pythondsintro-VisualizacionDeLaRecursividad
    :from_source: None
    :caption: Dibujar una espiral recursiva usando el módulo turtle
    :nocodelens:


    import turtle

    miTortuga = turtle.Turtle()
    miVentana = turtle.Screen()

    def dibujarEspiral(miTortuga, longitudLinea):
        if longitudLinea > 0:
            miTortuga.forward(longitudLinea)
            miTortuga.right(90)
            dibujarEspiral(miTortuga,longitudLinea-5)

    dibujarEspiral(miTortuga,100)
    miVentana.exitonclick()