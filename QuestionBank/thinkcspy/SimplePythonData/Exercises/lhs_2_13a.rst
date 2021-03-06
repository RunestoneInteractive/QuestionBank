.. activecode:: lhs_2_13a
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.0147601476
    :total_students_attempting: 271
    :num_students_correct: 192.0
    :mean_clicks_to_correct: 14.6145833333

    A convenient algorithm for determining the date of Easter in a given year was devised in 1876 and first appeared in Butcher\'s Ecclesiastical Handbook. This algorithm holds for any year in the Gregorian calendar, which means years including and after 1583. Subject to minor adaptations, the algorithm is as follows:
    
    1. Let ``y`` be the year (such as 1583 or 2003).
    2. Divide ``y`` by ``19`` and call the remainder ``a``. Ignore the quotient.
    3. Divide ``y`` by ``100`` and get a quotient ``b`` and a remainder ``c``.
    4. Divide ``b`` by ``4`` and get a quotient ``d`` and a remainder ``e``.
    5. Divide ``b + 8`` by ``25`` and get a quotient ``f``. Ignore the remainder.
    6. Divide ``b - f + 1`` by ``3`` and get a quotient ``g``. Ignore the remainder.
    7. Divide ``19 * a + b - d - g + 15`` by ``30`` and get a remainder ``h``. Ignore the quotient.
    8. Divide ``c`` by ``4`` and get a quotient ``i`` and a remainder ``k``.
    9. Divide ``32 + 2 * e + 2 * i - h - k`` by ``7`` and get a remainder ``r``. Ignore the quotient.
    10. Divide ``a + 11 * h + 22 * r`` by ``451`` and get a quotient ``m``. Ignore the remainder.
    11. Divide ``h + r - 7 * m + 114`` by ``31`` and get a quotient ``n`` and a remainder ``p``.
    
    The value of ``n`` gives the month (3 for March and 4 for April) and the value of ``p + 1`` gives the day of the month. For example, if ``y`` is 2003:
    
    ::
    
      a = 8
      b = 20
      c = 3
      d = 5
      e = 0
      f = 1
      g = 6
      h = 26
      i = 0
      k = 3
      r = 3
      m = 0
      n = 4
      p = 19
    
    Therefore, in 2003, Easter fell on April 20 (month = n = 4 and day = p + 1 = 20).
    
    Complete the function below to solve for the day that Easter falls on for a given year. The function should display the values for all of the variables and the date for Easter. A Sample run output for the year 2003 would be:
    
    ::
    
      a = 8
      b = 20
      c = 3
      d = 5
      e = 0
      f = 1
      g = 6
      h = 26
      i = 0
      k = 3
      r = 3
      m = 0
      n = 4
      p = 19
      
      Easter in 2003 falls on 4 / 20
    
    ~~~~
    def Easter(year):
        y = year
    
        a = y % 19;
        print("a = ", a);
        b = y // 100;
        print("b = ", b);
    
        # Your code here
    
        return (a, b, c, d, e, f, g, h, i, k, r, m, n, p)
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def easterSoln(self, year):
            y = year
            a = y % 19;
            b = y // 100;
            c = y % 100;
            d = b // 4;
            e = b % 4;
            f = ( b + 8 ) // 25
            g = ( b - f + 1 ) // 3
            h = ( 19 * a + b - d - g + 15 ) % 30
            i = c // 4
            k = c % 4
            r = ( 32 + 2 * e + 2 * i - h - k ) % 7
            m = ( a + 11 * h + 22 * r ) // 451
            n = ( h + r - 7 * m + 114 ) // 31 # [3 = March, 4 = April]
            p = ( h + r - 7 * m + 114 ) % 31
            return (a, b, c, d, e, f, g, h, i, k, r, m, n, p)
        
        def testOne(self):
            year = 2018
            a, b, c, d, e, f, g, h, i, k, r, m, n, p = self.easterSoln(year)
            _a, _b, _c, _d, _e, _f, _g, _h, _i, _k, _r, _m, _n, _p = Easter(year)
            self.assertEqual(a, _a, "Testing that a's value is correct.")
            self.assertEqual(b, _b, "Testing that b's value is correct.")
            self.assertEqual(c, _c, "Testing that c's value is correct.")
            self.assertEqual(d, _d, "Testing that d's value is correct.")
            self.assertEqual(e, _e, "Testing that e's value is correct.")
            self.assertEqual(f, _f, "Testing that f's value is correct.")
            self.assertEqual(g, _g, "Testing that g's value is correct.")
            self.assertEqual(h, _h, "Testing that h's value is correct.")
            self.assertEqual(i, _i, "Testing that i's value is correct.")
            self.assertEqual(k, _k, "Testing that k's value is correct.")
            self.assertEqual(r, _r, "Testing that r's value is correct.")
            self.assertEqual(m, _m, "Testing that m's value is correct.")
            self.assertEqual(n, _n, "Testing that n's value is correct.")
            self.assertEqual(p, _p, "Testing that p's value is correct.")
            _out = "Easter in " + str(year) + " falls on " + str(n) + " / " + str( p + 1 )
    
            outText = self.getOutput()
            outText = " ".join(outText.split())   # get rid of multiple spaces
            self.assertIn(_out, outText, "Testing final output. (Don't worry about Actual and Expected Values.)")
    
            year = 2003
            a, b, c, d, e, f, g, h, i, k, r, m, n, p = self.easterSoln(year)
            _a, _b, _c, _d, _e, _f, _g, _h, _i, _k, _r, _m, _n, _p = Easter(year)
            self.assertEqual(a, _a, "Testing that a's value is correct.")
            self.assertEqual(b, _b, "Testing that b's value is correct.")
            self.assertEqual(c, _c, "Testing that c's value is correct.")
            self.assertEqual(d, _d, "Testing that d's value is correct.")
            self.assertEqual(e, _e, "Testing that e's value is correct.")
            self.assertEqual(f, _f, "Testing that f's value is correct.")
            self.assertEqual(g, _g, "Testing that g's value is correct.")
            self.assertEqual(h, _h, "Testing that h's value is correct.")
            self.assertEqual(i, _i, "Testing that i's value is correct.")
            self.assertEqual(k, _k, "Testing that k's value is correct.")
            self.assertEqual(r, _r, "Testing that r's value is correct.")
            self.assertEqual(m, _m, "Testing that m's value is correct.")
            self.assertEqual(n, _n, "Testing that n's value is correct.")
            self.assertEqual(p, _p, "Testing that p's value is correct.")
         
            outText = self.getOutput()
            outText = " ".join(outText.split())   # get rid of multiple spaces
            self.assertIn('a = ' + str(a), outText, "Testing output for a. (Don't worry about Actual and Expected Values.)")
            self.assertIn('b = ' + str(b), outText, "Testing output for b. (Don't worry about Actual and Expected Values.)")
            self.assertIn('c = ' + str(c), outText, "Testing output for c. (Don't worry about Actual and Expected Values.)")
            self.assertIn('d = ' + str(d), outText, "Testing output for d. (Don't worry about Actual and Expected Values.)")
            self.assertIn('e = ' + str(e), outText, "Testing output for e. (Don't worry about Actual and Expected Values.)")
            self.assertIn('f = ' + str(f), outText, "Testing output for f. (Don't worry about Actual and Expected Values.)")
            self.assertIn('g = ' + str(g), outText, "Testing output for g. (Don't worry about Actual and Expected Values.)")
            self.assertIn('h = ' + str(h), outText, "Testing output for h. (Don't worry about Actual and Expected Values.)")
            self.assertIn('i = ' + str(i), outText, "Testing output for i. (Don't worry about Actual and Expected Values.)")
            self.assertIn('k = ' + str(k), outText, "Testing output for k. (Don't worry about Actual and Expected Values.)")
            self.assertIn('r = ' + str(r), outText, "Testing output for r. (Don't worry about Actual and Expected Values.)")
            self.assertIn('m = ' + str(m), outText, "Testing output for m. (Don't worry about Actual and Expected Values.)")
            self.assertIn('n = ' + str(n), outText, "Testing output for n. (Don't worry about Actual and Expected Values.)")
            self.assertIn('p = ' + str(p), outText, "Testing output for p. (Don't worry about Actual and Expected Values.)")
            _out = "Easter in " + str(year) + " falls on " + str(n) + " / " + str( p + 1 ) 
            self.assertIn(_out, outText, "Testing final output. (Don't worry about Actual and Expected Values.)")
    
    myTests().main()