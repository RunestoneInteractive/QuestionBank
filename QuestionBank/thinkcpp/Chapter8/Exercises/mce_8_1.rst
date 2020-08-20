.. mchoice:: mce_8_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: Exercises
    :topics: Chapter8/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.0

    Which of the following are compound values?
    
    .. code-block:: cpp
    
      struct Student {
        string firstName, lastName;
        int year;
        double gpa;
      };
    
      struct Professor {
        string firstName, lastName;
        string department;
        int class;
      };
    
      int main() {
        Student x = { "John", "Doe", 2, 3.46 };
        Student y = { "Jane", "Doe", 3, 3.68 };
        Professor z = { "Richard", "Roe", "Computer Science", 101 };
        string college = "University of College";
        int studentPop = 3400;
        double avgGPA = 3.2;
      }
    
    - ``x``
    
      + ``x`` is a ``Student`` which is a ``struct``.
    
    - ``y``
    
      + ``y`` is a ``Student`` which is a ``struct``.
    
    - ``z``
    
      + ``z`` is a ``Professor`` which is a ``struct``.
    
    - ``college``
    
      + ``college`` is a ``string`` which is made up of characters.
    
    - ``studentPop``
    
      - An ``int`` is not a compound value.
    
    - ``avgGPA``
    
      - A ``double`` is not a compound value.