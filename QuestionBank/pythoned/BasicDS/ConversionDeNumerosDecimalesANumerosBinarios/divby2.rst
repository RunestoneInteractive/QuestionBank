.. activecode:: divby2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: ConversionDeNumerosDecimalesANumerosBinarios
   :topics: BasicDS/ConversionDeNumerosDecimalesANumerosBinarios
   :from_source: None
   :caption: Conversión de decimal a binario
   :nocodelens:

   from pythoned.basicas.pila import Pila

   def dividirPor2(numeroDecimal):
       pilaResiduo = Pila()

       while numeroDecimal > 0:
           residuo = numeroDecimal % 2
           pilaResiduo.incluir(residuo)
           numeroDecimal = numeroDecimal // 2

       cadenaBinaria = ""
       while not pilaResiduo.estaVacia():
           cadenaBinaria = cadenaBinaria + str(pilaResiduo.extraer())

       return cadenaBinaria

   print(dividirPor2(42))