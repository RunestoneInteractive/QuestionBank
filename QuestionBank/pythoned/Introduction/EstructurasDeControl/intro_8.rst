.. activecode:: intro_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Introduction
    :subchapter: EstructurasDeControl
    :topics: Introduction/EstructurasDeControl
    :from_source: None
    :caption: Procesamiento de cada carácter en una lista de cadenas

    listaPalabras = ['gato','perro','conejo']
    listaLetras = [ ]
    for unaPalabra in listaPalabras:
        for unaLetra in unaPalabra:
            listaLetras.append(unaLetra)
    print(listaLetras)