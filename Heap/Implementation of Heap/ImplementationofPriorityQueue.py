#User function Template for python3

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].


class Solution:
    def extractMax(self):
        global H, s
        
        # If heap is empty
        if s < 0:
            return -1
        
        # Store the maximum value
        result = H[0]
        
        # Replace root with last element
        H[0] = H[s]
        
        # Decrease heap size
        s -= 1
        
        # Restore heap property
        if s >= 0:
            shiftDown(0)
        
        return result