.. mchoice:: qssm_6
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/ssHardMC
   :from_source: T
   :practice: T
   :answer_a: Anna John Billy Bob Roger Dominic
   :answer_b: John Dominic Anna Roger Bob Billy
   :answer_c: Billy Bob Roger Anna Dominic John
   :answer_d: Anna John Billy Bob Roger
   :correct: b
   :feedback_a: This would be true if the program did not modify the names array at all.
   :feedback_b: This is the correct answer. The program is ordering the grades array from greatest to least as well as keeping the names with the grades.
   :feedback_c: This would be true if the program sorted the grades array from the smallest value to the largest value.
   :feedback_d: This would be true if the program did not modify the names array and if the for loop at the end of the program did not output all the values of the array.

   What is printed when the following main method is executed?

   .. code-block:: java

                public class GradeSort
                {
                   public static void main(String[] args)
                   {
                        String[] names = {"Anna","John","Billy","Bob","Roger","Dominic"};
                        int[] grades = {93,100,67,84,86, 93};
                        int i, j, first, temp;
                        String temp2;
                        for (i = grades.length - 1; i > 0; i--)
                        {
                            first = 0;
                            for (j = 1; j <= i; j++)
                            {
                                if (grades[j] < grades[first])
                                    first = j;
                            }
                            temp = grades[first];
                            grades[first] = grades[i];
                            grades[i] = temp;
                            temp2 = names[first];
                            names[first] = names[i];
                            names[i] = temp2;
                        }
                        for (int t = 0; t < names.length; t++)
                        {
                            System.out.print((names[t]) + " ");
                        }
                   }
                }