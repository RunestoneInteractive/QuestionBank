.. fillintheblank:: file_reading
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cpp4python
  :chapter: Input_and_Output
  :subchapter: InputandOutput
  :topics: Input_and_Output/InputandOutput
  :from_source: T

  Fill in the blank with the value of ``inputn`` when the following code runs.
  ::

      #include <fstream>
      #include <cstdlib>
      #include <iostream>
      using namespace std;

      main(){
        ifstream in_stream;
        ofstream out_stream;
        int inputn;

        out_stream.open("anotherFile.txt");
        out_stream << 25;
        out_stream << 15 << endl;
        out_stream << 101 << endl;

        in_stream.open("anotherFile.txt");
        in_stream >> inputn;
        cout << inputn;
        in_stream >> inputn;
      }

  - :101: That is the correct answer! Good job!
    :25: No. Hint: ``inputn`` is changed twice.
    :2515: No. Hint: ``inputn`` is changed twice.
    :15: No. Hint: note that there is no space between the first 25 and 15!
    :.*: No. Hint: Observe what specific numbers are being written to the file!