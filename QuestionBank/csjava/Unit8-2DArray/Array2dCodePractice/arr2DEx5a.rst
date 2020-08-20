.. activecode::  arr2DEx5a
    :author: bmiller
    :difficulty: 3
    :basecourse: csjava
    :topics: Unit8-2DArray/Array2dCodePractice
    :from_source: T
    :language: java

    public class Test1 {
        public static void main(String[] args)
        {
            String[][] arr = { {"hello","there","world"},
                              {"how","are","you"} };

            System.out.println("Rows:" + arr.length);
            System.out.println();
            System.out.println("Columns:" + arr[0].length);
        }
    }