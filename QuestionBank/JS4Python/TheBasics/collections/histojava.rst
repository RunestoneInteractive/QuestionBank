.. activecode:: histojava
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    "use strict"
    let main = function() {
        let count = new Array(10).fill(0);
        let data = '9,8,4,3,5,5,1,1,5,8,9,7,7,7,6'

        for (let num of data.split(',')) {
            const idx = parseInt(num);
            count[idx] = count[idx] + 1
        }

        for(let num in count) {
            writeln(num + " occured " + count[num] + " times.")
        }
    }

    main()