.. parsonsprob:: mixedupcode_question9_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-mixedupcode
   :topics: 09-dictionaries/09-mixedupcode
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Rearrange the code blocks so the code prints the key containing the lowest value of all the keys in the dictionary.
   -----
   sampleDict = {'Physics': 82, 'Math', : 65, 'History': 75}
   =====
   sampleDict['English'] = 66
   =====
   sampleDict['Ceramics'] = 90
   =====
   sampleDict['History'] = 64
   =====
   minimum_value = 0 #distractor
   =====
   minimum_value = sampleDict[sampleDict.keys()[0]]
   =====
   for key in sampleDict.keys():
   =====
   for key in sampleDict.keys: #distractor
   =====
    if sampleDict[key] <= minimum_value:
   =====
     minimum_value = sampleDict[key]
   =====
   print(minimum_value)