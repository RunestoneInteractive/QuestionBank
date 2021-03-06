.. activecode:: lhs_6_9
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0970873786
    :total_students_attempting: 412
    :num_students_correct: 365.0
    :mean_clicks_to_correct: 25.1095890411

    Write a function that writes a tree made of stars (``"*"``) on the display. The height of the tree (the size excluding the base) is input by the user. The base of the tree is created by a separate function which you will also write.
    The tree trunk should always have a width of 3  and a height of 3 regardless of the height of the tree.
    
    ::
    
            Enter the height of the tree: 8
    
                   *
                  ***
                 *****
                *******
               *********             <-- Note, no spaces after the asterisks...
              ***********
             *************
            ***************
                  ***
                  ***
                  ***
    
    **NOTE**: this assignment requires printing without the addition of a newline after each print call. To print without newline you will need to use the ``end`` parameter of the ``print()`` function. For example, to print and ``*`` and remain on the same line your would use a print statement of the form ``print("*", end='')``.
    
    **DEBUGGING HINT**: Spaces are invisible, so use "." to make spaces visible while debugging.
    
    ~~~~
    # My Name:
    
    def tree(n):
        # write your code here
    
    def trunk(n):
        # write your code here
    
    def drawTree(base):
        tree(base)
        trunk(base)
    
    def main():
        h = int(input("Enter the height of the tree:"))
        drawTree( h )
    
    if __name__ == "__main__":
        main()
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
     
        def testOne(self):
            print("\nAuto-testing...\n")
            tSize = 5
            oLen = len(self.getOutput())
            tree( tSize )
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #remove original output from buffer
            self.assertEqual( outText, "    *\n   ***\n  *****\n *******\n*********\n", "Testing top of tree.")
    
            oLen = len(self.getOutput())
            trunk( tSize )
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #remove original output from buffer
            self.assertEqual( outText, "   ***\n   ***\n   ***\n", "Testing trunk")
    
    myTests().main()