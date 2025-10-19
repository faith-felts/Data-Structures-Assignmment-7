
class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  



class MinHeap:
    def __init__(self):
        self.data = []  

    def print_heap(self):
        print("\nCurrent Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            current = self.data[index] 
            parent = self.data[parent_index]
            if current.urgency < parent.urgency:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

       
                index = parent_index
            else: 
                break

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_patient



heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

heap.print_heap()

next_up = heap.peek()
if next_up:
    print(f"\nNext up: {next_up.name}, {next_up.urgency}")


served = heap.remove_min()
print(f"\nServed: {served.name}")
heap.print_heap()


# Why is a tree appropriate for the doctor structure?
# A tree is appropriate for the doctor structure because it accuratly represents hierarchical relationships.
# Each doctor can have subordinates (left and right children nodes), that need to be represented. 
# This structure allows for efficient organization, traversal, and visualization of the management hierarchy.
# Which makes it easy to identify supervisors, subordinates, and any other relationships within staff.
# 
# When might a software engineer use preorder, inorder, or postorder traversals?
# A software engineer could decide to use preorder traversal when they need to process parent nodes before their children.
# This could include things like printing a management structure or copying a tree. 
# Inorder traversal is often used for retrieving data in sorted order, such as in a binary search tree. 
# Postorder traversal is useful when child nodes must be processed before their parent.
# 
# How do heaps help simulate real-time systems like emergency intake?
# Heaps help simulate real-time systems like emergency intake by always keeping the most urgent item at the top. 
#In a min-heap, patients with lower urgency values are treated first. 
# This allows the system to efficiently insert new patients. It removes the most critical case and enshures that emergencies are prioritized and managed efficently.



