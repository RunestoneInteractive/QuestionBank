.. activecode:: heap1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Trees
    :subchapter: OperacionesDeMonticulosBinarios
    :topics: Trees/OperacionesDeMonticulosBinarios
    :from_source: None
    :caption: Uso de un montículo binario
    :nocodelens:

    from pythoned.arboles.monticuloBinario import MonticuloBinario

    miMonticulo = MonticuloBinario()
    miMonticulo.insertar(5)
    miMonticulo.insertar(7)
    miMonticulo.insertar(3)
    miMonticulo.insertar(11)

    print(miMonticulo.eliminarMin())

    print(miMonticulo.eliminarMin())

    print(miMonticulo.eliminarMin())

    print(miMonticulo.eliminarMin())