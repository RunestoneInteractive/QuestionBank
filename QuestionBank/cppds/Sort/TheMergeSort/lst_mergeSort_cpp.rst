.. activecode:: lst_mergeSort_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Sort
  :subchapter: TheMergeSort
  :topics: Sort/TheMergeSort
  :from_source: T
  :caption: The Merge Sort
  :language: cpp

  #include <iostream>
  #include <vector>
  using namespace std;

  //function that prints the vector
  void printl(vector<int> avector) {
      for (unsigned int i=0; i<avector.size(); i++) {
          cout << avector[i] << " ";
      }
      cout << endl;
  }

  //function sorts using mergesort.
  vector<int> mergeSort(vector<int> avector) {
      cout<<"Splitting ";
      printl(avector);
      if (avector.size()>1) {
          int mid = avector.size()/2;
          //C++ Equivalent to using Python Slices
          vector<int> lefthalf(avector.begin(),avector.begin()+mid);
          vector<int> righthalf(avector.begin()+mid,avector.begin()+avector.size());

          lefthalf = mergeSort(lefthalf);
          righthalf = mergeSort(righthalf);

          unsigned i = 0;
          unsigned j = 0;
          unsigned k = 0;
          while (i < lefthalf.size() && j < righthalf.size()) {
              if (lefthalf[i] < righthalf[j]) {
                  avector[k]=lefthalf[i];
                  i++;
              } else {
                  avector[k] = righthalf[j];
                  j++;
              }
              k++;
          }

          while (i<lefthalf.size()) {
              avector[k] = lefthalf[i];
              i++;
              k++;
          }

          while (j<righthalf.size()) {
              avector[k]=righthalf[j];
              j++;
              k++;
          }

      }
      cout<<"Merging ";
      printl(avector);

      return avector;
  }

  int main() {
      // Vector initialized using a static array
      static const int arr[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
      vector<int> avector (arr, arr + sizeof(arr) / sizeof(arr[0]) );

      printl(mergeSort(avector));

      return 0;
  }