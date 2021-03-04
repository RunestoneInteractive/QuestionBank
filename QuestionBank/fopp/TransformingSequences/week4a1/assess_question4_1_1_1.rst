.. mchoice:: assess_question4_1_1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: I.
   :answer_b: II.
   :answer_c: Neither is the correct reference diagram.
   :feedback_a: Yes, when we are using the remove method, we are just editing the existing list, not making a new copy.
   :feedback_b: When we use the remove method, we just edit the existing list. We do not make a new copy that does not include the removed object.
   :feedback_c: One of the diagrams is correct - look again at what is happening to lst.
   :correct: a
   :practice: T

   Which of these is a correct reference diagram following the execution of the following code?

   .. sourcecode:: python

    lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
    lst.remove('pluto')
    first_three = lst[:3]

   I.

   .. image:: Figures/week3a1_1.png
      :alt: First Potential Solution

   II.

   .. image:: Figures/week3a1_2.png
      :alt: Second Potential Solution