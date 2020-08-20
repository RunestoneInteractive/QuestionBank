.. activecode:: vector_no_reserve_cpp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Introduction
   :subchapter: CollectionData
   :topics: Introduction/CollectionData
   :from_source: T
   :caption: With use of ``reserve``
   :language: cpp

   //code from above but without the reserve
   #include <iostream>
   #include <vector>
   using namespace std;

   int main(){

       vector<int> intvector;
       // without intvector.reserve(50);

       for (int i=0; i<50; i++){
           intvector.push_back(i*i);
           cout << intvector[i] << endl;
           cout << "capacity: " << intvector.capacity() << endl;
       }
       return 0;
   }