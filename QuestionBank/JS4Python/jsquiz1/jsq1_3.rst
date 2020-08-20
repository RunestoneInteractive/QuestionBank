.. mchoice:: jsq1_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: jsquiz1
    :subchapter: 
    :topics: jsquiz1/
    :from_source: T
    :answer_a: ReferenceError: foo is not defeined
    :answer_b: ReferenceError: y is not defined
    :answer_c: NaN then 11
    :answer_d: 110 then 11
    :correct: c

    What is the output of the following?

    ::

        "use strict"
        var y = 100
        foo()

        function foo() {
            let x = 10 + y;
            var y
            y = 1
            let z = 10 + y
            console.log(x)
            console.log(z)
        }