.. mchoice:: jsq1_9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: jsquiz1
    :subchapter: 
    :topics: jsquiz1/
    :from_source: T
    :answer_a: Nothing
    :answer_b: 0
    :answer_c: 1
    :answer_d: some kind of error
    :correct: b

    what is the output of the following snippet of code?

    ::

        let i = 0;
        let sum = 0;
        do {
            sum = sum + i
            console.log(sum)
            i -= 1
        } while( i > 0 )