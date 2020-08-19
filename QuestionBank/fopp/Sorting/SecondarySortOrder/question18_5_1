.. mchoice:: question18_5_1
      :author: bmiller
      :difficulty: 3.0
      :basecourse: fopp
      :chapter: Sorting
      :subchapter: SecondarySortOrder
      :topics: Sorting/SecondarySortOrder
      :from_source: T
      :answer_a: first city name (alphabetically), then temperature (lowest to highest)
      :answer_b: first temperature (highest to lowest), then city name (alphabetically)
      :answer_c: first city name (alphabetically), then temperature (highest to lowest)
      :answer_d: first temperature (lowest to highest), then city name (alphabetically)
      :feedback_a: Correct! First we sort alphabetically by city name, then by the temperature, from lowest to highest.
      :feedback_b: The order of the tuple matters. The first item in the tuple is the first condition used to sort.
      :feedback_c: Not quite, remember that by default, the sorted function will sort by alphabetical order, or lowest to highest. Is the reverse parameter set to True? Has a negative sign been used in the key parameter?
      :feedback_d: The order of the tuple matters. The first item in the tuple is the first condition used to sort.
      :correct: a
      :practice: T
      :pct_on_first: 0.6538461538
      :total_students_attempting: 338
      :num_students_correct: 331.0
      :mean_clicks_to_correct: 1.6555891239

      What will the sorted function sort by?
      
      .. code-block:: python
      
         weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
                    'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
                    'Cairo': {'temp': 96, 'condition': 'sunny'},
                    'Berlin': {'temp': 89, 'condition': 'sunny'},
                    'Caloocan': {'temp': 78, 'condition': 'sunny'}}
      
         sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))