.. activecode:: output_vars_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: OutputtingVariables
   :topics: Chapter2/OutputtingVariables
   :from_source: T
   :language: cpp
   :caption: Condensing The Code

   This program does the same thing as the previous, but the print
   statements have been condensed to one line.  This is better style.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int hour, minute;
       char colon;

       hour = 11;
       minute = 59;
       colon = ':';

       cout << "The current time is " << hour << colon << minute << endl;

       return 0;
   }