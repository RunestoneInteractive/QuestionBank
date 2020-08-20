.. activecode:: lst_itsum
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Recursion
    :subchapter: pythondsCalculoDeLaSumaDeUnaListaDeNumeros
    :topics: Recursion/pythondsCalculoDeLaSumaDeUnaListaDeNumeros
    :from_source: None
    :caption: Sumatoria iterativa

    def sumalista(listaNumeros):
        laSuma = 0
        for i in listaNumeros:
            laSuma = laSuma + i
        return laSuma

    print(sumalista([1,3,5,7,9]))