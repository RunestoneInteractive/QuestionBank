.. activecode:: parallelArrayLists
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-4-arraylist-algorithms
   :topics: Unit8-ArrayList/topic-8-4-arraylist-algorithms
   :from_source: T
   :language: java

   Demonstration of parallel ArrayLists.
   ~~~~
   import java.util.*;

    public class ParallelTests
    {
        public static void main(String[] args)
        {
            ArrayList<Integer> test1Grades = new ArrayList<Integer>();
            ArrayList<Integer> test2Grades = new ArrayList<Integer>();
            test1Grades.add(100);
            test2Grades.add(100);
            test1Grades.add(80);
            test2Grades.add(70);
            test1Grades.add(70);
            test2Grades.add(90);
            double total = 0;
            for (int i = 0; i < test1Grades.size(); i++)
            {
                total +=  test1Grades.get(i) + test2Grades.get(i);
            }
            int numberOfGrades = test1Grades.size() * 2;
            System.out.println("Average over two tests: " + total/numberOfGrades);
        }
    }