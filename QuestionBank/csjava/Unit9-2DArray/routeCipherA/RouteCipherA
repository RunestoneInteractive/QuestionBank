.. parsonsprob:: RouteCipherA
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit9-2DArray
  :subchapter: routeCipherA
  :topics: Unit9-2DArray/routeCipherA
  :from_source: T
  :numbered: left
  :adaptive:

  The method fillBlock below contains the correct code for one solution to this problem, but it is mixed up and contains extra blocks that are not needed.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
  -----
  private void fillBlock(String str) {
    int pos = 0;
  =====
    for (int r = 0; r < this.numRows; r++ ) {
  =====
        for (int c = 0; c < this.numCols; c++ ) {
  =====
            if (pos < str.length()) {
  =====
                String subStr = str.substring(pos, pos+1);
                this.letterBlock[r][c] = subStr;
                pos++;
  =====
            } else {
                this.letterBlock[r][c] = "A";
            } // end else block
  =====
        } // end inner for
  =====
    } // end outer for
  =====
  } // end method