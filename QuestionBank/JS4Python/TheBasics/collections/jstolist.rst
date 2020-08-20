.. activecode:: jstolist
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: collections
    :topics: TheBasics/collections
    :from_source: T
    :language: javascript

    l1 = "the quick brown fox jumps over".split(/\s/);
    writeln(l1)
    l2 = Array.from("the quick brown fox jumps over")
    writeln(l2)
    // Join works similarly, but the sparator is the argument not the list
    writeln(l1.join(":"))