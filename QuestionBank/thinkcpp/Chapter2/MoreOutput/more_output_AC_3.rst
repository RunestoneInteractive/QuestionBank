.. activecode:: more_output_AC_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: MoreOutput
   :topics: Chapter2/MoreOutput
   :from_source: T
   :language: cpp
   :caption: Spaces Removed (messy)

   This program accomplishes the same thing as the one above.  The
   difference is that there are no spaces separating the different
   components of each line.  This is a matter of personal preference.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       cout<<"Goodbye, ";
       cout<<"cruel world!"<<endl;
   }