.. parsonsprob:: cndtnl-mixed-price
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 03-conditional
   :subchapter: 03-MixedupCode
   :topics: 03-conditional/03-MixedupCode
   :from_source: T
   :practice: T
   :adaptive:
   :numbered: left

   The following program should calculate the total price, but the lines are mixed up. The price is
   based on the weight. Items that weigh less than 2 pounds should cost 1.5. Items that weigh more
   than 2 pounds should cost 1.3. Be sure to indent correctly!
   -----
   weight = 0.5
   numItems = 5
   if weight < 2:
   =====
       price = 1.50
   =====
   if weight >= 2:
   =====
       price = 1.30
   =====
   total = weight * price
   =====
   print(weight)
   print(price)
   print(total)