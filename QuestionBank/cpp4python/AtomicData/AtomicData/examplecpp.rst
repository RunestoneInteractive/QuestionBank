.. activecode:: examplecpp
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: F
    :language: cpp

    #include <iostream>
    using namespace std;

    int main( ) {
        int varName = 100;
        int *varPntr = &varName;

        cout << "varName value: " << varName << endl;
        cout << "varPntr location: " << varPntr << endl;
        cout << "varPntr points to varName: " << endl;
        cout << "dereference varPntr: " << *varPntr << "\n\n";

        varName = 50;

        cout << "varName changed: " << varName << endl;
        cout << "varPntr still points to varName: " << endl;
        cout << "dereference varPntr: " << *varPntr << "\n\n";

        *varPntr = 2000;
        cout << "Changed *varPntr, ie varName to: " << endl;
        cout << "dereference varPntr: " << *varPntr << "\n\n";

        return 0;
    }