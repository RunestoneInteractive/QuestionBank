.. activecode:: ac_async_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Javascript
    :subchapter: asyncJavascript
    :topics: Javascript/asyncJavascript
    :from_source: T
    :language: javascript

    function receiveResponse(resp) {
        writeln('received response')
        return resp.json();
    }

    function receiveJson (prediction) {
        writeln(prediction.stock);
        writeln(prediction.price);
    }

    writeln("sending the request");
    let opts = {
        method: 'GET',
    }

    let myPromise =
        fetch("/runestone/stocks/predict/AAPL", opts)
    let jp = myPromise.then(receiveResponse)
    jp.then(receiveJson)
    jp.catch( (err) => writeln('Error getting prediction, details: ' + err) );
    writeln("the request has been sent");