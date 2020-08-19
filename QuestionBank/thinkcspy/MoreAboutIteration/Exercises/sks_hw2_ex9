.. activecode:: sks_hw2_ex9
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python

    Write a program that will approximate the value of π.  You can do this by computing π to be the 
    ratio of the area of a circle to the area of the square that bounds that circle. Assume a circle of 
    radius 0.5 enclosed by a 1x1 square.  The area of the circle then is πr^2=π/4, since r=0.5=1/2 
    and the area of the square is 1. To approximate the ratio, take a large number of uniformly distributed 
    random points. These points can be in any position within the square i.e. between (0,0) and (1,1). 
    If they fall within the circle, they are considered in, otherwise they are out. Keep track of the total 
    number of points, and the number of points that are inside the circle. If we divide the number of points 
    within the circle by the total number of points, we should get a value that is an approximation of the 
    ratio of the areas, which should equate to π/4.  Hence, you would get an estimate of π to be 
    4 * approximate ratio of areas.  Of course, larger the number of points, better will be our estimate of the areas.  

    To get a uniformly distributed random point, use the function random.random().
    Example usage of the function is:
    ::

        import random as r
        x = r.random()

    ~~~~
    # Write your code here