.. activecode:: array_werror_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Array write error in C++
    :language: cpp

    #include <iostream>
    using namespace std;

    // Demonstrates how in iterating outside
    // of an arry in C++, can change data in other places
    int main(){
        int myarray[] = {2, 4};
        int otherdata[]={777, 777};
        for (int i=0; i<4; i++){
            myarray[i]=0;
            cout <<"myarray["<< i << "]=";
            cout << myarray[i]<< endl;
            cout << "add:" << &myarray[i] << endl;
        }

        for (int i=0; i<2; i++){
            cout <<"otherdata["<< i << "]=";
            cout << otherdata[i]<< endl;
            cout << "add:" << &otherdata[i] << endl;
        }

        return 0;
    }