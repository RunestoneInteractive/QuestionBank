.. activecode:: IT105_AY182_GradedLab02_01
   :author: Tom Babbitt
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :language: python
   :nocodelens: 
   :pct_on_first: 0.023255814
   :total_students_attempting: 43
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 9.25

   Write a function ``DNSLookup(domainName)`` that will take a domain name and ``return``
   the ip address as a string. Assume the domain name is formatted as ``xxxxxx.com``. For
   example, ``google.com``. 
   
   For a given domain name, if there is not an entry in the local DNS 
   server cache, the function will return ``Not in local DNS cache``.
   
   Example: 
   
   ::     
      
      ### Internet Explorer is looking for the IP address of usma.edu followed by cnn.com.
      print(DNSLookup('usma.edu'))
      print(DNSLookup('cnn.com'))
       
      
   
   Results:
   
   ::
   
      143.69.2.10
      Not in local DNS cache
   
   
   ~~~~
   ### Name:
   
   ### Use the shell provided. Do not modify the code given.
   
   def DNSLookup(domainName):
      ### DNSEntries is the list of cached entries currently on the local DNS server. 
      DNSEntries = [['usma.edu','143.69.2.10'],['google.com','172.217.7.14'],['delta.com','216.87.148.114'],['travelalaska.com','38.119.165.230'],['nps.gov','23.36.91.207']]
      
      ###write your code here.
   
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
      	 print('Auto-testing...')
         self.assertEqual(DNSLookup("usma.edu"),'143.69.2.10',"Ensure all entries are checked")
         self.assertEqual(DNSLookup("google.com"),'172.217.7.14',"Ensure all entries are checked")
         self.assertEqual(DNSLookup("delta.com"),'216.87.148.114',"Ensure all entries are checked")
         self.assertEqual(DNSLookup("travelalaska.com"),'38.119.165.230',"Ensure all entries are checked")
         self.assertEqual(DNSLookup("nps.gov"),'23.36.91.207',"Ensure all entries are checked")
         self.assertEqual(DNSLookup("cnn.gov"),'Not in local DNS cache',"Ensure you return the proper response when the entry is not in the DNS Cache")
         editText = self.getEditorText()
         Found = len(re.findall("for .* in",editText)) >=1
         if Found:
         	self.assertEqual(Found, True, "for loop used to check DNS entries.")
         else:
         	self.assertEqual(Found, True, "for loop not used; You must search DNS entries and not hard code all possibilities.")
   
   myTests().main()