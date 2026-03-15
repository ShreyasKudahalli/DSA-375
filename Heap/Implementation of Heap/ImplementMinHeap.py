class minHeap:

    def __init__(self):
        self.heap = []

    # Insert element
    def push(self, x: int):

        def heapify_up(i):
            while i > 0:
                p = (i - 1) // 2
                if self.heap[p] > self.heap[i]:
                    self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                    i = p
                else:
                    break

        self.heap.append(x)
        heapify_up(len(self.heap) - 1)

    # Remove max element
    def pop(self):

        if not self.heap:
            return None

        min_val = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return min_val

        def heapify_down(index):
            size = len(self.heap)

            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest = index

                if left < size and self.heap[left] < self.heap[smallest]:
                    smallest = left

                if right < size and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == index:
                    break

                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest

        self.heap[0] = self.heap[-1]
        self.heap.pop()
        heapify_down(0)

        return min_val

    # Return max element
    def peek(self) -> int:
        return self.heap[0] if self.heap else -1

    # Return heap size
    def size(self) -> int:
        return len(self.heap)