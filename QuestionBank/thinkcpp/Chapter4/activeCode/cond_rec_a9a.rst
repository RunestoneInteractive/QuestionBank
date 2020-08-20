.. activecode:: cond_rec_a9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Below is one way to write the program.
   ~~~~
   void countdown (int num) {
       if (num != 0){
           cout << num << endl;
           num -= 1;
           countdown (num);
       }
       else {
           cout << "Blastoff!";
       }
   }