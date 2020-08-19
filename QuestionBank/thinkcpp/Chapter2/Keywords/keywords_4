.. activecode:: keywords_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Keywords
   :topics: Chapter2/Keywords
   :from_source: T
   :language: cpp
   :autograde: unittest

   Fix the code below so that it runs without errors.  Hint: you might
   need to change the names of some variables.
   ~~~~
   int main () {
       int friend = 4;
       int enemy = friend * (-1);
       cout << "enemy = " << enemy << endl;

       // Do not modify anything below.
       return 0;
   }

   ====

   #define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do   this in one cpp file
   #include <catch.hpp>

   TEST_CASE( "Compile Check", "[compile]" ) {
   REQUIRE( main() == 0 );
   }