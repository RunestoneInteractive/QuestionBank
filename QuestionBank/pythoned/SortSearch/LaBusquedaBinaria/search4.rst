.. codelens:: search4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: SortSearch
    :subchapter: LaBusquedaBinaria
    :topics: SortSearch/LaBusquedaBinaria
    :from_source: None
    :caption: Una búsqueda binaria--Versión recursiva

    def busquedaBinaria(unaLista, item):
        if len(unaLista) == 0:
            return False
        else:
            puntoMedio = len(unaLista)//2
            if unaLista[puntoMedio]==item:
              return True
            else:
              if item<unaLista[puntoMedio]:
                return busquedaBinaria(unaLista[:puntoMedio],item)
              else:
                return busquedaBinaria(unaLista[puntoMedio+1:],item)

    listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(busquedaBinaria(listaPrueba, 3))
    print(busquedaBinaria(listaPrueba, 13))