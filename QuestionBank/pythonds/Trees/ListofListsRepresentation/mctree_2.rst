.. actex:: mctree_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds
   :chapter: Trees
   :subchapter: ListofListsRepresentation
   :topics: Trees/ListofListsRepresentation
   :from_source: T

   Write a function ``buildTree`` that returns a tree using the list of lists functions that looks like this:

   .. image:: Figures/tree_ex.png
   ~~~~
   from test import testEqual

   def buildTree():
       pass

   ttree = buildTree()
   testEqual(getRootVal(getRightChild(ttree)),'c')
   testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
   testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')