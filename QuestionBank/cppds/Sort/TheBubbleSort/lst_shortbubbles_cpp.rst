.. activecode:: lst_shortbubbles_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Sort
  :subchapter: TheBubbleSort
  :topics: Sort/TheBubbleSort
  :from_source: T
  :caption: The Short Bubble Sort in C++
  :language: cpp

  #include <iostream>
  #include <vector>

  using namespace std;

  vector<int> shortBubbleSort(vector<int> avector){ //the vector for bubble sort
      bool exchanges = true;
      int passnum = avector.size();
      //while vector size is greater than 0 and exchanges = true
      while (passnum > 0 && exchanges) {
          exchanges = false;
         //loops through vector, exchanging values until it reaches the end of vector.
          for(int i = 0; i < passnum; i++){
              if(avector[i] > avector[i+1]){
                  exchanges = true;
                  int temp = avector[i];
                  avector[i] = avector[i+1];
                  avector[i+1] = temp;
              }
          }
          //subtracts from the passnum variable so that the next passthrough is one less
          //than the previous, because the largest value has already 'bubbled' all the way up.
          passnum = passnum - 1;
      }
      return avector;
  }

  int main() {
      // Vector initialized using a static array
      static const int arr[] = {20,30,40,90,50,60,70,80,110,100};
      vector<int> avector (arr, arr+ sizeof(arr)/sizeof(arr[0])); //intializes vector

      vector<int> bvector = shortBubbleSort(avector);

      for(unsigned int i = 0; i < bvector.size(); i++){
        cout<< bvector[i] << " ";
      }
      return 0;
  }