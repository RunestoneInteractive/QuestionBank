.. actex:: assess_ac23_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: Exercises
   :topics: Exceptions/Exercises
   :from_source: T
   :practice: T
   :autograde: unittest

   Below, we have provided buggy code. Add a try/except clause so the code runs without errors. If a blog post didn't get any likes, a 'Likes' key should be added to that dictionary with a value of 0.

   ~~~~

   blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

   total_likes = 0

   for post in blog_posts:
       total_likes = total_likes + post['Likes']

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testA(self):
           self.assertEqual(total_likes, 86, "Testing that total_likes has the correct value.")
       def testB(self):
            accum = 0
            for d in blog_posts:
                if 'Likes' in d:
                    accum +=1
            self.assertEqual(accum, 6, "Testing that blog_post dictionaries all have a 'Likes' key.")

   myTests().main()