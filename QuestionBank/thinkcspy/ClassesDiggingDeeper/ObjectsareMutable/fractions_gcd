.. activecode:: fractions_gcd
        :author: bmiller
        :difficulty: 3.0
        :basecourse: thinkcspy
        :chapter: ClassesDiggingDeeper
        :subchapter: ObjectsareMutable
        :topics: ClassesDiggingDeeper/ObjectsareMutable
        :from_source: T

        def gcd(m, n):
            while m % n != 0:
                oldm = m
                oldn = n

                m = oldn
                n = oldm % oldn

            return n

        print(gcd(12, 16))