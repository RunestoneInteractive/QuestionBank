.. activecode:: hanoi
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Recursion
    :subchapter: LasTorresDeHanoi
    :topics: Recursion/LasTorresDeHanoi
    :from_source: None
    :caption: Solución recursiva del problema de las torres de Hanoi

    def moverTorre(altura,origen, destino, intermedio):
        if altura >= 1:
            moverTorre(altura-1,origen,intermedio,destino)
            moverDisco(origen,destino)
            moverTorre(altura-1,intermedio,destino,origen)

    def moverDisco(desde,hacia):
        print("mover disco de",desde,"a",hacia)

    moverTorre(3,"A","B","C")