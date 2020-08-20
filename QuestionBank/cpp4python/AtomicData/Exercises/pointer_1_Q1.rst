.. parsonsprob:: pointer_1_Q1
   :author: Matthew Zuniga
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: AtomicData
   :subchapter: Exercises
   :topics: AtomicData/Exercises
   :from_source: F

   Construct a program that creates a pointer called foobar and compares its values with the int foo.  Print "Hello World" if they are equal.
   
   -----
   int foo = 1;
   int* foobar;
   =====
   foobar = &foo;
   =====
   if(foo = *foobar) {
   =====
    std::cout << "Hello World" << std::endl;
   =====
   }
   =====
   if(foo = &foobar) { #distractor

config values (conf.py):

- parsons_div_class - custom CSS class of the component's outermost div