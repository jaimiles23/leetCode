"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-29 10:07:00
 * @modify date 2019-11-29 10:52:22
 * @desc [
My initial solution to this problem was to use [permutations](https://en.wikipedia.org/wiki/Permutation), however because of the potentially 
(N) number of 'Nones', a simple permutation formula wouldn't work to determine the number of structurally unique BSTs. Additionally, the question
refers to 'structurally unique' BSTs, _not_ value unique. Hence, permutations would not work. 

Ultimately, the problem asks to return the structurally unique BSTs, not determine the number. Thus, this algorithm must bruteforce the
solution. The solutions shown here utilize demonstrations from the following online resources:
1. https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31521/Python-solution-with-detailed-explanation
2. https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

 ]
 */
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Taken from source 1 - leetCode
    """
    def helper(self, start, end):       # Helper function for recursive call
        result = []         # return list
        if start > end: # Base case.
            result.append(None) 
        else:
            for root in range(start, end+1):    # range from start to end.
                left, right = self.helper(start, root-1), self.helper(root+1, end)  # cut values in half, left_side < n/2, right_side > n/2 
                for lt in left:
                    for rt in right:
                        x = TreeNode(root)  # parent tree
                        x.left, x.right = lt, rt    # create branches
                        result.append(x)    # append parent to result
        return result
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)


"""
Taken from source 2: geekforgeeks
"""
# Python3 prgroam to construct all unique 
# BSTs for keys from 1 to n  
  

# Binary Tree Node  
""" A utility function to create a 
new BST node """
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, item):  
        self.key=item 
        self.left = None
        self.right = None
  

# A utility function to do preorder  
# traversal of BST  
def preorder(root) : ## Recursive function to print the order of the roots
  
    if (root != None) : 
      
        print(root.key, end = " " ) 
        preorder(root.left)  
        preorder(root.right)  
      

# function for constructing trees  
def constructTrees(start, end):  
  
    list = []  
  
    """ if start > end then subtree will be  
        empty so returning None in the list """
    if (start > end) : 
      
        list.append(None)  
        return list
      
    """ iterating through all values from  
        start to end for constructing 
        left and right subtree recursively """
    for i in range(start, end + 1):  
      
        """ constructing left subtree """
        leftSubtree = constructTrees(start, i - 1)  
  
        """ constructing right subtree """
        rightSubtree = constructTrees(i + 1, end)  
  
        """ now looping through all left and  
            right subtrees and connecting  
            them to ith root below """
        for j in range(len(leftSubtree)) : 
            left = leftSubtree[j]  
            for k in range(len(rightSubtree)):  
                right = rightSubtree[k]  
                node = newNode(i)   # making value i as root  
                node.left = left    # connect left subtree  
                node.right = right    # connect right subtree  
                list.append(node)    # add this tree to list  
    return list
  
# # Driver Code  
# if __name__ == '__main__': 
  
#     # Construct all possible BSTs  
#     totalTreesFrom1toN = constructTrees(1, 4)  
  
#     """ Printing preorder traversal of  
#         all constructed BSTs """
#     print("Preorder traversals of all",  
#                 "constructed BSTs are")  
#     for i in range(len(totalTreesFrom1toN)):  
#         preorder(totalTreesFrom1toN[i]) 
#         print() 

def j_unique_BST(n: int):
    """
    Personal re-creation of the above code for learning purposes
    """
    def construct_trees(start: int, end: int):
        ## Node structures
        nodes = []

        if start > end:
            nodes.append(None)
            return nodes
        
        ## Iterate all values to create list nodes
        for i in range(start, end + 1):

            left_tree = construct_trees(start, i - 1)
            right_tree = construct_trees(i + 1, end)

            ## connect all possible trees to the root
            for j in range(len(left_tree)):
                left = left_tree[j]

                for k in range(len(right_tree)):
                    right = right_tree[k]
                    node = newNode(i)
                    node.left = left
                    node.right = right
                    nodes.append(node)
        return nodes
    
    start, end = 1, n
    return construct_trees(start, end)


def print_nodes(node: newNode):
    """
    Utility function: prints all values from head tree node
    """
    if node != None:
        print(node.key, end = '')
        print_nodes(node.left)
        print_nodes(node.right)


def test_j_code():
    for i in range(1, 6):
        print(f"\n{'#' * 5} n = {i}")
        nodes = j_unique_BST(i)
        print(len(nodes))
        for i in range(len(nodes)):
            print_nodes(nodes[i])
            print('')


def main():
    test_j_code()


if __name__ == "__main__":
    main()
