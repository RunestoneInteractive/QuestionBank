.. mchoice:: qab_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aForEach
   :topics: ArrayBasics/aForEach
   :from_source: T
   :answer_a: Whenever the first element in <i>a</i> is equal to <i>val</i>.
   :answer_b: Whenever <i>a</i> contains any element which equals <i>val</i>.
   :answer_c: Whenever the last element in <i>a</i> is equal to <i>val</i>.
   :answer_d: Whenever only 1 element in <i>a</i> is equal to <i>val</i>.
   :correct: c
   :feedback_a: This would be true if the loop started at the end of the array and moved toward the beginning.  But, it will loop from the first element to the last.
   :feedback_b: This would be true if temp was only set to the result of checking if the current element in the array is equal to <i>val</i> when it is <i>false</i>.  But, it is reset each time through the loop.
   :feedback_c: The variable <i>temp</i> is assigned to the result of checking if the current element in the array is equal to <i>val</i>.  The last time through the loop it will check if the last element is equal to <i>val</i>.
   :feedback_d: There is no count of the number of times the array element is equal to <i>val</i>.


   Given that ``a`` is an array of integers and ``val`` is an integer value, which of the following best describes the conditions under which the following code segment will return true?

   .. code-block:: java

     boolean temp = false;
     for ( int i = 0; i < a.length; i++)
     {
       temp = ( a[i] == val );
     }
     return temp;