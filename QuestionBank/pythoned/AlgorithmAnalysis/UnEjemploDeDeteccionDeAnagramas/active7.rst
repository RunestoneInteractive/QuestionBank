.. activecode:: active7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: AlgorithmAnalysis
    :subchapter: UnEjemploDeDeteccionDeAnagramas
    :topics: AlgorithmAnalysis/UnEjemploDeDeteccionDeAnagramas
    :from_source: None
    :caption: Contar y comparar

    def anagramaSolucion4(cadena1,cadena2):
        c1 = [0]*26
        c2 = [0]*26

        for i in range(len(cadena1)):
            pos = ord(cadena1[i])-ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(cadena2)):
            pos = ord(cadena2[i])-ord('a')
            c2[pos] = c2[pos] + 1

        j = 0
        aunOK = True
        while j<26 and aunOK:
            if c1[j]==c2[j]:
                j = j + 1
            else:
                aunOK = False

        return aunOK

    print(anagramaSolucion4('cero','ocre'))