.. activecode:: palchecker
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: BasicDS
   :subchapter: VerificadorDePalindromos
   :topics: BasicDS/VerificadorDePalindromos
   :from_source: None
   :caption: Un verificador de palíndromos usando una cola doble
   :nocodelens:

   from pythoned.basicas.coladoble import ColaDoble

   def verificarPalindromo(cadena):

       colaDobleCaracteres = ColaDoble()
       for  caracter in cadena:
           colaDobleCaracteres.agregarFinal(caracter)

       aunIguales = True

       while colaDobleCaracteres.tamano() > 1 and aunIguales:
           primero = colaDobleCaracteres.removerFrente()
           ultimo = colaDobleCaracteres.removerFinal()
           if primero != ultimo:
               aunIguales = False

       return aunIguales

   print(verificarPalindromo("lsdkjfskf"))
   print(verificarPalindromo("radar"))