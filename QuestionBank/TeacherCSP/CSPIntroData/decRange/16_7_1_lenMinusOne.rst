.. mchoice:: 16_7_1_lenMinusOne
          :author: bmiller
          :difficulty: 3.0
          :basecourse: TeacherCSP
          :chapter: CSPIntroData
          :subchapter: decRange
          :topics: CSPIntroData/decRange
          :from_source: T
          :answer_a: If we started with len(source), we would get an error for indexing past the end of the list
          :answer_b: It is a mistake and should be len(source)
          :answer_c: Because we have -1 in the other two spots
          :correct: a
          :feedback_a: Right -- the end element is at index len(source)-1
          :feedback_b: No -- if accessed len(source) as an index, we would be going past the end of the list
          :feedback_c: We have -1 in the end position because we want to stop at zero, and we have an increment of -1 (last position)

           Why do we start at ``len(source)-1`` in this program?