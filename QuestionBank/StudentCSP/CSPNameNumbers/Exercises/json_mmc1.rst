.. mchoice:: json_mmc1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F
   :correct: c
   :answer_a: name = dList.get("last_name", None)
   :answer_b: name = dlist[0][last_name]
   :answer_c: name = dlist[0].get("last_name")
   :answer_d: name = dList[0]["first name"]
   :feedback_a: Can you use get with a list?
   :feedback_b: The attribute name needs to be in quotes.
   :feedback_c: Can use get with an attribute name to get the value.
   :feedback_d: This gets the first name, not the last name

   What line would you use after the code below to get the value of the last_name from the first item from dList?

   .. code-block:: python

      data = '''
      [{
          "id": 1,
          "first_name": "Jeanette",
          "last_name": "Penddreth",
          "email": "jpenddreth@census.gov",
          "gender": "non-binary",
          "ip_address": "26.58.193.2",
        }, {
          "id": 2, 
          "first_name": "Giavani",
          "last_name" : "Russo"
      }]'''
      dList = json.loads(data)