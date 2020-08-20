.. mchoice:: assess_question3_3_1_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: I.
   :answer_b: II.
   :answer_c: III.
   :answer_d: IV.
   :feedback_a: When an object is concatenated with another using +=, it extends the original object. If this is done in the longer form (item = item + object) then it makes a copy.
   :feedback_b: When an object is concatenated with another using +=, it extends the original object. If this is done in the longer form (item = item + object) then it makes a copy.
   :feedback_c: When an object is concatenated with another using +=, it extends the original object. If this is done in the longer form (item = item + object) then it makes a copy.
   :feedback_d: Yes, the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first version makes a new object entirely and reassigns to obj. The second version changes the original object so that the contents of object_two are added to the end of the first.
   :correct: d
   :practice: T
   :topics: TransformingSequences/ObjectsandReferences

   Which of these is a correct reference diagram following the execution of the following code?

   .. sourcecode:: python

    x = ["dogs", "cats", "birds", "reptiles"]
    y = x
    x += ['fish', 'horses']
    y = y + ['sheep']

   I.

   .. image:: Figures/week3a3_1.png
      :alt: First Potential Solution

   II.

   .. image:: Figures/week3a3_2.png
      :alt: Second Potential Solution

   III.

   .. image:: Figures/week3a3_3.png
      :alt: Third Potential Solution

   IV.

   .. image:: Figures/week3a3_4.png
      :alt: Fourth Potential Solution