#include <iostream>

class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 

#in_order function. Runs iteratively instead of recursively
def in_order(tree):
    prev_loc = []
    treePointer = tree
    while True: #While loop. Don't know how many times we need to loop
        while treePointer != None: #Runs as long as treePointer isnt None
            prev_loc.append(treePointer) #Append pointer to stack
            treePointer = treePointer.left #Move pointer to left
        if len(prev_loc) == 0: #Program exit, stack empty (base case)
            return
        treePointer = prev_loc.pop() #Return last item in stack
        print(treePointer.value) #Print current value
        while treePointer.right is None and len(prev_loc) != 0: #Nested while loop, if right is None
            treePointer = prev_loc.pop() #Return last item in list
            print(treePointer.value) #Print current value
        treePointer = treePointer.right #Change pointer to right branch
        
        
            
        
            
        
        
            
#Allows program to run, with pre-defined nodes for testing
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
