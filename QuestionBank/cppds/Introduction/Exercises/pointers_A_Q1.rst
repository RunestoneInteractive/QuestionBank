.. parsonsprob:: pointers_A_Q1
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: cppds
   :chapter: Introduction
   :subchapter: Exercises
   :topics: Introduction/Exercises
   :from_source: F
   :language: c++

   Construct a block of code that checks if the contents of the pointer are equal to foo and print "Hello world" if they are equal.
   -----
   int foo = 10;
   int* foobar;
   =====
   foobar = &foo;
   =====
   if(foo == *foobar) {
   =====
    cout << "Hello world" << endl;
   =====
   }
   =====
   if(foo == &foobar) { #distractor
   =====
   foo* == &foobar; #distractor