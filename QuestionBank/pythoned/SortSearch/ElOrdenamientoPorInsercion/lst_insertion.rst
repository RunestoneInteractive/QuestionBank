.. activecode:: lst_insertion
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: SortSearch
    :subchapter: ElOrdenamientoPorInsercion
    :topics: SortSearch/ElOrdenamientoPorInsercion
    :from_source: None
    :caption: Ordenamiento por inserción

    def ordenamientoPorInsercion(unaLista):
       for indice in range(1,len(unaLista)):

         valorActual = unaLista[indice]
         posicion = indice

         while posicion>0 and unaLista[posicion-1]>valorActual:
             unaLista[posicion]=unaLista[posicion-1]
             posicion = posicion-1

         unaLista[posicion]=valorActual

    unaLista = [54,26,93,17,77,31,44,55,20]
    ordenamientoPorInsercion(unaLista)
    print(unaLista)