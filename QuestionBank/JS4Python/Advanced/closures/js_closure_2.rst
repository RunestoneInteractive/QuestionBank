.. activecode:: js_closure_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: Advanced
    :subchapter: closures
    :topics: Advanced/closures
    :from_source: T
    :language: javascript

    var v = 1;
    function fun1() {
        writeln(v);
    }

    function fun2() {
        var v = 2;
        fun1();
    };

    fun2();