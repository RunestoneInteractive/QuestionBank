.. parsonsprob:: SoundB
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/soundB
   :from_source: T
   :numbered: left
   :adaptive:

   The method <code>trimSilenceFromBeginning</code> below contains correct code for one solution to this problem, but it is mixed up.  Drag the code blocks from the left to the right and put them in order with the correct indention so that the code would work correctly.
   -----
   public void trimSilenceFromBeginning()
   {
       int i = 0;
   =====
       while (this.samples[i] == 0)
       {
   =====
           i++;
   =====
       } // end while
   =====
       int samplesLen = this.samples.length;
       int[] newSamples = new int[samplesLen - i];
   =====
       for (int j = 0; j < newSamples.length; j++)
       {
   =====
           newSamples[j] = this.samples[j+i];
   =====
       } // end for
   =====
       this.samples = newSamples;
   =====
   } // end method