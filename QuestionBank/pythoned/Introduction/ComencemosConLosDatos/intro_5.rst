.. activecode:: intro_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Introduction
    :subchapter: ComencemosConLosDatos
    :topics: Introduction/ComencemosConLosDatos
    :from_source: None
    :caption: Ejemplos de métodos de las listas

    miLista = [1024, 3, True, 6.5]
    miLista.append(False)
    print(miLista)
    miLista.insert(2,4.5)
    print(miLista)
    print(miLista.pop())
    print(miLista)
    print(miLista.pop(1))
    print(miLista)
    miLista.pop(2)
    print(miLista)
    miLista.sort()
    print(miLista)
    miLista.reverse()
    print(miLista)
    print(miLista.count(6.5))
    print(miLista.index(4.5))
    miLista.remove(6.5)
    print(miLista)
    del miLista[0]
    print(miLista)