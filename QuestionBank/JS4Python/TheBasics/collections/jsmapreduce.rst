.. activecode:: jsmapreduce
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    let data = '9,8,4,3,5,5,1,1,5,8,9,7,7,7,6'
    sum = data.split(',')
        .map(function(t) {return parseInt(t)})
        .reduce((a,b) => a+b)

    writeln(sum)