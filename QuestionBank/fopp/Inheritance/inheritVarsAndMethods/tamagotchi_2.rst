.. activecode:: tamagotchi_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: inheritVarsAndMethods
    :topics: Inheritance/inheritVarsAndMethods
    :from_source: T
    :nocanvas:
    :include: inheritance_cat_example

    p1 = Pet("Fido")
    print(p1) # we've seen this stuff before!

    p1.feed()
    p1.hi()
    print(p1)

    cat1 = Cat("Fluffy")
    print(cat1) # this uses the same __str__ method as the Pets do

    cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
    cat1.hi()
    print(cat1)

    print(cat1.chasing_rats())

    #print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!