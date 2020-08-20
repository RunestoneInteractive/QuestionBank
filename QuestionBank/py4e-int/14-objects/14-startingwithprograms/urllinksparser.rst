.. activecode:: urllinksparser
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-startingwithprograms
   :topics: 14-objects/14-startingwithprograms
   :from_source: T
   :language: python3

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

   # Retrieve all of the anchor tags
   tags = soup('a')
   for tag in tags:
       print(tag.get('href', None))