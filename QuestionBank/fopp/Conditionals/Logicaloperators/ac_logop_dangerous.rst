.. activecode:: ac_logop_dangerous
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Logicaloperators
   :topics: Conditionals/Logicaloperators
   :from_source: T

   total_weight = int(input('Enter total weight of luggage:'))
   num_pieces = int(input('Number of pieces of luggage?'))

   if total_weight / num_pieces > 50:
      print('Average weight is greater than 50 pounds -> $100 surcharge.')

   print('Luggage check complete.')