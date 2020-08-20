.. codelens:: search2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: SortSearch
    :subchapter: LaBusquedaSecuencial
    :topics: SortSearch/LaBusquedaSecuencial
    :from_source: None
    :caption: Búsqueda secuencial en una lista ordenada

    def busquedaSecuencialOrdenada(unaLista, item):
        pos = 0
        encontrado = False
        parar = False
        while pos < len(unaLista) and not encontrado and not parar:
            if unaLista[pos] == item:
                encontrado = True
            else:
                if unaLista[pos] > item:
                    parar = True
                else:
                    pos = pos+1

        return encontrado

    listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(busquedaSecuencialOrdenada(listaPrueba, 3))
    print(busquedaSecuencialOrdenada(listaPrueba, 13))