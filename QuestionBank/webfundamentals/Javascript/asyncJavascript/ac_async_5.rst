.. activecode:: ac_async_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Javascript
    :subchapter: asyncJavascript
    :topics: Javascript/asyncJavascript
    :from_source: T
    :language: javascript

    async function getPrediction(stock) {
        writeln("sending the request");
        let opts = {
            method: 'GET',
        }
        let resp = await fetch(`/runestone/stocks/predict/${stock}`, opts)
        writeln(`got response for ${stock}`);
        return resp.json();
    }

    let promiseList = [];
    for (let stock of ["AAPL", "GOOG", "FB", "AMZN", "MSFT"]) {
        promiseList.push(getPrediction(stock))
    }

    Promise.all(promiseList).then(function(plist) {
            writeln("all promises complete");
            for (let p of plist) {
                writeln(`${p.stock}, ${p.price}`)
            }
    });