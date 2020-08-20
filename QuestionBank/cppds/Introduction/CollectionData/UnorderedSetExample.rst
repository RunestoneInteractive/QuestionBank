.. activecode:: UnorderedSetExample
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :language: cpp

    //code detects if a specific char is in an unordered set.
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