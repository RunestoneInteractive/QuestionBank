.. codelens:: functBuiltin_codelens_line2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-builtin
    :topics: 04-functions/04-builtin
    :from_source: T
    :question: What is the next line that will execute after the line with the red arrow executes?
    :breakline: 3
    :feedback: Remember what the len function does.
    :correct: line

    city_name = "Detroit"
    num = 10
    if len(city_name) > num:
      print("Long city name")
    else:
      print("Short city name")