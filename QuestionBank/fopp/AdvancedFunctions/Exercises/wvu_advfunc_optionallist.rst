.. activecode:: wvu_advfunc_optionallist
    :author: Brian Powell
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: AdvancedFunctions
    :subchapter: Exercises
    :topics: AdvancedFunctions/Exercises
    :from_source: F

    Write a function named **add_wvu()**. It should accept one parameter, an optional parameter named **colleges** designed to take a list. If an existing list is not provided for **colleges** when calling your function, your function should create a new list.

    Your function must append an entry containing "WVU" to the **colleges** list, and return the updated list.

    Be careful that if **add_wvu()** is called multiple times, any lists it generates are new and independent from other previously returned lists.
    

    ~~~~
    ====