.. activecode:: dictjava
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    "use strict";
    main()

    function main() {

        const data = document.getElementById('alice30.txt').innerText

        let count = {}

        for (let word of data.split(/\s/)) {
            word = word.toLowerCase();
            count[word] = (count[word] || 0) + 1
        }

        for (let key of Object.keys(count)) {
            writeln(key + ": " + count[key])
        }
    }