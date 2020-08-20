.. activecode:: intro_7cpp
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: F
    :caption: Using a Hash Table C++
    :language: cpp

    #include <iostream>
    #include <map>
    #include <string>
    using namespace std;

    int main() {
        map<string, string> capitals;

        capitals["Iowa"] = "Desmoines";
        capitals["Wisconsin"] = "Madison";
        cout << capitals["Iowa"] << endl;
        capitals["Utah"] = "SaltLakeCity";

        capitals["California"] = "Sacramento";
        cout << capitals.size() << endl;

        for (map<string, string>::iterator it=capitals.begin(); it!=capitals.end(); ++it){
            cout << it->second << " is the capital of " << it->first << '\n';
        }
    }