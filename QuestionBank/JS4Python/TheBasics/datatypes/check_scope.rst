.. clickablearea:: check_scope
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: datatypes
    :topics: TheBasics/datatypes
    :from_source: T
    :question: click on all of the variables that are correctly scoped
    :iscode:

    "use strict";
    function main(x) {
       :click-incorrect:z = 11:endclick:
       :click-correct:let y = 10:endclick:
       for (let i = 0; i < 10; i++) {
           :click-correct:y = y + 1:endclick:
       }
       :click-incorrect:writeln(i):endclick:
       :click-correct:writeln(y):endclick:
    }