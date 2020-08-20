.. activecode:: lst_dprememberpy
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: DynamicProgramming
    :topics: Recursion/DynamicProgramming
    :from_source: T
    :caption: Complete Solution to the Change Problem Python
    :nocodelens:
    :optional:

    #Addition to the precious program that finds the types of coins used and the process of doing it.

    def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
        for cents in range(change+1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j] + 1 #assigns the amount of coins used.
                    newCoin = j #assigns the type of coin used.
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
        return minCoins[change]

    def printCoins(coinsUsed,change):
        coin = change
        while coin > 0:
            thisCoin = coinsUsed[coin]
            print(thisCoin)
            coin = coin - thisCoin

    def main():
        amnt = 63
        clist = [1, 5, 10, 21, 25]
        coinsUsed = [0]*(amnt+1)
        coinCount = [0]*(amnt+1)

        print("Making change for",amnt,"requires")
        print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
        print("They are:")
        printCoins(coinsUsed,amnt)
        print("The used list is as follows:")
        print(coinsUsed)

    main()