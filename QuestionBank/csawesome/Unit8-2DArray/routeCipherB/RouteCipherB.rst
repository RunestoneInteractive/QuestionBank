.. parsonsprob:: RouteCipherB
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit8-2DArray
  :subchapter: routeCipherB
  :topics: Unit8-2DArray/routeCipherB
  :from_source: T
  :numbered: left
  :adaptive: 
  :pct_on_first: 0.0563380282
  :total_students_attempting: 426
  :num_students_correct: 336.0
  :mean_clicks_to_correct: 7.0863095238

  The method encryptMessage below contains the correct code for one solution to this problem, but it is mixed up and contains extra blocks that are not needed.  Drag the needed code from the left to the right and put them in order with the correct indention so that the code would work correctly.
  -----
  public String encryptMessage(String message) {
    String encryptedMessage = "";
    int chunkSize = this.numRows * this.numCols;
  =====
    while (message.length() > 0) {
  =====
      if (chunkSize > message.length()) {
  =====
        chunkSize = message.length();
  =====
      } // end if
  =====
      fillBlock(message);
      encryptedMessage += encryptBlock();
      message = message.substring(chunkSize);
  =====
    } // end while
  =====
    return encryptedMessage;
  =====
  } // end method