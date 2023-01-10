# https://leetcode.com/problems/all-elements-in-two-binary-search-trees
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorderTraversal(root):
            stack = []
            inorder = []
            node = root
            while (True):
                if node != None:
                    stack.append(node)
                    node = node.left
                
                else:
                    if (len(stack) == 0):
                        break
                    node = stack[-1]  # top
                    stack.pop()
                    inorder.append(node.val)
                    node = node.right
            return inorder
        
        arr1 = inorderTraversal(root1)
        arr2 = inorderTraversal(root2)
        arr = arr1 + arr2
        arr.sort()
        return arr

class Solution2:
    def getAllElements(self, root1, root2):
        def inorder(root, lst):
            if not root: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
        
        lst1, lst2 = [], []
        inorder(root1, lst1)
        inorder(root2, lst2)
        
        i1, i2, res = 0, 0, []
        s1, s2 = len(lst1), len(lst2)
        
        while i1 < s1 and i2 < s2:
            if lst1[i1] < lst2[i2]:
                res += [lst1[i1]]
                i1 += 1
            else:
                res += [lst2[i2]]
                i2 += 1
                
        return res + lst1[i1:] + lst2[i2:]