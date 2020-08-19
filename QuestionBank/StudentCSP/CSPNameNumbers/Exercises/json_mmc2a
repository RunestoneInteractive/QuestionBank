.. mchoice:: json_mmc2a
   :author: Barbara  Ericson
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F
   :correct: d
   :answer_a: question = dict["question"]
   :answer_b: question = dict[results][0]["question"]
   :answer_c: question = dict[0]["question"]
   :answer_d: question = dict["results"][0]["question"]
   :feedback_a: The question is in a dictionary which is in a list which is in a dictionary
   :feedback_b: The attribute name needs to be in quotes.
   :feedback_c: The question is in a dictionary inside a list which is in a dictionary
   :feedback_d: This gets the value for the key "results" which is a list and then the first item in that list which is a dictionary and then the value for "question".
   :pct_on_first: 0.4310344828
   :total_students_attempting: 116
   :num_students_correct: 116.0
   :mean_clicks_to_correct: 1.9568965517

   Which line would you use after the code below to get the text of the first question?
   
   .. code-block:: python
   
      data = '''
      {
          "response_code": 0,
          "results: [{"category": "Entertainment", 
          "type": "multiple",
          "difficulty": "hard",
          "question": "Which of these was not in JoJo's Adventure?",
          "correct_answer": "JoJo Kikasu"}]  
      }'''
      dict = json.loads(data)