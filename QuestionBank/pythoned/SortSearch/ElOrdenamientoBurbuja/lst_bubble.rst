.. activecode:: lst_bubble
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: SortSearch
    :subchapter: ElOrdenamientoBurbuja
    :topics: SortSearch/ElOrdenamientoBurbuja
    :from_source: None
    :caption: El ordenamiento burbuja

    def ordenamientoBurbuja(unaLista):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp

    unaLista = [54,26,93,17,77,31,44,55,20]
    ordenamientoBurbuja(unaLista)
    print(unaLista)