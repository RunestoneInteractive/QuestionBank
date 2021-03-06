.. mchoice:: qvh_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: vHardMC
   :topics: VariableBasics/vHardMC
   :from_source: T
   :answer_a: itemArray = {0, 1, 2, 3} and val = 3;
   :answer_b: itemArray = {0, 1, 2, 3} and val = 5;
   :answer_c: itemArray = {0, 0, 0, 0} and val = 0;
   :answer_d: itemArray = {9, 8, 7, 6} and val = 3;
   :answer_e: itemArray = {9, 8, 7, 6} and val = 5;
   :correct: b
   :feedback_a: This would be true if Java used pass by reference rather than pass by value (it creates copies of the values that are passed).
   :feedback_b: Java passes parameters by copying the value.  With an array it creates a copy of the object reference.  So, <code>mod</code> will change the <code>itemArray</code>, but <code>val</code> won't change since <code>mod</code> only changes the copy of the primitive value.
   :feedback_c: How could this have happened?
   :feedback_d: Java passes parameters by passing the values this means that the contents of <code>itemArray</code> will be changed by the <code>mod</code> method, but <code>val</code> won't change.
   :feedback_e: Java passes parameters by passing the values this means that the contents of <code>itemArray</code> will be changed by the <code>mod</code> method.

   Given the following code are the contents of ``itemArray`` and ``val`` after a call of ``mod(itemArray,val)``?

   .. code-block:: java

    int[] itemArray = {9, 8, 7, 6};
    int val = 5;

    public static void mod(int[] a, int value)
    {
       for (int i=0; i < a.length; i++)
       {
          a[i] = i;
       }
       value = a[a.length-1];
    }