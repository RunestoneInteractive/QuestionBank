.. mchoice:: 16_5_1_reversinglist
                  :author: bmiller
                  :difficulty: 3.0
                  :basecourse: TeacherCSP
                  :chapter: CSPIntroData
                  :subchapter: revList
                  :topics: CSPIntroData/revList
                  :from_source: T
                  :answer_a: Because we started at 0 and went to len(source).
                  :answer_b: Because we put the new element ahead of the others in soFar.
                  :answer_c: Because of the square brackets around source[index].
                  :correct: b
                  :feedback_a: That is the normal way of accessing each element, one at a time.
                  :feedback_b: If we had done soFar = soFar + [source[index]], soFar would have just duplicated the list, in order.
                  :feedback_c: We need those in order to add elements into the list.  You can only add a list to a list.

                   Why did the code above end up reversing the list?