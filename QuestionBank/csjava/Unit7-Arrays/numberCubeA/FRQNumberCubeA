.. activecode:: FRQNumberCubeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: numberCubeA
   :topics: Unit7-Arrays/numberCubeA
   :from_source: T
   :language: java

    import java.util.Arrays;
    public class NumberCube
    {

        public int toss()
        {
            return (int)( (Math.random() * 6) + 1 );
        }

        public static int[] getCubeTosses(NumberCube cube, int numTosses)
        {
            // Complete this method
        }

        public static void main(String[] args) {
            NumberCube cube = new NumberCube();
            int numTosses = 9;
            int[] tosses = getCubeTosses(cube, numTosses);

            if(tosses.length < numTosses) {
              System.out.println("It looks like you are not returning an array of the correct size:");
              System.out.println(Arrays.toString(tosses));
            } else {
              System.out.println("You returned an array of the correct size:");
              System.out.println(Arrays.toString(tosses));
            }
        }
    }