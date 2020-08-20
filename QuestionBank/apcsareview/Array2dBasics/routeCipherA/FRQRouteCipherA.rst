.. activecode:: FRQRouteCipherA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Array2dBasics
   :subchapter: routeCipherA
   :topics: Array2dBasics/routeCipherA
   :from_source: T
   :language: java

   public class RouteCipher
   {
     /** A two-dimensional array of single-character strings, instantiated in the constructor */
     public String[][] letterBlock;

     /** The number of rows of letterBlock, set by the constructor */
     private int numRows;

     /** The number of columns of letterBlock, set by the constructor */
     private int numCols;

     public RouteCipher(int r, int c){
      this.letterBlock = new String[r][c];
      this.numRows = r;
      this.numCols = c;
     }

     /** Places a string into letterBlock in row-major order.
     *   @param str the string to be processed
     *   Postcondition:
     *     if str.length() < numRows * numCols, "A" in each unfilled cell
     *     if str.length() > numRows * numCols, trailing characters are ignored
     */
     public void fillBlock(String str){
      // Complete this method
     }

     /** Extracts encrypted string from letterBlock in column-major order.
     *   Precondition: letterBlock has been filled
     *   @return the encrypted string from letterBlock
     */
     private String encryptBlock()
     { return ""; }

     /** Encrypts a message.
     *   @param message the string to be encrypted
     *   @return the encrypted message;
     *           if message is the empty string, returns the empty string
     */
     public String encryptMessage(String message)
     { return ""; }

     public static void main(String[] args){

      boolean test1 = false;
      RouteCipher ciph = new RouteCipher(3, 3);

      ciph.fillBlock("There's 1");

      if((ciph.letterBlock[0][2]).equals("e") && (ciph.letterBlock[2][1]).equals(" "))
        test1 = true;
      else
        System.out.println("Oops! Looks like your code doesn't properly insert the given String.\n");

      if(test1)
        System.out.println("Looks like your code works well!");
      else
        System.out.println("Make a few changes, please.");

     }
   }