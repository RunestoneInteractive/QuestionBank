.. activecode:: ec2cpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: AlgorithmAnalysis
   :subchapter: WhatIsAlgorithmAnalysis
   :topics: AlgorithmAnalysis/WhatIsAlgorithmAnalysis
   :from_source: T
   :caption: C++
   :language: cpp

    #include <iostream>
    #include <ctime>
    using namespace std;

    //Performs same function as listing one, and also list the time it takes to perform
    //the function

    int sumofN2(int n) {
        clock_t begin = clock();
        int theSum = 0;
        for(int i = 0; i < n+1; i++){
            theSum = theSum + i;
        }
        clock_t end = clock();
        double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "Sum is " << theSum << " required "<<elapsed_secs << " seconds" << endl;
        return theSum;
   }

   int main(){
       for (int i = 0; i < 6; i++){
            sumofN2(10000);
       }
       return 0;
   }