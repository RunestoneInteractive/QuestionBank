.. activecode:: lst_rectostr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Recursion
    :subchapter: pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
    :topics: Recursion/pythondsConversionDeUnEnteroAUnaCadenaEnCualquierBase
    :from_source: None
    :caption: Conversión recursiva de un entero a una cadena

    def aCadena(n,base):
       cadenaConversion = "0123456789ABCDEF"
       if n < base:
          return cadenaConversion[n]
       else:
          return aCadena(n//base,base) + cadenaConversion[n%base]

    print(aCadena(1453,16))