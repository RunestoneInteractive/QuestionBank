.. mchoice:: mutobj-q2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Functions
    :subchapter: PassingMutableObjects
    :topics: Functions/PassingMutableObjects
    :from_source: T
    :pct_on_first: 0.7428571429
    :total_students_attempting: 105
    :num_students_correct: 104.0
    :mean_clicks_to_correct: 1.25

    What is the output of the following code fragment?
    
    .. sourcecode:: python
    
        def myfun(lst):
            del lst[0]
    
        mylist = ['a', 'b']
        myfun(mylist)
        print(mylist)
    
    - ['a', 'b']
    
      - Incorrect. ``myfun`` alters the state of the list object by removing the value at slot 0.
    
    - ['b']
    
      + Correct! ``myfun`` alters the state of the list object by removing the value at slot 0.