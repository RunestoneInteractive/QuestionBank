.. activecode:: lst_selectionsortcode_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Sort
  :subchapter: TheSelectionSort
  :topics: Sort/TheSelectionSort
  :from_source: T
  :caption: The Selection Sort
  :language: cpp

  #include <iostream>
  #include <vector>
  using namespace std;
  //function that sorts through values in vector through selection sort
  vector<int> selectionSort(vector<int> avector) {
      for (int fillslot = (avector.size() - 1); fillslot >= 0; fillslot--) {
          int positionOfMax = 0;
          for (int location = 1; location < fillslot + 1; location++) {
              if (avector[location] > avector[positionOfMax]) {
                  positionOfMax = location;
              }
          }

          int temp = avector[fillslot];
          avector[fillslot] = avector[positionOfMax];
          avector[positionOfMax] = temp;
      }
      return avector;
  }

  int main() {
      // Vector initialized using a static array
      static const int arr[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
      vector<int> avector (arr, arr + sizeof(arr) / sizeof(arr[0]) );

      // Call to the selectionSort function
      vector<int> updatedAvector = selectionSort(avector);

      // print the vector
      for (unsigned int i = 0; i < updatedAvector.size(); i++) {
          cout << updatedAvector[i] << " ";
      }
      cout << endl;

      return 0;
  }