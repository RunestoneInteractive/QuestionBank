.. activecode:: qs_ex1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: AdvancedJavascript
    :subchapter: mashup
    :topics: AdvancedJavascript/mashup
    :from_source: T
    :language: python

    Write a python function that given a URL like `http://example.com/api/getdata?id=1234&date=now&apikey=1234567` returns a dictionary containing the correct keys and values.
    ~~~~
    def query_string_parser(qs):
        # your code Here