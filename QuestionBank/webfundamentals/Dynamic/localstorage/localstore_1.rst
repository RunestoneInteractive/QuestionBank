.. activecode:: localstore_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Dynamic
    :subchapter: localstorage
    :topics: Dynamic/localstorage
    :from_source: T
    :language: javascript

    counter = localStorage.counter
    writeln("counter is " + counter);
    if (! counter) {
        counter = 1
    } else {
        counter += 1
    }
    localStorage.counter = counter
    writeln("counter is now " + localStorage.counter)