.. activecode:: q2_dict_answer_with_text
    :author: Karl Sickendick
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F

    Give the Python interpreter’s response to each of the following from a continuous interpreter session:

     >>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
     >>> d['banana']

     >>> d['oranges'] = 20
     >>> len(d)

     >>> 'grapes' in d

     >>> d['pears']

     >>> d.get('pears', 0)

     >>> fruits = d.keys()
     >>> fruits.sort()
     >>> print(fruits)

     >>> del d['apples']
     >>> 'apples' in d

    Be sure you understand why you get each result. Feel free to try them out in the code window below. Then apply what you have learned to fill in the body of the function below, and add code for the tests indicated:

    ~~~~
    def add_fruit(inventory, fruit, quantity=0):
         pass

    # make these tests work...
    new_inventory = {}
    add_fruit(new_inventory, 'strawberries', 10)
    #  test that 'strawberries' in new_inventory
    #  test that new_inventory['strawberries'] is 10
    add_fruit(new_inventory, 'strawberries', 25)
    #  test that new_inventory['strawberries'] is now 35)