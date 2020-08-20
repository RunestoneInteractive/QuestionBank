.. activecode:: cgi1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: webfundamentals
   :chapter: CGI
   :subchapter: basiccgi
   :topics: CGI/basiccgi
   :from_source: T
   :language: python

   #!/usr/bin/python

   print("Content-type: text/html\n")
   print("<html>")
   print("<body>")
   print("<h1>Hello %s</h1>" % "World")
   print("</body>")
   print("</html>")