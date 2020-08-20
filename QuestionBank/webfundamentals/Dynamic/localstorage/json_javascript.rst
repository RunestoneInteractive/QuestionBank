.. activecode:: json_javascript
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Dynamic
    :subchapter: localstorage
    :topics: Dynamic/localstorage
    :from_source: T
    :language: javascript

    x = JSON.stringify([1,2,3.1415, 4])
    write("x is a")
    writeln(typeof x)
    writeln(x)

    y = JSON.parse(x)
    write("y is a ")
    writeln(typeof y)
    writeln(y)
    y.push(5)
    writeln(y)