.. activecode:: active6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: AlgorithmAnalysis
    :subchapter: UnEjemploDeDeteccionDeAnagramas
    :topics: AlgorithmAnalysis/UnEjemploDeDeteccionDeAnagramas
    :from_source: None
    :caption: Ordenar y comparar

    def anagramaSolucion2(cadena1,cadena2):
        unaLista1 = list(cadena1)
        unaLista2 = list(cadena2)

        unaLista1.sort()
        unaLista2.sort()

        pos = 0
        coincide = True

        while pos < len(cadena1) and coincide:
            if unaLista1[pos]==unaLista2[pos]:
                pos = pos + 1
            else:
                coincide = False

        return coincide

    print(anagramaSolucion2('abcde','edcba'))