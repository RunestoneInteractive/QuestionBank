.. activecode:: arraykeys
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    let mylist = [1, 2, 3, "foo", "bar"];
    for (let k of Object.keys(mylist)) {
        writeln(k)
    }