.. activecode:: vectcpp3
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

    //Tests the time of the vector push_back() operation "reserved" versus "unreserved"

    void test1(int num){
        vector<int> vect;
        // no reserve set
        for (int i = 0; i < num; i++){
            vect.push_back(i);
        }
    }

    void test2(int num){
        vector<int> vect2;
        vect2.reserve(num);
        for (int i = 0; i < num; i++){
            vect2.push_back(i);
        }
    }

    int main(){
        int numruns = 10000;
        clock_t begin_t1 = clock();
        for (int i = 0; i < numruns; i++){
            test1(numruns);
        }
        clock_t end_t1 = clock();
        double elapsed_secs1 = double(end_t1 - begin_t1) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "unreserved push_back " << elapsed_secs1 << " milliseconds" << endl;

        clock_t begin_t2 = clock();
        for (int i = 0; i < numruns; i++){
            test2(numruns);
        }
        clock_t end_t2 = clock();
        double elapsed_secs2 = double(end_t2 - begin_t2) /CLOCKS_PER_SEC;
        cout << fixed << endl;
        cout << "reserved push_back " << elapsed_secs2 << " milliseconds" << endl;


        return 0;
    }