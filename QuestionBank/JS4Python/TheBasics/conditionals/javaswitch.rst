.. activecode:: javaswitch
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: conditionals
    :topics: TheBasics/conditionals
    :from_source: T
    :language: javascript

    "use strict";
    main(85);
    main(70);
    main(99);
    main(10);

    function main(grade) {

       let tempgrade = Math.trunc(grade / 10);
       switch(tempgrade) {
       case 10:
       case 9:
           writeln('A');
           break;
       case 8:
           writeln('B');
           break;
       case 7:
           writeln('C');
           break;
       case 6:
           writeln('A');
           break;
       default:
           writeln('F');
       }
    }