.. activecode:: ec2_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: WhatIsAlgorithmAnalysis
    :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
    :from_source: T
    :caption: Another Summation of the First n Integers in C++
    :language: cpp

    #include <iostream>
    using namespace std;

    //Performs same function as listing 1, but is less descriptive
    //This is not good practice

    int foo(int tom){
        int fred = 0;
        for (int bill = 0; bill < tom+1; bill++){
            int barney = bill;
            fred = fred + barney;
        }
        return fred;
    }

    int main(){
        cout << foo(10);
        return 0;
    }