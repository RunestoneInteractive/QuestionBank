.. mchoice:: question_inheritance_2
   :author: bmiller
   :difficulty: 1.9380530973
   :basecourse: fopp
   :chapter: Inheritance
   :subchapter: inheritVarsAndMethods
   :topics: Inheritance/inheritVarsAndMethods
   :from_source: T
   :answer_a: We are Siamese if you please. We are Siamese if you don’t please.
   :answer_b: Error
   :answer_c: Pumpkin
   :answer_d: Nothing. There’s no print statement.
   :feedback_a: another_cat is an instance of Siamese, so its song() method is invoked.
   :feedback_b: another_cat is an instance of Siamese, so its song() method is invoked.
   :feedback_c: This would print if the statement was print new_cat.name.
   :feedback_d: There is a print statement in the method definition.
   :correct: a
   :pct_on_first: 0.7654867257
   :total_students_attempting: 226
   :num_students_correct: 223.0
   :mean_clicks_to_correct: 1.3946188341

   What would print after running the following code:
   
   .. code-block:: python
   
     new_cat = Cheshire("Pumpkin”)
     class Siamese(Cat):
       def song(self):
         print("We are Siamese if you please. We are Siamese if you don’t please.")
     another_cat = Siamese("Lady")
     another_cat.song()