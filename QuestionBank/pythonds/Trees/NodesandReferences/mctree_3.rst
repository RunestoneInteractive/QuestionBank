.. actex:: mctree_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: Trees
   :subchapter: NodesandReferences
   :topics: Trees/NodesandReferences
   :from_source: T

   Write a function ``buildTree`` that returns a tree using the nodes and references implementation that looks like this:

   .. image:: Figures/tree_ex.png
   ~~~~
   from test import testEqual

   def buildTree():
       pass

   ttree = buildTree()

   testEqual(ttree.getRightChild().getRootVal(),'c')
   testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
   testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')