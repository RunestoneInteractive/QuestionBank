.. activecode:: Unordered_set_example
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: UnorderedSet
    :topics: CollectionData/UnorderedSet
    :from_source: T
    :language: cpp

    // Function that checks to see if a char
    // is in the unorderd set
    #include <iostream>
    #include <unordered_set>
    using namespace std;

    void checker(unordered_set<char> set, char letter){
        if(set.find(letter) == set.end()){
            cout << "letter " << letter << " is not in the set." << endl;
        }
        else{
            cout << "letter " << letter << " is in the set." << endl;
        }
    }

    int main(){
    unordered_set<char> charSet = {'d', 'c', 'b', 'a'};

    char letter = 'e';
    checker(charSet, letter);
    charSet.insert('e');
    checker(charSet, letter);
    return 0;
    }