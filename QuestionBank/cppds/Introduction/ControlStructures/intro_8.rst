.. activecode:: intro_8
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ControlStructures
    :topics: Introduction/ControlStructures
    :from_source: F
    :language: cpp
    :caption: Processing Each Character in a List of Strings

    #include <iostream>
    #include <string>
    using namespace std;

    int main() {
        string wordList[] = {"cat", "dog", "rabbit"};
        int wordListSize = sizeof(wordList) / sizeof(wordList[0]);

        char letterlist[wordListSize];
        int indx = 0;

        for (int i = 0; i < wordListSize; i++) {
                for (unsigned int j = 0; j < wordList[i].size(); j++) {
                        letterlist[indx] = wordList[i][j];
                        indx = indx + 1;
                }
        }

        cout << letterlist << endl;
    }