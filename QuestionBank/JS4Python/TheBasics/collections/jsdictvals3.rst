.. activecode:: jsdictvals3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    const myDict = {foo: "bar", baz: 22, 33: 'hello'};
    const vals = Object.keys(myDict).map(key => myDict[key])
    writeln(vals)