.. codelens:: keyword_params_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: KeywordParameters
   :topics: AdvancedFunctions/KeywordParameters
   :from_source: T
   :python: py3

   def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
       print("-- This parrot wouldn't" + action,)
       print("if you put" + str(voltage) + "volts through it.")
       print("-- Lovely plumage, the" +  type)
       print("-- It's " + state + "!")

   parrot(1000)                                          # 1 positional argument
   parrot(voltage=1000)                                  # 1 keyword argument
   parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
   parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
   parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
   parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword