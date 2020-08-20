.. activecode:: js_scope_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: Advanced
    :subchapter: closures
    :topics: Advanced/closures
    :from_source: T
    :language: javascript


    function fact(n) {
        let result = 1;
        for(let i = n; i > 0; i--) {
            let y = 'block';
            var z = 'function'
            result = result * i;
        }
        writeln(x)
        //writeln(y, i) this is an error as y and i are no longer in scope.
        writeln(z)
        return result;
    }

    var x = 'global'
    writeln(fact(10))