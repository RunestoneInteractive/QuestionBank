.. mchoice:: jsq1_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: jsquiz1
    :subchapter: 
    :topics: jsquiz1/
    :from_source: T
    :answer_a: 6
    :answer_b: 5
    :answer_c: 3
    :answer_d: ReferenceError: i is not defined
    :correct: a

    What is the output of the following code snippet?

    ::

        var sum = 0;
        for(var i = 0; i < 3; i++) {
            sum += i
        }
        let last = sum + i
        console.log(last)