.. activecode:: baseconvert
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: BasicDS
    :subchapter: ConversionDeNumerosDecimalesANumerosBinarios
    :topics: BasicDS/ConversionDeNumerosDecimalesANumerosBinarios
    :from_source: None
    :caption: Conversión de decimal a cualquier base
    :nocodelens:

    from pythoned.basicas.pila import Pila

    def convertirBase(numeroDecimal,base):
        digitos = "0123456789ABCDEF"

        pilaResiduo = Pila()

        while numeroDecimal > 0:
            residuo = numeroDecimal % base
            pilaResiduo.incluir(residuo)
            numeroDecimal = numeroDecimal // base

        nuevaCadena = ""
        while not pilaResiduo.estaVacia():
            nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]

        return nuevaCadena

    print(convertirBase(25,2))
    print(convertirBase(25,16))