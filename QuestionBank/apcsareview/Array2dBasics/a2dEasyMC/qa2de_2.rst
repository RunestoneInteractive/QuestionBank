.. mchoice:: qa2de_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: a2dEasyMC
   :topics: Array2dBasics/a2dEasyMC
   :from_source: T
   :answer_a: <code>strGrid[0][2] = "S";</code>
   :answer_b: <code>strGrid[1][3] = "S";</code>
   :answer_c: <code>strGrid[3][1] = "S";</code>
   :answer_d: <code>strGrid[2][0] = "S";</code>
   :answer_e: <code>strGrid[0][0] = "S";</code>
   :correct: d
   :feedback_a: The code <code>letterGrid[0][2] = "S";</code> actually sets the 1st row and 3rd column to hold a reference to the <code>String</code> object "S".
   :feedback_b: This would be true if row and column indicies started at 1 instead of 0 and if this was in column major order.
   :feedback_c: This would be true if row and column indicies started at 1 instead of 0.
   :feedback_d: In row-major order the row is specified first followed by the column.  Row and column indicies start with 0.  So <code>letterGrid[2][0]</code> is the 3rd row and 1st column.
   :feedback_e: This would set the element at the first row and column.

   Which of the following statements assigns the letter S to the third row and first column of a two-dimensional array named ``strGrid`` (assuming row-major order).