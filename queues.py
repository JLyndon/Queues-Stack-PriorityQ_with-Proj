from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# ------------------DEQUEUE II-------------------
    # def __init__(self, *elements):
    #     self._elements = deque(elements)

    # def __len__(self):
    #     return len(self._elements)

    # def __iter__(self):
    #     while len(self) > 0:
    #         yield self.dequeue()

    # def enqueue(self, element):
    #     self._elements.append(element)

    # def dequeue(self):
    #     return self._elements.popleft()
    
# ------------------STACK I-------------------

# class Stack(Queue):
#     def dequeue(self):
#         return self._elements.pop()