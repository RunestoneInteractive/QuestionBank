.. actex:: mctree_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Trees
   :subchapter: NodesandReferences
   :topics: Trees/NodesandReferences
   :from_source: T

   Write a function ``build_tree`` that returns a tree using the nodes and references implementation that looks like this:

   .. image:: Figures/tree_ex.png
   ~~~~
   from test import testEqual

   def build_tree():
       pass

   ttree = build_tree()

   testEqual(ttree.get_right_child().get_root_val(), "c")
   testEqual(ttree.get_left_child().get_right_child().get_root_val(), "d")
   testEqual(ttree.get_right_child().get_left_child().get_root_val(), "e")