.. mchoice:: header_files_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: header_files
   :topics: Chapter11/header_files
   :from_source: T
   :answer_a: #include <header.h>
   :answer_b: #include <"header.h">
   :answer_c: #include header.h
   :answer_d: #include "header.h"
   :correct: d
   :feedback_a: Incorrect! This is how we include standard library headers.
   :feedback_b: Incorrect! You should get rid of those brackets!
   :feedback_c: Incorrect! You're missing quotes!
   :feedback_d: Correct!

   If I have defined a structure in ``header.h``, how would I include it in the implementation file?