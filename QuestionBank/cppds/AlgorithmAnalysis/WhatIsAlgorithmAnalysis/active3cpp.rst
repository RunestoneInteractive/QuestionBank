.. activecode:: active3cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Summation Without Iteration C++
    :language: cpp

    //Performs same function as listing one, and also list the time it takes to perfrom
    //the function, and it performs better with larger inputs or (n)

    #include <iostream>
    using namespace std;
    #include <ctime>

    int sumOfN3(int n){
        int sum_n = (n*(n+1))/2;
        return sum_n;
    }

    int main(){
        cout << sumOfN3(10);
        return 0;
    }