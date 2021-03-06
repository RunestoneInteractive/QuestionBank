.. activecode:: binary_search_cpp_array
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: SearchHash
    :subchapter: TheBinarySearch
    :topics: SearchHash/TheBinarySearch
    :from_source: T
    :caption: Optimized Binary Search
    :language: cpp

    #include <iostream>
    using namespace std;

    //Checks to see if item is in a vector
    //retruns true or false (1 or 0)
    //using binary Search and
    //uses start and end indices
    bool binarySearch(int arr[], int item, int start, int end) {
        if (end >= start) {
            int mid = start + (end - start) / 2;
            if (arr[mid] == item)
                return true;
            if (arr[mid] > item)
                return binarySearch(arr, item, start, mid - 1);
            else {
                return binarySearch(arr, item, mid + 1, end);
            }
        }

        return false;
    }

    bool binarySearchHelper(int arr[], int size, int item) {
        return binarySearch(arr, item, 0, size);
    }

    int main(void) {
        int arr[] = {0, 1, 2, 8, 13, 17, 19, 32, 42};
        int arrLength = sizeof(arr) / sizeof(arr[0]);

        cout << binarySearchHelper(arr, arrLength, 3) << endl;
        cout << binarySearchHelper(arr, arrLength, 13) << endl;

        return 0;
    }