.. parsonsprob:: ch12p2ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rMixedUpCodePractice
   :topics: Recursion/rMixedUpCodePractice
   :from_source: T
   :adaptive:
   :noindent:

   The following method should recursively replace all the spaces in the String str with dashes.
   -----
   public String spaceDash(String str)
   {
   =====
       if(str.length == 0)
   =====
           return str;
   =====
       else if(str.charAt(0) ==  ' ')
   =====
           return "-" + spaceDash(str.substring(1));
   =====
       else
   =====
           return str.charAt(0) + spaceDash(str.substring(1));
   =====
   }
   =====
        return "-" + str.substring(1); #distractor