.. mchoice:: question17_3_1
   :author: bmiller
   :difficulty: 2.3139534884
   :basecourse: fopp
   :chapter: NestedData
   :subchapter: jsonlib
   :topics: NestedData/jsonlib
   :from_source: T
   :answer_a: json.loads(d)
   :answer_b: json.dumps(d)
   :answer_c: d.json()
   :feedback_a: loads turns a json-formatted string into a list or dictionary
   :feedback_b: dumps turns a list or dictionary into a json-formatted string
   :feedback_c: .json() tries to invoke the json method, but that method is not defined for dictionaries
   :correct: b
   :practice: T
   :pct_on_first: 0.6715116279
   :total_students_attempting: 344
   :num_students_correct: 342.0
   :mean_clicks_to_correct: 1.418128655

   Because we can only write strings into a file, if we wanted to convert a dictionary `d` into a json-formatted string so that we could store it in a file, what would we use?