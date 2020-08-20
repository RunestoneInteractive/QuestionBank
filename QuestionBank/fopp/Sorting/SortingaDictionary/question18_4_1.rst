.. mchoice:: question18_4_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sorting
   :subchapter: SortingaDictionary
   :topics: Sorting/SortingaDictionary
   :from_source: T
   :multiple_answers: 
   :answer_a: sorted(ks, key=g)
   :answer_b: sorted(ks, key=lambda x: g(x, d))
   :answer_c: sorted(ks, key=lambda x: d[x])
   :correct: b,c
   :feedback_a: g is a function that takes two parameters. The key function passed to sorted must always take just one parameter.
   :feedback_b: The lambda function takes just one parameter, and calls g with two parameters.
   :feedback_c: The lambda function looks up the value of x in d.
   :practice: T
   :pct_on_first: 0.0901408451
   :total_students_attempting: 355
   :num_students_correct: 350.0
   :mean_clicks_to_correct: 2.8

   Which of the following will sort the keys of d in ascending order of their values (i.e., from lowest to highest)?
   
   .. code-block:: python
   
        L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]
   
        d = {}
        for x in L:
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
   
        def g(k, d):
            return d[k]
   
        ks = d.keys()