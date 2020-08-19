.. activecode:: writtencode_question9_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :available_files: mbox-short.txt

   with open("mbox-short.txt3", "r") as filename:
       message_count = {}
       messages = filename.readlines()
       for message in messages:
           key = message.split()[0]
           value = message.split()[1]
           if key not in message_count.keys():
               message_count[key] = value

   max_emails = 0
   for key in message_count.keys():
       if int(message_count[key]) >= max_emails:
           max_emails = int(message_count[key])
   print(max_emails)