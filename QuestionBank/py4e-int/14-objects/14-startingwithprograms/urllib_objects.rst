.. mchoice:: urllib_objects
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-startingwithprograms
   :topics: 14-objects/14-startingwithprograms
   :from_source: T
   :practice: T
   :answer_a: BeautifulSoup creates and returns an object to soup
   :answer_b: The following program is sequential and not object oriented.
   :answer_c: The following program is an example of procedural programming.
   :answer_d: The program will give a 'NameError' as function BeautifulSoup
              is called before its defined.
   :correct: a
   :feedback_a: BeautifulSoup makes use of the object 'html.parser'
                and returns an object.
   :feedback_b: The program may look sequential but it also calls on other classes to return
                objects.
   :feedback_c: The program inherits functions from other classes with the import statements instead
                of using procedures.
   :feedback_d: BeautifulSoup is imported to the program.

   Which of the following is true about the following code?

   ::

     import urllib.request, urllib.parse, urllib.error
     from bs4 import BeautifulSoup
     import ssl

     # Ignore SSL certificate errors
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE

     url = input('Enter - ')
     html = urllib.request.urlopen(url, context=ctx).read()
     soup = BeautifulSoup(html, 'html.parser')
     print(soup('a'))