.. mchoice:: retention_6_F16_q12
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: Exercises
   :topics: CSPIntroDecisions/Exercises
   :from_source: F
   :practice: T

   What is the output of the following code snippet?

   .. sourcecode:: python

      myDictionary = {'a': 1, 'b': 2}
      bvr = 'b'
      myDictionary['a'] = 10
      myDictionary['c'] = 30
      myDictionary[bvr] = 20
      print (len(myDictionary.keys()))

   ..

   -   2

       -   Incorrect! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.

   -   3

       +   Correct! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.

   -   4

       -   Incorrect! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.

   -   1

       -   Incorrect! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.

   -   None

       -   Incorrect! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.

   -   Error

       -   Incorrect! ``bvr`` will be replaced by its value, 'b', then the value corresponding to key 'b' in the dictionary will be updated to 20.