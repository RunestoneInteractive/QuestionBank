.. activecode:: lst_dpremembercpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: DynamicProgramming
    :topics: Recursion/DynamicProgramming
    :from_source: T
    :caption: Complete Solution to the Change Problem C++
    :language: cpp

    //Addition to the precious program that finds the types of coins used and the process of doing it.

    #include <iostream>
    #include <vector>
    using namespace std;

    int dpMakeChange(vector<int> coinValueList, int change, vector<int> minCoins,   vector<int> coinsUsed){
        //This function keeps track of the number of coins needed to create the change.
        for (int cents = 0 ; cents < change+1; cents++){
            int coinCount = cents;
            int newCoin = 1;

            for (int j : coinValueList){ //loop finds solution for all sets of change from 0 to int change.
                if (j <= cents){
                    if (minCoins[cents-j] + 1 < coinCount){
                        coinCount = minCoins[cents-j] + 1; //assigns the number of coins used to make the sum.
                        newCoin = j; //assigns the type of coins that is used to find the sum.
                    }
                }
            }

            minCoins[cents] = coinCount;
            coinsUsed[cents] = newCoin;
        }

        return minCoins[change];
    }

    vector<int> dpMakeChange2(vector<int> coinValueList, int change, vector<int>   minCoins, vector<int> coinsUsed){
        //This function keeps track of the exact coins used to make the change.
        for (int cents = 0; cents < change + 1; cents++){
            int coinCount = cents;
            int newCoin = 1;

            for (int j : coinValueList){
                if (j <= cents){
                    if (minCoins[cents-j] + 1 < coinCount){
                        coinCount = minCoins[cents-j] + 1; //assigns the number of coins that have been used to make the sum.
                        newCoin = j; //assigns the current type of coin that will be used to make the sum.
                    }
                }
            }

            minCoins[cents] = coinCount;
            coinsUsed[cents] = newCoin;
        }
        return coinsUsed;
    }

    void printCoins(vector<int> coinsUsed, int change){
        int coin = change;

        while (coin > 0){
            int thisCoin = coinsUsed[coin];
            cout << thisCoin << endl;
            coin = coin - thisCoin;
        }
    }

    int main(){
        vector<int> clist = {1, 5, 10, 21, 25};
        int amnt = 63;
        vector<int> minCoins(amnt + 1, 0);
        vector<int> coinsUsed(amnt + 1, 0);
        vector<int> coinCount(amnt + 1, 0);

        cout << "Making change for " << amnt << " requires" << endl;
        cout << dpMakeChange(clist, amnt, minCoins, coinsUsed)<< " coins" << endl;
        cout << "They are: " << endl;
        printCoins(dpMakeChange2(clist, amnt, minCoins, coinsUsed), amnt);
        cout << "The used list is as follows: " << endl;
        vector<int> coinsUsed2 = dpMakeChange2(clist, amnt, minCoins, coinsUsed);
        cout << "[";

        for (unsigned int i = 0; i<coinsUsed2.size(); i++){
            cout << coinsUsed2[i] << ", ";
        }

        cout << "]" << endl;
        return 0;
    }