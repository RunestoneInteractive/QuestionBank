.. codelens:: search1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: SortSearch
    :subchapter: LaBusquedaSecuencial
    :topics: SortSearch/LaBusquedaSecuencial
    :from_source: None
    :caption: Búsqueda secuencial en una lista no ordenada

    def busquedaSecuencial(unaLista, item):
        pos = 0
        encontrado = False

        while pos < len(unaLista) and not encontrado:
            if unaLista[pos] == item:
                encontrado = True
            else:
                pos = pos+1

        return encontrado

    listaPrueba = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(busquedaSecuencial(listaPrueba, 3))
    print(busquedaSecuencial(listaPrueba, 13))