.. activecode:: lst_shell_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Sort
  :subchapter: TheShellSort
  :topics: Sort/TheShellSort
  :from_source: T
  :caption: The Shell Sort
  :language: cpp

  #include <iostream>
  #include <vector>
  using namespace std;

  // print the sorted vector
  void printl(vector<int> avector) {
      for (unsigned int i=0; i<avector.size(); i++) {
          cout << avector[i] << " ";
      }
      cout << endl;
  }
  // function returns sorted subvector
  vector<int> gapInsertionSort(vector<int> avector, int start, int gap) {
      for (unsigned int i = start + gap; i < avector.size(); i += gap) {
          int currentvalue = avector[i];
          int position = i;

          while (position >= gap && avector[position - gap] > currentvalue) {
              avector[position] = avector[position - gap];
              position -= gap;
          }
          avector[position] = currentvalue;
      }
      return avector;
  }

  //function shellsorts through the vector
  vector<int> shellSort(vector<int> avector) {
      int subvectorcount = avector.size() / 2; //cuts vector by half
      while (subvectorcount > 0) {
          for (int startposition = 0; startposition < subvectorcount;
               startposition++) {
              avector = gapInsertionSort(avector, startposition, subvectorcount);/*
        runs avector through gapInsertionSort function
         */
          }
          cout << "After increments of size " << subvectorcount
               << " The vector is: " << endl;
          printl(avector);

          subvectorcount = subvectorcount / 2; //cuts vector in half
      }

      return avector;
  }

  int main() {
      // Vector initialized using a static array
      static const int arr[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
      vector<int> avector (arr, arr + sizeof(arr) / sizeof(arr[0]));

      printl(shellSort(avector));

      return 0;
  }