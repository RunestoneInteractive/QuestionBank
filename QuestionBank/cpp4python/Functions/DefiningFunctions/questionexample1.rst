..  activecode:: questionexample1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Functions
    :subchapter: DefiningFunctions
    :topics: Functions/DefiningFunctions
    :from_source: T
    :coach:
    :language: cpp

    // demonstrates the difference between pass-by-value
    // and pass-by-reference functions.
    #include <iostream>
    using namespace std;

    void func1(int var1, int var2){
        int temp;
        temp = var1;
        var1 = var2;
        var2 = temp;
    }

    void func2(int &var1, int &var2){
        int temp;
        temp = var1;
        var1 = var2;
        var2 = temp;
    }

    int main(){
        int num1 = 2;
        int num2 = 3;

        func1(num1, num2);
        cout << "results of func1:" << endl;
        cout << "num1: " << num1 << ", num2: " << num2 << endl;
        func2(num1, num2);
        cout << "results of func2:" << endl;
        cout << "num1: " << num1 << ", num2: " << num2 << endl;

        return 0;
    }