.. activecode:: String_Slice1_ch17
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPStringPieces
   :subchapter: createPartsOfStrings
   :topics: CSPStringPieces/createPartsOfStrings
   :from_source: T
   :nocodelens:

   namePart = "name: Anu Gao"
   posName = namePart.find("name:")
   if (posName > -1):
       name = namePart[posName+6:len(namePart)]
   else:
       name = "Unknown"
   print(name)