.. activecode:: lst_itsumcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: pythondsCalculatingtheSumofaListofNumbers
    :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
    :from_source: T
    :caption: Iterative Summation C++
    :language: cpp

    //Example of summing up a vector without using recursion.

    #include <iostream>
    using namespace std;

    int vectsum(int numVect[]){
        int theSum = 0;
        for (int i = 0; i < 5; i++){
            theSum += numVect[i];
        }
        return theSum;
    }

    int main() {
        int numVect[5] = {1, 3, 5, 7, 9};
        cout << vectsum(numVect) << endl;

        return 0;
    }