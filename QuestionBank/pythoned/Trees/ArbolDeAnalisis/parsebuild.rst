.. activecode::  parsebuild
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Trees
    :subchapter: ArbolDeAnalisis
    :topics: Trees/ArbolDeAnalisis
    :from_source: None
    :caption: Contrucción de un árbol de análisis
    :nocodelens:

    from pythoned.basicas.pila import Pila
    from pythoned.arboles.arbolBinario import ArbolBinario

    def construirArbolAnalisis(expresionAgrupada):
        listaSimbolos = expresionAgrupada.split()
        pilaPadres = Pila()
        arbolExpresion = ArbolBinario('')
        pilaPadres.incluir(arbolExpresion)
        arbolActual = arbolExpresion
        for i in listaSimbolos:
            if i == '(':
                arbolActual.insertarIzquierdo('')
                pilaPadres.incluir(arbolActual)
                arbolActual = arbolActual.obtenerHijoIzquierdo()
            elif i not in ['+', '-', '*', '/', ')']:
                arbolActual.asignarValorRaiz(int(i))
                padre = pilaPadres.extraer()
                arbolActual = padre
            elif i in ['+', '-', '*', '/']:
                arbolActual.asignarValorRaiz(i)
                arbolActual.insertarDerecho('')
                pilaPadres.incluir(arbolActual)
                arbolActual = arbolActual.obtenerHijoDerecho()
            elif i == ')':
                arbolActual = pilaPadres.extraer()
            else:
                raise ValueError
        return arbolExpresion

    miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * 3 )")
    print(miArbolAnalisis) # Imprimir el objeto árbol pero no muestra los valores en los nodos
    #miArbolAnalisis.postorden()  #definida y explicada en la próxima sección