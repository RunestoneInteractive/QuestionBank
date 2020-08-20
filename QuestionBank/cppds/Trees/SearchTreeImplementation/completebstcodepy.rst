.. activecode:: completebstcodepy
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Trees
    :subchapter: SearchTreeImplementation
    :topics: Trees/SearchTreeImplementation
    :from_source: T
    :optional:

    #The TreeNode class represents a node, or vertex, in a tree heirarchy.
    class TreeNode:
        def __init__(self,key,val,left=None,right=None,parent=None):
            self.key = key
            self.payload = val
            self.leftChild = left
            self.rightChild = right
            self.parent = parent

        """ Returns a pointer to the left child of this node.
         If null, the child doesn't exist."""
        def hasLeftChild(self):
            return self.leftChild

        """ Returns the right child, or None if it doesn't exist."""
        def hasRightChild(self):
            return self.rightChild

        # Returns a boolean indicating if this node is the left child of its parent.
        def isLeftChild(self):
            return self.parent and self.parent.leftChild == self

        # Returns a boolean indicating if this node is the right child of its parent.
        def isRightChild(self):
            return self.parent and self.parent.rightChild == self

        # Returns a boolean indicating if this node is a root node (has no parents).
        def isRoot(self):
            return not self.parent

        # Returns a boolean indicating if this node has no children.
        def isLeaf(self):
            return not (self.rightChild or self.leftChild)

        # Returns a boolean indicating if this node has children.
        def hasAnyChildren(self):
            return self.rightChild or self.leftChild

        # Returns a boolean indicating if this node has both childeren.
        def hasBothChildren(self):
            return self.rightChild and self.leftChild

        """ Removes this node from the tree it exists in,
        making it the root node of its own tree."""
        def spliceOut(self):
            if self.isLeaf():
                if self.isLeftChild():
                    self.parent.leftChild = None
                else:
                    self.parent.rightChild = None
            elif self.hasAnyChildren():
                if self.hasLeftChild():
                    if self.isLeftChild():
                        self.parent.leftChild = self.leftChild
                    else:
                        self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
                else:
                    if self.isLeftChild():
                        self.parent.leftChild = self.rightChild
                    else:
                        self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

        """ Uses same properties of binary search tree
            that cause an inorder traversal to find
            nodes in the tree from smallest to largest. """
        def findSuccessor(self):
            succ = None
            if self.hasRightChild():
                succ = self.rightChild.findMin()
            else:
                if self.parent:
                       if self.isLeftChild():
                           succ = self.parent
                       else:
                           self.parent.rightChild = None
                           succ = self.parent.findSuccessor()
                           self.parent.rightChild = self
            return succ

        #Finds the leftmost node out of all of this node's children.
        def findMin(self):
            current = self
            while current.hasLeftChild():
                current = current.leftChild
            return current

        # Sets the variables of this node. lc/rc are left child and right child.
        def replaceNodeData(self,key,value,lc,rc):
            self.key = key
            self.payload = value
            self.leftChild = lc
            self.rightChild = rc
            if self.hasLeftChild():
                self.leftChild.parent = self
            if self.hasRightChild():
                self.rightChild.parent = self


    class BinarySearchTree:

        # references the TreeNode
        # that is the root of the binary search tree.
        def __init__(self):
            self.root = None
            self.size = 0

        def length(self):
            return self.size

        def __len__(self):
            return self.size

        """Checks to see if the tree has a root,
        if there is not a root then it will create a new TreeNode
        and install it as the root of the tree.
        If a root node is already in place than it calls _put
        to search the tree"""
        def put(self,key,val):
            if self.root:
                self._put(key,val,self.root)
            else:
                self.root = TreeNode(key,val)
            self.size = self.size + 1

        """searches the binary tree comparing the new key to the key in the current node. If the new key is less than the current node, search the left subtree. If the new key is greater than the current node, search the right subtree.*\
           When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.*\
           To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step.*\
           this is all done recursively"""
        def _put(self,key,val,currentNode):
            if key < currentNode.key:
                if currentNode.hasLeftChild():
                       self._put(key,val,currentNode.leftChild)
                else:
                       currentNode.leftChild = TreeNode(key,val,parent=currentNode)
            else:
                if currentNode.hasRightChild():
                       self._put(key,val,currentNode.rightChild)
                else:
                       currentNode.rightChild = TreeNode(key,val,parent=currentNode)

        # prints string associated with key to console
        def get(self,key):
           if self.root:
               res = self._get(key,self.root)
               if res:
                      return res.payload
               else:
                      return None
           else:
               return None

        # Uses the same search method as _put, and returns
        # a TreeNode to get
        def _get(self,key,currentNode):
           if not currentNode:
               return None
           elif currentNode.key == key:
               return currentNode
           elif key < currentNode.key:
               return self._get(key,currentNode.leftChild)
           else:
               return self._get(key,currentNode.rightChild)

        #def __contains__(self,key):
         #  if self._get(key,self.root):
          #    return True
           #else:
            #   return False

        """ Checks to make sure the key of the root matches the key that is to be deleted.
            In either case if the key is not found an error is raised.
            If the node is found and has no childeren it is deleted
            If the node has a single child, the child takes the place of the parent.
            Look at explination for listing 10 """
        def delete(self,key):
          if self.size > 1:
             nodeToRemove = self._get(key,self.root)
             if nodeToRemove:
                 self.remove(nodeToRemove)
                 self.size = self.size-1
             else:
                 raise KeyError('Error, key not in tree')
          elif self.size == 1 and self.root.key == key:
             self.root = None
             self.size = self.size - 1
          else:
             raise KeyError('Error, key not in tree')

        # Removes the specified currentNode from this tree.
        def remove(self,currentNode):
             if currentNode.isLeaf(): #leaf
               if currentNode == currentNode.parent.leftChild:
                   currentNode.parent.leftChild = None
               else:
                   currentNode.parent.rightChild = None
             elif currentNode.hasBothChildren(): #interior
               succ = currentNode.findSuccessor()
               succ.spliceOut()
               currentNode.key = succ.key
               currentNode.payload = succ.payload

             else: # this node has one child
               if currentNode.hasLeftChild():
                 if currentNode.isLeftChild():
                     currentNode.leftChild.parent = currentNode.parent
                     currentNode.parent.leftChild = currentNode.leftChild
                 elif currentNode.isRightChild():
                     currentNode.leftChild.parent = currentNode.parent
                     currentNode.parent.rightChild = currentNode.leftChild
                 else:
                     currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)
               else:
                 if currentNode.isLeftChild():
                     currentNode.rightChild.parent = currentNode.parent
                     currentNode.parent.leftChild = currentNode.rightChild
                 elif currentNode.isRightChild():
                     currentNode.rightChild.parent = currentNode.parent
                     currentNode.parent.rightChild = currentNode.rightChild
                 else:
                     currentNode.replaceNodeData(currentNode.rightChild.key,
                                        currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild,
                                        currentNode.rightChild.rightChild)


    def main():

        mytree = BinarySearchTree()
        mytree.put(3, "red")
        mytree.put(4, "blue")
        mytree.put(6, "yellow")
        mytree.put(2, "at")

        print(mytree.get(6))
        print(mytree.get(2))

    main()