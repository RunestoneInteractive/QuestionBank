.. activecode:: promise_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Javascript
    :subchapter: asyncJavascript
    :topics: Javascript/asyncJavascript
    :from_source: T
    :language: javascript

    async function fibb(n) {
        let p = new Promise(function (resolve, reject) {
            let a = 0;
            let b = 1;
            let c = 0;
            for (let i = 0; i < n; i++) {
                c = a + b;
                a = b;
                b = c;
            }
            if (c % 2 == 0) {
                reject(c);
            } else {
                resolve(c);
            }
        }
        return p;
    }

    fibb(1)
    .then( (r) => writeln(r) )
    .catch( (r) => writeln("rejected ", r) )