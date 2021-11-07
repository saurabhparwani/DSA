# Problem Statement : https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

class Node(object):
    def __init__(self,freq,symbol,left = None ,right = None):
        self.symbol = symbol
        self.freq = freq
        self.left  = left
        self.right = right
        self.huff = ''    # This is to mention tree direction.



def printHuffmanNodes(node,val):
    newVal = val + str(node.huff)

    # If node is the leaf node then simply print the node else traverse in the left & right side.
    if node.left == None and node.right == None:
        print(node.symbol, newVal)
        return

    if node.left:
        printHuffmanNodes(node.left,newVal)

    if node.right:
        printHuffmanNodes(node.right,newVal)




# TC = O(N*LogN)where n is the number of unique characters.
# If there are n nodes, extractMin() is called 2*(n – 1) times. extractMin() takes O(logn) time as it calles minHeapify(). So, overall complexity is O(nlogn).
# SC = O(N) For storing the nodes.
def buildHuffmanTree(chars,frequency):

    nodes = []   # List to store all the huffman nodes in the list.

    for i in range(len(chars)):
        nodes.append(Node(frequency[i],chars[i]))

    # Now Traverse the nodes list and make subtrees of two minimum nodes.
    while len(nodes) > 1:

        nodes = sorted(nodes,key= lambda x:x.freq)

        # Get left & right nodes and smallest & second smallest element.
        left = nodes[0]
        right = nodes[1]

        # Set the direction for the left & right nodes.
        left.huff = 0
        right.huff = 1

        # Create new Node with the new data and frequecnt.
        newNode = Node(left.freq + right.freq,left.symbol+right.symbol,left,right)

        # Now remove both popped nodes and append the newly create node in the node list.
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)


    # At this point only 1 node will be available in the nodes list . Now traverse this Node & print nodes.
    printHuffmanNodes(nodes[0],'')


# Driver Code
chars = 'qwertyuiopasdfghjklzxcvbn'
frequency = [8 ,9 ,14, 19, 20, 21, 21, 25, 33 ,45 ,50, 50 ,66 ,68 ,70, 73 ,74, 75 ,76, 82, 85, 90, 94 ,97 ,100]
buildHuffmanTree(chars,frequency)

# Expected Output :
#0000 0001 00100 001010 001011 0011 0100 0101 0110 0111 1000 100100 100101 10011 1010 1011 1100 11010 11011 1110 111100 1111010 11110110 11110111 11111

