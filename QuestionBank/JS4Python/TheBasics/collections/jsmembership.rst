.. activecode:: jsmembership
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    let mylist = [1, 2, 3, "foo", "bar"]
    if (mylist.includes(3)) {
        writeln('yes, includes returns true')
    }
    // indexOf returns the location of item or -1 if not found
    if (mylist.indexOf(3) > -1) {
        writeln('yes, index is > -1')
    }

    // BEWARE this does not work as expected
    if (3 in mylist) {
        writeln('yes, 3 is in mylist')
    }

    if ("foo" in mylist) {
        writeln('yes, foo is in mylist')
    } else {
        writeln("what?")
    }