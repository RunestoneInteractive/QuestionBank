.. activecode:: completeheap
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythoned
   :chapter: Trees
   :subchapter: ImplementacionDeUnMonticuloBinario
   :topics: Trees/ImplementacionDeUnMonticuloBinario
   :from_source: None
   :caption: El ejemplo completo de un montículo binario
   :hidecode:

   class MonticuloBinario:
       def __init__(self):
           self.listaMonticulo = [0]
           self.tamanoActual = 0


       def infiltArriba(self,i):
           while i // 2 > 0:
             if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
             i = i // 2

       def insertar(self,k):
         self.listaMonticulo.append(k)
         self.tamanoActual = self.tamanoActual + 1
         self.infiltArriba(self.tamanoActual)

       def infiltAbajo(self,i):
         while (i * 2) <= self.tamanoActual:
             hm = self.hijoMin(i)
             if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                 tmp = self.listaMonticulo[i]
                 self.listaMonticulo[i] = self.listaMonticulo[hm]
                 self.listaMonticulo[hm] = tmp
             i = hm

       def hijoMin(self,i):
         if i * 2 + 1 > self.tamanoActual:
             return i * 2
         else:
             if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                 return i * 2
             else:
                 return i * 2 + 1

       def eliminarMin(self):
         valorSacado = self.listaMonticulo[1]
         self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
         self.tamanoActual = self.tamanoActual - 1
         self.listaMonticulo.pop()
         self.infiltAbajo(1)
         return valorSacado

       def construirMonticulo(self,unaLista):
         i = len(unaLista) // 2
         self.tamanoActual = len(unaLista)
         self.listaMonticulo = [0] + unaLista[:]
         while (i > 0):
             self.infiltAbajo(i)
             i = i - 1

   miMonticulo = MonticuloBinario()
   miMonticulo.construirMonticulo([9,5,6,2,3])

   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())