.. activecode:: lst_recsumcpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Recursion
  :subchapter: pythondsCalculatingtheSumofaListofNumbers
  :topics: Recursion/pythondsCalculatingtheSumofaListofNumbers
  :from_source: T
  :caption: Recursion Summation C++
  :language: cpp

  //Example of summing a vector by using recursion.

  #include <iostream>
  #include <vector>
  using namespace std;

  int vectsum(vector<int> numVect){
      if (numVect.size() <= 1){
          return numVect[0];
      }
      else {
          vector<int> slice(numVect.begin() + 1, numVect.begin()+numVect.size());
          return numVect[0] + vectsum(slice); //function makes a recursive call to itself.
      }
  }

  int main() {
      int arr2[] = {1, 3, 5, 7, 9};
      vector<int> numVect(arr2, arr2 + (sizeof(arr2) / sizeof(arr2[0])));  //Initializes vector with same items as arr2.
      cout << vectsum(numVect) << endl;

      return 0;
  }