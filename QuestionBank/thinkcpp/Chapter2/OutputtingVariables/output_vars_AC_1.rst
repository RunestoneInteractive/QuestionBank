.. activecode:: output_vars_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: OutputtingVariables
   :topics: Chapter2/OutputtingVariables
   :from_source: T
   :language: cpp
   :caption: Time Output

   This program outputs the current time, according to the values you
   provide for hour and minute.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int hour, minute;
       char colon;

       hour = 11;
       minute = 59;
       colon = ':';

       cout << "The current time is ";
       cout << hour;
       cout << colon;
       cout << minute;
       cout << endl;

       return 0;
   }