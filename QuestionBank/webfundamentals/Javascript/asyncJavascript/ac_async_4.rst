.. activecode:: ac_async_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Javascript
    :subchapter: asyncJavascript
    :topics: Javascript/asyncJavascript
    :from_source: T
    :language: javascript

    async function getPrediction() {
        writeln("sending the request");
        let opts = {
            method: 'GET',
        }

        let resp = await fetch("/runestone/stocks/predict/AAPL", opts)
        writeln('got response');
        let prediction = await resp.json();
        writeln(prediction.stock);
        writeln(prediction.price);
        writeln("all done");
    }

    writeln("calling getPrediction")
    let p = getPrediction();
    writeln("back -- " + typeof p)