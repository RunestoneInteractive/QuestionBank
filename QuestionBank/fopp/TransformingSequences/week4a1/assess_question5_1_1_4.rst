.. fillintheblank:: assess_question5_1_1_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :practice: T

   What is the iterator (loop) variable in the following?

   .. sourcecode:: python

    rest = ["sleep", 'dormir', 'dormire', "slaap", 'sen', 'yuxu', 'yanam']
    let = ''
    for phrase in rest:
        let += phrase[0]

   The iterator variable is

   -  :phrase: Good work!
      :rest: rest is the sequence, not the iterator variable.
      :let: let is the accumulator variable, not the iterator variable.
      :.*: Incorrect, try again.