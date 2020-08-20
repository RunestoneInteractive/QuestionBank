.. activecode:: popbackvserase
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: VectorAnalysis
    :topics: AlgorithmAnalysis/VectorAnalysis
    :from_source: T
    :language: cpp

    #include <iostream>
    #include <vector>
    using namespace std;

    //Tests the time of the vector "pop_back()" operation versus the vector "erase" operation

    int main(){
        int num = 10000;
        vector<int> vect;
        vector<int> vect2;
        vect.reserve(num);
        vect2.reserve(num);

        for (int i = 0; i < num; i++){
            vect.push_back(i);
        }

        for (int i = 0; i < num; i++){
            vect2.push_back(i);
        }

        clock_t begin = clock();
        for (int i = 0; i < num; i++){
            vect.erase(vect.begin()+0);
        }
        clock_t end = clock();
        double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "popzero = " << elapsed_secs << endl;

        clock_t begin2 = clock();
        for (int i = 0; i < num; i++){
            vect2.pop_back();
        }
        clock_t end2 = clock();
        double elapsed_secs2 = double(end2 - begin2) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "popend = " << elapsed_secs2 << endl;

        cout << "\nPopping from the end is " << elapsed_secs/elapsed_secs2 <<" times faster." << endl;

        return 0;
    }