.. parsonsprob:: SoundA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: soundA
   :topics: ArrayBasics/soundA
   :from_source: T
   :numbered: left
   :adaptive:

   The method <code>limitAmplitude</code> below contains the correct code for a solution to this problem, but the code blocks are mixed up.  Drag the blocks from the left to the right and put them in order with the correct indentation so that the code would work correctly.
   -----
   public int limitAmplitude(int limit)
   {
   =====
       int numChanged = 0;
       for (int i = 0; i < samples.length; i++)
       {
   =====
           if (samples[i] > limit)
           {
   =====
               samples[i] = limit;
               numChanged++;
   =====
           } // end first if
           if (samples[i] < -limit)
           {
   =====
               samples[i] = -limit;
               numChanged++;
   =====
           } // end second if
   =====
       } // end for
   =====
       return numChanged;
   =====
   } // end method