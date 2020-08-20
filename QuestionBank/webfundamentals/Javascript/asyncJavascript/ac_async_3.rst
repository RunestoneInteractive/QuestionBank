.. activecode:: ac_async_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Javascript
    :subchapter: asyncJavascript
    :topics: Javascript/asyncJavascript
    :from_source: T
    :language: javascript

    writeln("sending the request");
    let opts = {
        method: 'GET',
    }

    fetch("/runestone/stocks/predict/AAPL", opts)
    .then(function (resp) {
        writeln('received response')
        return resp.json();
    })
    .then(function (prediction) {
        writeln(prediction.stock);
        writeln(prediction.price);
    })
    .catch( (err) => writeln('Error getting prediction, details: ' + err) );
    writeln("the request has been sent");