.. activecode:: c2l
        :author: jenkins
        :difficulty: 3.0
        :basecourse: msumoorhead
        :chapter: ClassesDiggingDeeper
        :subchapter: HelperFuncs
        :topics: ClassesDiggingDeeper/HelperFuncs
        :from_source: None

        def gcd(m, n):
            while m % n != 0:
                oldm = m
                oldn = n
                m = oldn
                n = oldm % oldn
            return n

        print(gcd(12, 16))