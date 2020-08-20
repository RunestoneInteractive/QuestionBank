.. activecode:: json_ex1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: AdvancedJavascript
    :subchapter: mashup
    :topics: AdvancedJavascript/mashup
    :from_source: T
    :language: javascript

    x = [1, 2, 3.1415, "Hello World"]
    y = {first_name: "Joe", salary: 104000.50 }

    sval = JSON.stringify(y)
    writeln(sval)
    sobj = JSON.parse(sval)
    writeln(sobj)