.. activecode:: strremjs
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: TheBasics
    :subchapter: datatypes
    :topics: TheBasics/datatypes
    :from_source: T
    :language: javascript

    function removeVowels(s) {
        const vowels = "aeiouAEIOU";
        let sWithoutVowels = "";
        for (let eachChar of s) {
            if (vowels.indexOf(eachChar) === -1) {
                sWithoutVowels = sWithoutVowels + eachChar
            }
        }
        return sWithoutVowels
    }