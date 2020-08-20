.. activecode:: js_closure_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: Advanced
    :subchapter: closures
    :topics: Advanced/closures
    :from_source: T
    :language: javascript

    function counter_maker() {
        let x = 0;

        let ctr = function() {
            x = x + 1;
            return x;
        }

        return ctr;
    }

    let counter1 = counter_maker()
    writeln(counter1())
    let counter2 = counter_maker()
    writeln(counter2())

    for(let i = 0; i < 5; i++) {
        writeln(counter1())
        writeln(counter2())
    }