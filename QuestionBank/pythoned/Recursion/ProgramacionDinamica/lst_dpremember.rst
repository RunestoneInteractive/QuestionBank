.. activecode:: lst_dpremember
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythoned
    :chapter: Recursion
    :subchapter: ProgramacionDinamica
    :topics: Recursion/ProgramacionDinamica
    :from_source: None
    :caption: Solución completa al problema de dar las vueltas
    :nocodelens:

    def vueltasProgDin(listaValoresMonedas,vueltas,minMonedas,monedasUsadas):
       for centavos in range(vueltas+1):
          conteoMonedas = centavos
          nuevaMoneda = 1
          for j in [m for m in listaValoresMonedas if m <= centavos]:
                if minMonedas[centavos-j] + 1 < conteoMonedas:
                   conteoMonedas = minMonedas[centavos-j]+1
                   nuevaMoneda = j
          minMonedas[centavos] = conteoMonedas
          monedasUsadas[centavos] = nuevaMoneda
       return minMonedas[vueltas]

    def imprimirMonedas(monedasUsadas,vueltas):
       moneda = vueltas
       while moneda > 0:
          estaMoneda = monedasUsadas[moneda]
          print(estaMoneda)
          moneda = moneda - estaMoneda

    def main():
        cantidad = 63
        listaM = [1,5,10,21,25]
        monedasUsadas = [0]*(cantidad+1)
        conteoMonedas = [0]*(cantidad+1)

        print("Dar unas vueltas de",cantidad,"centavos requiere")
        print(vueltasProgDin(listaM,cantidad,conteoMonedas,monedasUsadas),"monedas")
        print("Tales monedas son:")
        imprimirMonedas(monedasUsadas,cantidad)
        print("La lista usada es la siguiente:")
        print(monedasUsadas)

    main()