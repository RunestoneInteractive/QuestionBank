.. activecode:: jsdictvals1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    const myDict = {foo: "bar", baz: 22, 33: 'hello'};
    let vals = []
    for (const key of Object.keys(myDict)) {
        vals.push(myDict[key])
    }
    writeln(vals)