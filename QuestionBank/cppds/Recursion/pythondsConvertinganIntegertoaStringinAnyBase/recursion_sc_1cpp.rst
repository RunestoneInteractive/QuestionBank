.. actex:: recursion_sc_1cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
    :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
    :from_source: T
    :language: cpp
    :nocodelens:

    #include <iostream>
    #include <string>
    using namespace std;

    void testEqual(string a, string b){
        if (a == b){
            cout << "PASS" << endl;
        }
        else{
            cout << "Failed" << endl;
        }
    }

    string reverse(string s){
        //Code Here
        return s;
    }

    int main(){
        testEqual(reverse("hello"),"olleh");
        testEqual(reverse("l"),"l");
        testEqual(reverse("follow"),"wollof");
        testEqual(reverse(""),"");

        return 0;
    }