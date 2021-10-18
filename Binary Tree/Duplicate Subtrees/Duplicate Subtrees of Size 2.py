# Problem Statement : https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(2)
    root.right.right.left = Node(4)
    root.right.right.right = Node(5)

    return root
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # return root


def inorder(root,h,answer):

    if root is None:
        return ''

    leftstr = inorder(root.left,h,answer)

    stri = leftstr + str(root.data)
    rightStr = inorder(root.right,h,answer)
    stri = stri + rightStr

    if  len(stri)>1:
        if stri not in h:
            h[stri] = 1
        else:
            h[stri] = h[stri]  + 1
            answer[0] = 1


    return stri


def findSubtree(root):
    h = {}
    answer = [0]
    inorder(root,h,answer)
    print(h)
    return answer[0]




# Driver Code
root  = buildTree()
print(findSubtree(root))
