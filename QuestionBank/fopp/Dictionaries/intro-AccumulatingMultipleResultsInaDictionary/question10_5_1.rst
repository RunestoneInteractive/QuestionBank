.. mchoice:: question10_5_1
   :author: bmiller
   :difficulty: 2.832034632
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: intro-AccumulatingMultipleResultsInaDictionary
   :topics: Dictionaries/intro-AccumulatingMultipleResultsInaDictionary
   :from_source: T
   :answer_a: print(txt['e'] > txt['t'])
   :answer_b: print(letter_counts['e'] > letter_counts['t'])
   :answer_c: print(letter_counts[e] > letter_counts[t])
   :answer_d: print(letter_counts[c] > txt[c])
   :answer_e: print(e[letter_counts] > t[letter_counts])
   :feedback_a: txt is the variable that has the original text, not the dictionary of counts.
   :feedback_b: letter_counts is the dictionary of counts; you want to compare the values associated with 'e' and 't'.
   :feedback_c: letter_counts is the dictionary of counts, but you don't want to evaluate e and t as variables in order to determine which keys to look up in the dictionary.
   :feedback_d: It seems like maybe you're guessing. Please review the material above and then try again.
   :feedback_e: It seems like you've reversed things. The variable that refers to the dictionary goes outside the square brackets; the key you're looking up goes inside.
   :correct: b
   :pct_on_first: 0.541991342
   :total_students_attempting: 1155
   :num_students_correct: 1133.0
   :mean_clicks_to_correct: 1.8331862312

   Consider example ac10_5_5 above. After the program runs, which of the following will print out True if there are more
   occurrences of *e* than *t* in the text of "A Study in Scarlet," and False if *t* occurred more frequently?