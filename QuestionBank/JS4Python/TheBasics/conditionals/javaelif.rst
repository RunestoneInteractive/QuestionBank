.. activecode:: javaelif
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: conditionals
    :topics: TheBasics/conditionals
    :from_source: T
    :language: javascript

    main(85)
    main(44)
    main(98)

    function main(grade) {
        if (grade < 60) {
            writeln('F');
        } else {
            if (grade < 70) {
                writeln('D');
            } else {
                if (grade < 80) {
                    writeln('C');
                } else {
                    if (grade < 90) {
                        writeln('B');
                    } else {
                        writeln('A');
                    }
                }
            }
        }
    }