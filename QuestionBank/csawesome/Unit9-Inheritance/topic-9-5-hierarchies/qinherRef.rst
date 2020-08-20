.. mchoice:: qinherRef
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-5-hierarchies
   :topics: Unit9-Inheritance/topic-9-5-hierarchies
   :from_source: T
   :practice: T
   :answer_a: Person p = new Person();
   :answer_b: Person p = new Student();
   :answer_c: Student s = new Student();
   :answer_d: Student s = new Person();
   :correct: d
   :feedback_a: This declares and creates an object of the same class Person.
   :feedback_b: This is allowed because a Student is-a Person.
   :feedback_c: This declares and creates an object of the same class Student.
   :feedback_d: This is not allowed because a Person is not always a Student.
   :pct_on_first: 0.5235173824
   :total_students_attempting: 1467
   :num_students_correct: 1460.0
   :mean_clicks_to_correct: 1.7739726027

   A class Student inherits from the superclass Person. Which of the following assignment statements will give a compiler error?