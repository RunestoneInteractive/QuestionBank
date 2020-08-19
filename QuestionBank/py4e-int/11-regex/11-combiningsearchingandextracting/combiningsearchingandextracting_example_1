.. activecode:: combiningsearchingandextracting_example_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-combiningsearchingandextracting
   :topics: 11-regex/11-combiningsearchingandextracting
   :from_source: T
   :nocodelens:

   # Search for lines that start with 'X', followed by any non-whitespace characters
   # and ':', followed by a space and any number. The number can contain a
   # decimal
   import re
   s = ['X-DSPAM-Confidence: 0.8475', 'X-DSPAM-Probability: 0.0000', 'X-DSPAM-Confidence: 0.6178', 'X-DSPAM-Probability: 0.0000']
   for item in s:
       x = re.findall('^X\S*: ([0-9.]+)', item)
       if len(x) > 0:
           print(x)