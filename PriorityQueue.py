# Priority Queue implementation

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go    
    
    def size(self):
        return self.next_index
    
    def insert(self, data):
        """
        Insert `data` into the heap
        """
        if self.next_index >= len(self.cbt):
            self.increase_size()
        self.cbt[self.next_index] = data
        current_index = self.next_index
        self.next_index += 1
        
        while self.cbt[current_index] is not None:
            parent = (current_index - 1)//2
            if parent >= 0 and self.cbt[parent] is not None:
                if self.cbt[parent] > self.cbt[current_index]:
                    temp = self.cbt[parent]
                    self.cbt[parent] = self.cbt[current_index]
                    self.cbt[current_index] = temp
                else:
                    current_index = parent
            else:
                return
            
    def increase_size(self):
        old_cbt = self.cbt
        self.cbt = [None for _ in range(2*len(old_cbt))]
        self.next_index = 0
        for i in old_cbt:
            self.cbt[self.next_index] = i
            self.next_index += 1
    
    def remove(self):
        """
        Remove and return the element at the top of the heap
        """
        temp = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index - 1]
        self.cbt[self.next_index - 1] = temp
        popped = self.cbt.pop(self.next_index - 1)
        self.next_index = self.next_index-1
        
        #current_node = self.cbt
        index = 0
        while self.cbt[index] is not None:
            #print(index)
            left = (index*2) + 1
            right = (index*2) + 2
            #print(left,right, self.next_index)
            if left <= self.next_index and right <= self.next_index:
                #print(self.cbt[index],self.cbt[left], self.cbt[right])
                if self.cbt[left] is not None:
                    #print('left not none')
                    if self.cbt[left] < self.cbt[index]:
                        #print('left small')
                        temp = self.cbt[left]
                        self.cbt[left] = self.cbt[index]
                        self.cbt[index] = temp
                        index = left
                if self.cbt[right] is not None:
                    #print('right not none')
                    if self.cbt[right] < self.cbt[index]:
                        #print('right small')
                        temp = self.cbt[right]
                        self.cbt[right] = self.cbt[index]
                        self.cbt[index] = temp
                        index = right
                return
            else:
                return

        return popped

heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(heap.cbt))

#heap.remove()

#print('Heap: {}'.format(heap.cbt))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Heap: {}'.format(heap.cbt))