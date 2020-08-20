.. activecode:: select1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Dynamic
    :subchapter: prototype1
    :topics: Dynamic/prototype1
    :from_source: T
    :language: html

    <select id="myid"></select>
    <script type="text/javascript">
        function populateSelect(selectId, sList) {
            let sel = document.getElementById(selectId)
            for (let s of sList) {
                let opt = document.createElement("option")
                opt.value = s
                opt.innerHTML = s
                sel.appendChild(opt)
            }
        }
        populateSelect('myid', ['one', 'two', 'three', 'four'])
    </script>