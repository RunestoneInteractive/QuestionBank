.. activecode:: chp08_fun5
        :author: bmiller
        :difficulty: 3.0
        :basecourse: thinkcspy
        :chapter: Strings
        :subchapter: Optionalparameters
        :topics: Strings/Optionalparameters
        :from_source: T

        def find3(astring, achar, start=0):
            """
            Find and return the index of achar in astring.
            Return -1 if achar does not occur in astring.
            """
            ix = start
            found = False
            while ix < len(astring) and not found:
                if astring[ix] == achar:
                    found = True
                else:
                    ix = ix + 1
            if found:
                return ix
            else:
                return -1

        print(find3('banana', 'a', 2))