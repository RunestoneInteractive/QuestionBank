.. activecode:: convert1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: datatypes
    :topics: TheBasics/datatypes
    :from_source: T
    :language: javascript

    var main = function() {
        var fahr;
        fahr = prompt("Enter the temperature in F: ");
        const ratio = 5.0/9.0;
        let cel = (fahr - 32) * ratio;
        writeln("The temperature in C is: " + cel);
    }

    main()