.. activecode::  arr2DEx5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit8-2DArray
    :subchapter: Array2dCodePractice
    :topics: Unit8-2DArray/Array2dCodePractice
    :from_source: T
    :language: java
    :optional:

    public class Test1 {
        public static void main(String[] args)
        {
            String[][] arr = { {"hello","there","world"},
                              {"how","are","you"} };

            System.out.print("Rows:");
            System.out.println(arr.length);

            System.out.print("Columns:");
            System.out.println(arr[0].length);
        }
    }