.. mchoice:: mutobj-q1
    :author: bmiller
    :difficulty: 2.6822429907
    :basecourse: fopp
    :chapter: Functions
    :subchapter: PassingMutableObjects
    :topics: Functions/PassingMutableObjects
    :from_source: T
    :pct_on_first: 0.5794392523
    :total_students_attempting: 107
    :num_students_correct: 105.0
    :mean_clicks_to_correct: 1.4380952381

    What is the output of the following code fragment?
    
    .. sourcecode:: python
    
        def myfun(lst):
            lst = [1, 2, 3]
    
        mylist = ['a', 'b']
        myfun(mylist)
        print(mylist)
    
    - ['a', 'b']
    
      + Correct! ``mylist`` is not changed by the assignment in ``myfun``.
    
    - [1, 2, 3]
    
      - Incorrect. ``mylist`` is not changed by the assignment in ``myfun``.