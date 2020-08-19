.. activecode:: compos_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Composition
   :topics: Chapter2/Composition
   :from_source: T
   :language: cpp
   :autograde: unittest

   Finish the code below so that the volume of a cylinder with
   radius r and height h is calculated and returned on the same line.
   Use 3.14 for pi.
   ~~~~
   double volume(int r, int h) {
       // You may only use the next line for your code.
       return ;
   }

   ====

   #define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do   this in one cpp file
   #include <catch.hpp>

   TEST_CASE( "Volume Check", "[volume]" ) {
   REQUIRE( volume(6,6) == 678.24 );
   REQUIRE( volume(3,6) == 169.56 );
   REQUIRE( volume(0,6) == 0 );
   REQUIRE( volume(6,0) == 0 );
   }