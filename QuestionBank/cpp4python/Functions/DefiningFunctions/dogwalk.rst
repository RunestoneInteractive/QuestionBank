.. activecode:: dogwalk
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Functions
    :subchapter: DefiningFunctions
    :topics: Functions/DefiningFunctions
    :from_source: T
    :language: cpp

    // function that retuns outputs number of steps wallked
    #include <iostream>
    using namespace std;

    void dogWalk(int steps){
        for (int step = 0; step < steps; step++){
            cout << "dog walked "<< step << " steps!"<< endl;
        }
    }

    int main() {
        dogWalk(11);

        return 0;
    }