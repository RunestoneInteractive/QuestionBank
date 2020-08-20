.. dragndrop:: chapter_eleven_glossary_three
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-summary
   :topics: 11-regex/11-summary
   :from_source: T
   :feedback: Look above for the definitions of these special characters.
   :match_1: [aeiou]|||Matches a single character as long as that character is in the specified set.
   :match_2: ()|||When these are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
   :match_3: \b|||Matches the empty string, but only at the start or end of a word.
   :match_4: \B|||Matches the empty string, but not at the start or end of a word.
   :match_5: \d|||Matches any decimal digit; equivalent to the set [0-9].
   :match_6: \D|||Matches any non-digit character; equivalent to the set [^0-9].

   Match each character with its regex definition.