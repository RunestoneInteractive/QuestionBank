.. activecode:: lst_change11cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: DynamicProgramming
    :topics: Recursion/DynamicProgramming
    :from_source: T
    :caption: Recursively Counting Coins with Table Lookup C++
    :language: cpp

    //Recursive example of trying to get the least amount of coins to make up an amount of change.

    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;

    int recMC_greedy(vector<int> coinValueList, int change){
            if (change == 0){ //base case if, change is 0, then the number of coins have been finalized
                return 0;
            }
            else{
                int cur_max =* max_element(coinValueList.begin(), coinValueList.end());//use the maximum in the list to see how many of these can be used to form the sum
                int count=int(change/cur_max); //find how many of the max is needed to make the change so that the number of coins used is minimum
                coinValueList.erase(std::remove(coinValueList.begin(), coinValueList.end(), cur_max), coinValueList.end()); //erasing the current max so that a different max can be
                                                                                                                            //used in next recursion and continue the greedy process
                return count + recMC_greedy(coinValueList, change-cur_max * count); //returns the counts of the coins using recursion
                }
    }

    int main() {
      int arr2[] = {1, 5, 10, 21, 25};
      vector<int> coinValueList(arr2, arr2 + (sizeof(arr2)/ sizeof(arr2[0])));  //Initializing vector
      cout<<recMC_greedy(coinValueList, 63)<<endl; //using the greedy algorithm for the edge case 63 whose optimal solution is 3 coins of 21
      return 0;                                  //but greedy algorithm gives 6 coins which is not the most optimum solution
    }