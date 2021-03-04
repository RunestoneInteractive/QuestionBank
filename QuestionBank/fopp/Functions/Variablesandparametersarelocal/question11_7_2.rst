.. fillintheblank:: question11_7_2
   :author: bmiller
   :difficulty: 4.1233307148
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Variablesandparametersarelocal
   :topics: Functions/Variablesandparametersarelocal
   :from_source: T
   :pct_on_first: 0.2191673213
   :total_students_attempting: 1273
   :num_students_correct: 1121.0
   :mean_clicks_to_correct: 3.049955397

   Which of the following are local variables? Please, write them in order of what line they are on in the code.
   
   .. sourcecode:: python
   
    numbers = [1, 12, 13, 4]
    def foo(bar):
        aug = str(bar) + "street"
        return aug
   
    addresses = []
    for item in numbers:
        addresses.append(foo(item))
   
   
   The local variables are
   
   -  :bar: Good work!
      :aug: While aug is a local variable, it is not the first one in the code.
      :item: item is not a local variable.
      :.*: Incorrect, try again.
   -  :aug: Good work!
      :bar: While bar is a local variable, it is not the first one in the code.
      :item: item is not a local variable.
      :.*: Incorrect, try again.